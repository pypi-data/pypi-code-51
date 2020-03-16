import time
import statsd
import functools
import socket
from .metrics import create_external_service_duration_metrics, create_function_duration_metrics, create_external_io_counter_metric_name
from .metrics import add_label_to_metric_name, logger


def collect_external_io_metrics(metric_prefix_app_name, service_name, service_address=None):
    """
        Decorator to collect metrics from the wrapper function.
        It returns the following metrics:
            1. app_name_external_io_duration_ms.service_name.service_address.status:

               Here both service_name and service_address becomes labels
               where 'status' can be 'success' or 'error'

            2. Errors counter while calling service. Uses exception to measure error and the name is
               the same as for previous metric since timing metric allow counts as well. The status wll be
               'error' if any exceptions are raised inside the decorated function.
        Attributes:
        service_address: defaults to hostname of the host running this code @TODO
    """
    if not service_address:
        service_address = socket.gethostname()
    def inner_func(func):
        @functools.wraps(func)
        def wrapper_decorator(*args, **kwargs):
            start_time = time.time()
            try:
                value = func(*args, **kwargs)
                end_time = time.time()
                duration_ms = (end_time - start_time)*1000
                status = 'success'

            except Exception as e:
                status = 'error'
                end_time = time.time()
                duration_ms = (end_time - start_time)*1000

                exception_type = e.__class__.__name__
                create_external_service_duration_metrics(status, duration_ms, metric_prefix_app_name, service_name, service_address, exception_type)

                raise

            else:
                create_external_service_duration_metrics(status, duration_ms, metric_prefix_app_name, service_name, service_address)

            finally:
                external_io_counter = create_external_io_counter_metric_name(metric_prefix_app_name)
                external_io_counter = add_label_to_metric_name(service_name, external_io_counter)
                external_io_counter = add_label_to_metric_name(service_address, external_io_counter)
                logger.debug('Incremented histogram metric {}'.format(external_io_counter))

            return value
        return wrapper_decorator
    return inner_func


def collect_function_duration_metrics(metric_prefix_app_name, function_name, host=None):
    """
        Pushes metrics that measure function runtime as histogram and exception type counter
    """
    if not host:
        host = socket.gethostname()
    def inner_func(func):
        @functools.wraps(func)
        def wrapper_decorator(*args, **kwargs):
            start_time = time.time()
            try:
                value = func(*args, **kwargs)
                end_time = time.time()
                duration_ms = (end_time - start_time)*1000

            except Exception as e:
                status = 'error'
                end_time = time.time()
                duration_ms = (end_time - start_time)*1000
                exception_type = e.__class__.__name__
                create_function_duration_metrics(duration_ms, metric_prefix_app_name, function_name, host, status, exception_type)
                raise

            else:
                status = 'success'
                create_function_duration_metrics(duration_ms, metric_prefix_app_name, function_name, host, status)

            return value
        return wrapper_decorator
    return inner_func
