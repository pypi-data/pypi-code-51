import traceback
import json
import time
import logging
from thundra import config, constants
from thundra.plugins.invocation import invocation_support
from thundra.integrations.base_integration import BaseIntegration
from thundra.opentracing.tracer import ThundraTracer

try:
    from pymongo.monitoring import CommandListener
    from bson.json_util import dumps
except ImportError:
    CommandListener = object


logger = logging.getLogger(__name__)


class CommandTracer(CommandListener):
    _scopes = {}

    def started(self, event):
        tracer = ThundraTracer.get_instance()
        if not tracer.get_active_span():
            return

        scope = tracer.start_active_span(operation_name=event.database_name, finish_on_close=False)

        self._scopes[event.request_id] = scope
        span = scope.span

        # Inject before span tags
        try:
            command_name = event.command_name
            scope.span.class_name = constants.ClassNames['MONGODB']
            scope.span.domain_name = constants.DomainNames['DB']

            try:
                host, port = event.connection_id
            except:
                host, port = "", ""

            try:
                collection_name = next(iter(event.command.items()))[1]
            except:
                collection_name = ""

            operation_type = constants.MongoDBCommandTypes.get(command_name.upper(), '')

            tags = {
                constants.SpanTags['OPERATION_TYPE']: operation_type,
                constants.DBTags['DB_TYPE']: 'mongodb',
                constants.DBTags['DB_HOST']: host,
                constants.DBTags['DB_PORT']: port,
                constants.SpanTags['DB_INSTANCE']: event.database_name,
                constants.MongoDBTags['MONGODB_COMMAND_NAME']: command_name.upper(),
                constants.MongoDBTags['MONGODB_COLLECTION']: collection_name,
                constants.SpanTags['TRIGGER_OPERATION_NAMES']: [invocation_support.function_name],
                constants.SpanTags['TRIGGER_DOMAIN_NAME']: constants.LAMBDA_APPLICATION_DOMAIN_NAME,
                constants.SpanTags['TRIGGER_CLASS_NAME']: constants.LAMBDA_APPLICATION_CLASS_NAME,
                constants.SpanTags['TOPOLOGY_VERTEX']: True,
            }

            if not config.mongodb_command_masked():
                try:
                    tags[constants.MongoDBTags['MONGODB_COMMAND']] = dumps(event.command)[
                                                                   :constants.DEFAULT_MONGO_COMMAND_SIZE_LIMIT]
                except Exception as e:
                    tags[constants.MongoDBTags['MONGODB_COMMAND']] = ''

            scope.span.tags = tags

        except Exception as instrumentation_exception:
            e = {
                'type': str(type(instrumentation_exception)),
                'message': str(instrumentation_exception),
                'traceback': traceback.format_exc(),
                'time': time.time()
            }
            scope.span.set_tag('instrumentation_error', e)

        try:
            # Inform span that initialization completed
            scope.span.on_started()
        except Exception as e:
            logger.error(e)

    def succeeded(self, event):
        scope = self._scopes.pop(event.request_id, None)
        if scope is None:
            return
        span = scope.span
        try:
            scope.span.finish()
        except Exception as e:
            logger.error(e)

        scope.close()

    def failed(self, event):
        scope = self._scopes.pop(event.request_id, None)
        if scope is None:
            return

        scope.span.set_error_to_tag(event.failure)
        try:
            scope.span.finish()
        except Exception as e:
            logger.error(e)

        scope.close()
