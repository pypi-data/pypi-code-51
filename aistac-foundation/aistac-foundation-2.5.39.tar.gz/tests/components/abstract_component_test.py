import inspect
import unittest
import os
import shutil
from datetime import datetime
from pprint import pprint
import platform

import pandas as pd

from aistac.components.abstract_component import AbstractComponent
from aistac.handlers.abstract_handlers import ConnectorContract
from aistac.intent.python_cleaners_intent import PythonCleanersIntentModel
from aistac.properties.abstract_properties import AbstractPropertyManager
from aistac.properties.property_manager import PropertyManager

from tests.handlers.test_handlers import TestPersistHandler


class ControlPropertyManager(AbstractPropertyManager):

    def __init__(self, task_name):
        # set additional keys
        root_keys = []
        knowledge_keys = []
        super().__init__(task_name=task_name, root_keys=root_keys, knowledge_keys=knowledge_keys)


class ControlComponent(AbstractComponent):

    DEFAULT_MODULE = 'aistac.handlers.python_handlers'
    DEFAULT_SOURCE_HANDLER = 'PythonSourceHandler'
    DEFAULT_PERSIST_HANDLER = 'PythonPersistHandler'

    def __init__(self, property_manager: ControlPropertyManager, intent_model: PythonCleanersIntentModel,
                 default_save=None, reset_templates: bool = None, align_connectors: bool = None):
        super().__init__(property_manager=property_manager, intent_model=intent_model, default_save=default_save,
                         reset_templates=reset_templates, align_connectors=align_connectors)

    @classmethod
    def from_uri(cls, task_name: str, uri_pm_path: str, pm_file_type: str = None, pm_module: str = None,
                 pm_handler: str = None, pm_kwargs: dict = None, default_save=None):
        pm_file_type = pm_file_type if isinstance(pm_file_type, str) else 'pickle'
        pm_module = pm_module if isinstance(pm_module, str) else 'aistac.handlers.python_handlers'
        pm_handler = pm_handler if isinstance(pm_handler, str) else 'PythonPersistHandler'
        _pm = ControlPropertyManager(task_name=task_name)
        _intent_model = PythonCleanersIntentModel(property_manager=_pm)
        super()._init_properties(property_manager=_pm, uri_pm_path=uri_pm_path, pm_file_type=pm_file_type,
                                 pm_module=pm_module, pm_handler=pm_handler, pm_kwargs=pm_kwargs)
        return cls(property_manager=_pm, intent_model=_intent_model, default_save=default_save)

    @property
    def pm(self) -> ControlPropertyManager:
        return self._component_pm

    @property
    def intent_model(self) -> PythonCleanersIntentModel:
        return self._intent_model


class AbstractComponentTest(unittest.TestCase):

    def setUp(self):
        os.environ['AISTAC_PM_PATH'] = os.path.join(os.environ['PWD'], 'work')
        os.environ['AISTAC_PM_TYPE'] = 'yaml'
        self.pm_uri = os.environ.get('AISTAC_PM_PATH')
        PropertyManager._remove_all()

    def tearDown(self):
        try:
            shutil.rmtree(os.path.join(os.environ['PWD'], 'work'))
        except:
            pass

    def test_runs(self):
        """Basic smoke test"""
        ControlComponent.from_env('test')

    def test_intent_report(self):
        instance = ControlComponent.from_env('test')
        data = {'A': [1,2,3,4,5], 'B': [4,2,6,1,3]}
        data = instance.intent_model.auto_clean_header(data, case='upper')
        data = instance.intent_model.auto_remove_columns(data, predominant_max=0.98)
        result = instance.pm.report_intent()
        control = {'level': ['0', '0'], 'intent': ['auto_clean_header', 'auto_remove_columns'],
                   'parameters': [['case=upper'], ['predominant_max=0.98']]}
        self.assertDictEqual(control, result)

    def test_report_connectors(self):
        instance = ControlComponent.from_env('task')
        report = instance.pm.report_connectors()
        control = [instance.pm.CONNECTOR_PM_CONTRACT, instance.TEMPLATE_SOURCE, instance.TEMPLATE_PERSIST]
        self.assertCountEqual(control, report.get('connector_name'))
        control = ['PythonPersistHandler', 'PythonSourceHandler', 'PythonPersistHandler']
        self.assertCountEqual(control, report.get('handler'))
        control = ['aistac.handlers.python_handlers']*3
        self.assertCountEqual(control, report.get('module_name'))
        self.assertIn(os.environ.get('AISTAC_PM_PATH') + '/aistac_pm_control_task.yaml', report.get('uri'))

    def test_PM_from_env(self):
        os.environ['AISTAC_PM_PATH'] = "work/test/contracts?A=24&B=fred"
        os.environ['AISTAC_PM_TYPE'] = 'yaml'
        os.environ['AISTAC_PM_MODULE'] = 'tests.handlers.test_handlers'
        os.environ['AISTAC_PM_HANDLER'] = 'TestPersistHandler'
        instance = ControlComponent.from_env('task', encoding='Latin1')
        result = instance.pm.get_connector_contract(instance.pm.CONNECTOR_PM_CONTRACT)
        self.assertEqual('work/test/contracts/aistac_pm_control_task.yaml', result.uri)
        self.assertEqual('TestPersistHandler', result.handler)
        self.assertEqual('tests.handlers.test_handlers', result.module_name)
        self.assertDictEqual({'A': '24', 'B': 'fred', 'encoding': 'Latin1'}, result.kwargs)
        os.environ.pop('AISTAC_PM_PATH')
        os.environ.pop('AISTAC_PM_TYPE')
        os.environ.pop('AISTAC_PM_MODULE')
        os.environ.pop('AISTAC_PM_HANDLER')

    def test_DEFAULT_from_env(self):
        os.environ['AISTAC_DEFAULT_PATH'] = "AISTAC_DEFAULT_PATH?A=24&B=fred"
        os.environ['AISTAC_DEFAULT_MODULE'] = "tests.handlers.test_handlers"
        os.environ['AISTAC_DEFAULT_SOURCE_HANDLER'] = "TestSourceHandler"
        os.environ['AISTAC_DEFAULT_PERSIST_HANDLER'] = "TestPersistHandler"
        instance = ControlComponent.from_env('task', encoding='Latin1')
        source = instance.pm.get_connector_contract(instance.TEMPLATE_SOURCE)
        self.assertEqual('AISTAC_DEFAULT_PATH', source.uri)
        self.assertEqual('TestSourceHandler', source.handler)
        self.assertEqual('tests.handlers.test_handlers', source.module_name)
        self.assertDictEqual({'A': '24', 'B': 'fred'}, source.kwargs)
        persist = instance.pm.get_connector_contract(instance.TEMPLATE_PERSIST)
        self.assertEqual('AISTAC_DEFAULT_PATH', persist.uri)
        self.assertEqual('TestPersistHandler', persist.handler)
        self.assertEqual('tests.handlers.test_handlers', persist.module_name)
        self.assertDictEqual({'A': '24', 'B': 'fred'}, persist.kwargs)
        os.environ['AISTAC_CONTROL_PATH'] = "AISTAC_CONTROL_PATH?C=24&B=fred"
        os.environ['AISTAC_CONTROL_MODULE'] = "aistac.handlers.python_handlers"
        os.environ['AISTAC_CONTROL_SOURCE_HANDLER'] = "PythonSourceHandler"
        os.environ['AISTAC_CONTROL_PERSIST_HANDLER'] = "PythonPersistHandler"
        instance = ControlComponent.from_env('task')
        source = instance.pm.get_connector_contract(instance.TEMPLATE_SOURCE)
        self.assertEqual('AISTAC_CONTROL_PATH', source.uri)
        self.assertEqual('PythonSourceHandler', source.handler)
        self.assertEqual('aistac.handlers.python_handlers', source.module_name)
        self.assertDictEqual({'C': '24', 'B': 'fred'}, source.kwargs)
        persist = instance.pm.get_connector_contract(instance.TEMPLATE_PERSIST)
        self.assertEqual('AISTAC_CONTROL_PATH', persist.uri)
        self.assertEqual('PythonPersistHandler', persist.handler)
        self.assertEqual('aistac.handlers.python_handlers', persist.module_name)
        self.assertDictEqual({'C': '24', 'B': 'fred'}, persist.kwargs)
        os.environ.pop('AISTAC_DEFAULT_PATH')
        os.environ.pop('AISTAC_DEFAULT_MODULE')
        os.environ.pop('AISTAC_DEFAULT_SOURCE_HANDLER')
        os.environ.pop('AISTAC_DEFAULT_PERSIST_HANDLER')
        os.environ.pop('AISTAC_CONTROL_PATH')
        os.environ.pop('AISTAC_CONTROL_MODULE')
        os.environ.pop('AISTAC_CONTROL_SOURCE_HANDLER')
        os.environ.pop('AISTAC_CONTROL_PERSIST_HANDLER')

    def test_from_environ(self):
        os.environ['AISTAC_PM_PATH'] = "work/${BUCKET}/${TASK}"
        os.environ['AISTAC_PM_TYPE'] = 'pickle'
        os.environ['AISTAC_PM_MODULE'] = '${MODULE}'
        os.environ['AISTAC_PM_HANDLER'] = '${HANDLER}'
        os.environ['BUCKET'] = 'contracts'
        os.environ['TASK'] = 'task'
        os.environ['MODULE'] = 'aistac.handlers.python_handlers'
        os.environ['HANDLER'] = 'PythonPersistHandler'
        instance = ControlComponent.from_env('task')
        cc = instance.pm.get_connector_contract(connector_name=instance.pm.CONNECTOR_PM_CONTRACT)
        self.assertTrue(cc.uri.startswith('work/contracts/task/'))
        self.assertEqual("aistac.handlers.python_handlers", cc.module_name)
        self.assertEqual("PythonPersistHandler", cc.handler)
        self.assertTrue(cc.raw_uri.startswith('work/${BUCKET}/${TASK}/'))
        self.assertEqual("${MODULE}", cc.raw_module_name)
        self.assertEqual("${HANDLER}", cc.raw_handler)
        os.environ.pop('AISTAC_PM_PATH')
        os.environ.pop('AISTAC_PM_TYPE')
        os.environ.pop('AISTAC_PM_MODULE')
        os.environ.pop('AISTAC_PM_HANDLER')
        os.environ.pop('BUCKET')
        os.environ.pop('TASK')
        os.environ.pop('MODULE')
        os.environ.pop('HANDLER')

    def test_connector_file_pattern(self):
        manager = ControlComponent.from_env('task')
        state_connector = ConnectorContract(
            uri=manager.pm.file_pattern(prefix=f"{os.environ['AISTAC_PM_PATH']}/data/", connector_name='version', versioned=True),
            module_name=manager.DEFAULT_MODULE,
            handler=manager.DEFAULT_PERSIST_HANDLER,
            version="v1.01")
        temporal_connector = ConnectorContract(
            uri=manager.pm.file_pattern(prefix=f"{os.environ['AISTAC_PM_PATH']}/data/", connector_name='temporal', stamped='DAYS'),
            module_name=manager.DEFAULT_MODULE,
            handler=manager.DEFAULT_PERSIST_HANDLER)
        manager.add_connector_contract(connector_name='persist_book_state', connector_contract=state_connector)
        manager.add_connector_contract(connector_name='temporal_state', connector_contract=temporal_connector)
        manager.persist_canonical(connector_name='persist_book_state', canonical=pd.DataFrame({'A': [1,2,3,4]}))
        self.assertTrue(os.path.exists(f"{os.environ['AISTAC_PM_PATH']}/data/aistac_CONTROL_task_version_v1.01.pickle"))
        manager.persist_canonical(connector_name='temporal_state', canonical=pd.DataFrame({'A': [1,2,3,4]}))
        dt = datetime.now().strftime("%Y%m%d")
        self.assertTrue(os.path.exists(f"{os.environ['AISTAC_PM_PATH']}/data/aistac_CONTROL_task_temporal_{dt}.pickle"))

    def test_add_connector_uri(self):
        manager = ControlComponent.from_env('task')
        cc = ConnectorContract(uri="/usr/jdoe/code/local_file.pickle", module_name=manager.DEFAULT_MODULE,handler=manager.DEFAULT_PERSIST_HANDLER)
        manager.add_connector_contract(connector_name='connector', connector_contract=cc)
        self.assertEqual("/usr/jdoe/code/local_file.pickle", manager.pm.get_connector_contract(connector_name='connector').uri)

    def test_set_connector_version(self):
        manager = ControlComponent.from_env('task')
        cc = ConnectorContract(uri="local_file.pickle", module_name=manager.DEFAULT_MODULE,handler=manager.DEFAULT_PERSIST_HANDLER, version="v1.01")
        manager.add_connector_contract(connector_name='connector', connector_contract=cc)
        self.assertEqual("v1.01", manager.pm.get_connector_contract(connector_name='connector').version)
        manager.set_connector_version(connector_names='connector', version="v2.11")
        self.assertEqual("v2.11", manager.pm.get_connector_contract(connector_name='connector').version)

    def test_report_eviron(self):
        manager = ControlComponent.from_env('test', default_save=False)
        result = manager.report_environ(hide_not_set=False)
        control = {'AISTAC_CONTROL_HANDLER': 'not set',
                   'AISTAC_CONTROL_MODULE': 'not set',
                   'AISTAC_CONTROL_PATH': 'not set',
                   'AISTAC_CONTROL_PERSIST_HANDLER': 'not set',
                   'AISTAC_CONTROL_PERSIST_MODULE': 'not set',
                   'AISTAC_CONTROL_PERSIST_PATH': 'not set',
                   'AISTAC_CONTROL_SOURCE_HANDLER': 'not set',
                   'AISTAC_CONTROL_SOURCE_MODULE': 'not set',
                   'AISTAC_CONTROL_SOURCE_PATH': 'not set',
                   'AISTAC_CONTROL_TEST_HANDLER': 'not set',
                   'AISTAC_CONTROL_TEST_MODULE': 'not set',
                   'AISTAC_CONTROL_TEST_PATH': 'not set',
                   'AISTAC_CONTROL_TEST_PERSIST_HANDLER': 'not set',
                   'AISTAC_CONTROL_TEST_PERSIST_MODULE': 'not set',
                   'AISTAC_CONTROL_TEST_PERSIST_PATH': 'not set',
                   'AISTAC_CONTROL_TEST_SOURCE_HANDLER': 'not set',
                   'AISTAC_CONTROL_TEST_SOURCE_MODULE': 'not set',
                   'AISTAC_CONTROL_TEST_SOURCE_PATH': 'not set',
                   'AISTAC_DEFAULT_HANDLER': 'not set',
                   'AISTAC_DEFAULT_MODULE': 'not set',
                   'AISTAC_DEFAULT_PATH': 'not set',
                   'AISTAC_DEFAULT_PERSIST_HANDLER': 'not set',
                   'AISTAC_DEFAULT_PERSIST_MODULE': 'not set',
                   'AISTAC_DEFAULT_PERSIST_PATH': 'not set',
                   'AISTAC_DEFAULT_SOURCE_HANDLER': 'not set',
                   'AISTAC_DEFAULT_SOURCE_MODULE': 'not set',
                   'AISTAC_DEFAULT_SOURCE_PATH': 'not set',
                   'AISTAC_PM_HANDLER': 'not set',
                   'AISTAC_PM_MODULE': 'not set',
                   'AISTAC_PM_PATH': f"{os.environ.get('PWD')}/work",
                   'AISTAC_PM_TYPE': 'yaml'}
        self.assertDictEqual(control, result)

    def test_default_connector(self):
        manager = ControlComponent.from_env('task')
        # source
        connector = manager.pm.get_connector_contract(manager.TEMPLATE_SOURCE)
        self.assertEqual('/tmp/aistac/data', connector.uri)
        self.assertEqual('aistac.handlers.python_handlers', connector.module_name)
        self.assertEqual('PythonSourceHandler', connector.handler)
        # persist
        manager = ControlComponent.from_env('task')
        connector = manager.pm.get_connector_contract(manager.TEMPLATE_PERSIST)
        self.assertEqual('/tmp/aistac/data', connector.uri)
        self.assertEqual('aistac.handlers.python_handlers', connector.module_name)
        self.assertEqual('PythonPersistHandler', connector.handler)
        # set source
        manager.add_connector_from_template(connector_name='source', uri_file='mysource.pickle', template_name=manager.TEMPLATE_SOURCE)
        connector = manager.pm.get_connector_contract('source')
        self.assertEqual('/tmp/aistac/data/mysource.pickle', connector.uri)
        self.assertEqual('aistac.handlers.python_handlers', connector.module_name)
        self.assertEqual('PythonSourceHandler', connector.handler)
        # set persist
        manager.add_connector_from_template(connector_name='persist', uri_file='mypersist.pickle', template_name=manager.TEMPLATE_PERSIST)
        connector = manager.pm.get_connector_contract('persist')
        self.assertEqual('/tmp/aistac/data/mypersist.pickle', connector.uri)
        self.assertEqual('aistac.handlers.python_handlers', connector.module_name)
        self.assertEqual('PythonPersistHandler', connector.handler)

    def test_modify_connector_from_template(self):
        os.environ['AISTAC_DEFAULT_MODULE'] = 'aistac.handlers.dummy_handlers'
        os.environ['AISTAC_DEFAULT_SOURCE_HANDLER'] = 'DummySourceHandler'
        os.environ['AISTAC_DEFAULT_PERSIST_HANDLER'] = 'DummyPersistHandler'
        manager = ControlComponent.from_env('task')
        self.assertTrue(manager.pm.has_connector(manager.TEMPLATE_SOURCE))
        self.assertTrue(manager.pm.has_connector(manager.TEMPLATE_PERSIST))
        source = ConnectorContract(uri="/tmp/local/data/source_file.pickle", module_name=manager.DEFAULT_MODULE, handler=manager.DEFAULT_SOURCE_HANDLER)
        manager.add_connector_contract(connector_name='my_source', connector_contract=source, template_aligned=True)
        persist = ConnectorContract(uri="s3://bucket/path/persist_file.pickle", module_name=manager.DEFAULT_MODULE, handler=manager.DEFAULT_PERSIST_HANDLER)
        manager.add_connector_contract(connector_name='my_persist', connector_contract=persist, template_aligned=True)
        manager.reset_template_connectors(connector_names=['my_source', 'my_persist'])
        result = manager.pm.get_connector_contract('my_source')
        self.assertEqual('/tmp/aistac/data/source_file.pickle', result.uri)
        self.assertEqual('aistac.handlers.dummy_handlers', result.module_name)
        self.assertEqual('DummySourceHandler', result.handler)
        result = manager.pm.get_connector_contract('my_persist')
        self.assertEqual('/tmp/aistac/data/persist_file.pickle', result.uri)
        self.assertEqual('aistac.handlers.dummy_handlers', result.module_name)
        self.assertEqual('DummyPersistHandler', result.handler)
        os.environ.pop('AISTAC_DEFAULT_MODULE')
        os.environ.pop('AISTAC_DEFAULT_SOURCE_HANDLER')
        os.environ.pop('AISTAC_DEFAULT_PERSIST_HANDLER')


if __name__ == '__main__':
    unittest.main()
