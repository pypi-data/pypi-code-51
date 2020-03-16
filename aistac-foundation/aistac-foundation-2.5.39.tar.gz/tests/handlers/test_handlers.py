import os
from contextlib import closing
import threading
import yaml
try:
    import cPickel as pickle
except ImportError:
    import pickle

from aistac.handlers.abstract_handlers import AbstractSourceHandler, ConnectorContract, AbstractPersistHandler
from aistac.handlers.parsers import DelimitedParser

__author__ = 'Darryl Oatridge'


class TestSourceHandler(AbstractSourceHandler):
    """ A simple pure Python data source handler. The format of the uri should be as a minimum:
                    uri = '/path/filename.ext'
        but can be a full url
                    uri = scheme://netloc/path/filename.ext

        recognised value pair parameters for file read and write are:
        - file_type: if the file extension is not in the list of 'supported_type'
        - encoding: if there is a specific encoding needed

        in addition the file parser takes the following value pair parameters:
        restkey: If row has more fields than fieldnames, remaining data is put in a list under restkey
        - restval: If non-blank row has fewer fields than fieldnames, values are filled-in with restval
        - dialect: Dialect class grouping formatting parameters
        - delimiter: A one-character string used to separate fields. It defaults to ','.
        - quotechar: A one-character string used to quote fields containing special characters, such as the
                    delimiter or quotechar, or which contain new-line characters. It defaults to '"'.
        - escapechar: A one-character string used by the writer to escape the delimiter if quoting is set to
                    QUOTE_NONE and the quotechar if doublequote is False.
        - doublequote: Controls how instances of quotechar appearing inside a field should themselves be quoted.
                    When True, the character is doubled. Default
                    When False, the escapechar is used as a prefix to the quotechar
        - skipinitialspace: When True, whitespace immediately following the delimiter is ignored. Default False
        - lineterminator: The string used to terminate lines produced by the writer.
        - quoting: Controls when quotes should be generated by the writer and recognised by the reader

    """

    def __init__(self, connector_contract: ConnectorContract):
        """ initialise the Handler passing the source_contract dictionary """
        super().__init__(connector_contract)

    def supported_types(self) -> list:
        """ The source types supported with this module"""
        return ['pickle', 'yaml', 'csv', 'tsv', 'dsv', 'txt']

    def load_canonical(self, **kwargs) -> dict:
        """ returns the canonical dataset.

        Extra Parameters in the ConnectorContract kwargs:
            - file_type: (optional) the type of the source file. if not set, inferred from the file extension
            - read_params: (optional) value pair dict of parameters to pass to the read methods. Underlying
                           read methods DelimitedParser.read_dsv and pickle.load
        """
        _cc = self.connector_contract
        if not isinstance(_cc, ConnectorContract):
            raise ValueError("The Python Source Connector Contract has not been set correctly")
        _, _, _ext = _cc.address.rpartition('.')
        # pop all the extra params
        cc_params = _cc.kwargs
        cc_params.update(_cc.query)  # Update kwargs with those in the uri query
        cc_params.update(kwargs)     # Update with any passed though the call
        read_params = cc_params.pop('read_params', {})
        file_type = cc_params.pop('file_type', _ext if len(_ext) > 0 else 'dsv')
        if file_type.lower() in ['pkl', 'pickle']:
            rtn_data = self._pickle_load(path_file=_cc.address, **read_params)
        elif file_type.lower() in ['csv', 'tsv', 'dsv', 'txt']:
            rtn_data = self._csv_load(path_file=_cc.address, **read_params)
        elif file_type.lower() in ['yml', 'yaml']:
            rtn_data = self._yaml_load(path_file=_cc.address, **read_params)
        else:
            raise ValueError("PythonPersistHandler only supports 'pickle, pkl, csv, tsv, dsv' source type,"
                             " '{}' found in Source Contract source-type".format(file_type))
        return rtn_data

    def exists(self) -> bool:
        """ Returns True is the file exists """
        if os.path.exists(self.connector_contract.address):
            return True
        return False

    def get_modified(self) -> [int, float, str]:
        """ returns if the file has been modified"""
        _cc = self.connector_contract
        if not isinstance(_cc, ConnectorContract):
            return False
        return os.stat(_cc.address)[8] if os.path.exists(_cc.address) else 0

    @staticmethod
    def _yaml_load(path_file, **kwargs) -> dict:
        """ loads the YAML file

        :param path_file: the name and path of the file
        :return: a dictionary
        """
        encoding = kwargs.pop('encoding', 'utf-8')
        with threading.Lock():
            try:
                with closing(open(path_file, mode='r', encoding=encoding)) as ymlfile:
                    rtn_dict = yaml.safe_load(ymlfile)
            except IOError as e:
                raise IOError("The yaml file {} failed to open with: {}".format(path_file, e))
            if not isinstance(rtn_dict, dict) or not rtn_dict:
                raise TypeError("The yaml file {} could not be loaded as a dict type".format(path_file))
            return rtn_dict

    @staticmethod
    def _csv_load(path_file: str, **kwargs) -> dict:
        """ loads a csv file """
        encoding = kwargs.pop('encoding', 'utf-8')
        with threading.Lock():
            with closing(open(path_file, mode="r", encoding=encoding)) as f:
                return DelimitedParser.read_dsv(f, **kwargs)

    @staticmethod
    def _pickle_load(path_file: str, **kwargs) -> dict:
        """ loads a pickle file """
        fix_imports = kwargs.pop('fix_imports', True)
        encoding = kwargs.pop('encoding', 'ASCII')
        errors = kwargs.pop('errors', 'strict')
        with threading.Lock():
            with closing(open(path_file, mode='rb')) as f:
                return pickle.load(f, fix_imports=fix_imports, encoding=encoding, errors=errors)


class TestPersistHandler(TestSourceHandler, AbstractPersistHandler):
    """ A simple pure Python data persist handler. The format of the uri should be as a minimum:
                    uri = '/path/filename.ext'
        but can be a full url
                    uri = scheme://netloc/path/filename.ext

        recognised value pair parameters for file read and write are:
        - file_type: if the file extension is not in the list of 'supported_type'
        - encoding: if there is a specific encoding needed

        in addition the file parser takes the following value pair parameters:
        restkey: If row has more fields than fieldnames, remaining data is put in a list under restkey
        - restval: If non-blank row has fewer fields than fieldnames, values are filled-in with restval
        - dialect: Dialect class grouping formatting parameters
        - delimiter: A one-character string used to separate fields. It defaults to ','.
        - quotechar: A one-character string used to quote fields containing special characters, such as the
                    delimiter or quotechar, or which contain new-line characters. It defaults to '"'.
        - escapechar: A one-character string used by the writer to escape the delimiter if quoting is set to
                    QUOTE_NONE and the quotechar if doublequote is False.
        - doublequote: Controls how instances of quotechar appearing inside a field should themselves be quoted.
                    When True, the character is doubled. Default
                    When False, the escapechar is used as a prefix to the quotechar
        - skipinitialspace: When True, whitespace immediately following the delimiter is ignored. Default False
        - lineterminator: The string used to terminate lines produced by the writer.
        - quoting: Controls when quotes should be generated by the writer and recognised by the reader

    """

    def persist_canonical(self, canonical: dict, **kwargs) -> bool:
        """ persists the canonical dataset """
        if not isinstance(self.connector_contract, ConnectorContract):
            return False
        return self.backup_canonical(uri=self.connector_contract.uri, canonical=canonical,
                                     ignore_kwargs=False, **kwargs)

    def remove_canonical(self) -> bool:
        _cc = self.connector_contract
        if not isinstance(_cc, ConnectorContract):
            return False
        if os.path.exists(_cc.address):
            os.remove(_cc.address)
            return True
        return False

    def backup_canonical(self, canonical: dict, uri: str, **kwargs):
        """ creates a backup of the canonical to am alternative URI
            NOTE: This only takes the 'address' part of the URI and not any query or param elements

        Extra Parameters in the ConnectorContract kwargs:
            - file_type: (optional) the type of the source file. if not set, inferred from the file extension
            - write_params (optional) a dictionary of additional write parameters directly passed to 'write_' methods
                            DelimitedParser.write_dsv (also takes encoding) and pickle.dump

        """
        _cc = self.connector_contract
        if not isinstance(_cc, ConnectorContract):
            return False
        persist_params = kwargs if isinstance(kwargs, dict) else _cc.kwargs
        persist_params.update(_cc.parse_query(uri=uri))
        _, _, _ext = _cc.address.rpartition('.')
        write_params = persist_params.pop('write_params', {})
        file_type = persist_params.pop('file_type', _ext if len(_ext) > 0 else 'dsv')
        _path, _ = os.path.split(_cc.path)
        if len(_path) > 0 and not os.path.exists(_path):
            os.makedirs(_path)

        # pickle
        if file_type.lower() in ['pkl', 'pickle']:
            self._pickle_dump(data=canonical, path_file=_cc.address, **write_params)
            return True
        # yaml
        elif file_type.lower() in ['csv', 'tsv', 'dsv', 'txt']:
            self._csv_dump(data=canonical, path_file=_cc.address, **write_params)
            return True
        # yaml
        if file_type.lower() in ['yml', 'yaml']:
            self._yaml_dump(data=canonical, path_file=_cc.address, **write_params)
            return True
        # not found
        raise ValueError("PythonPersistHandler only supports 'pickle', 'pkl' and 'csv' source type,"
                         " '{}' found in Source Contract source-type".format(file_type))

    @staticmethod
    def _yaml_dump(data, path_file, **kwargs) -> None:
        """ dump YAML file

        :param data: the data to persist
        :param path_file: the name and path of the file
        :param default_flow_style: (optional) if to include the default YAML flow style
        """
        encoding = kwargs.pop('encoding', 'utf-8')
        default_flow_style = kwargs.pop('default_flow_style', False)
        with threading.Lock():
            # make sure the dump is clean
            try:
                with closing(open(path_file, mode='w', encoding=encoding)) as ymlfile:
                    yaml.safe_dump(data=data, stream=ymlfile, default_flow_style=default_flow_style, **kwargs)
            except IOError as e:
                raise IOError("The yaml file {} failed to open with: {}".format(path_file, e))
        # check the file was created
        return

    @staticmethod
    def _csv_dump(canonical: dict, path_file: str, **kwargs) -> None:
        """ loads a csv file """
        encoding = kwargs.pop('encoding', 'utf-8')
        with threading.Lock():
            with closing(open(path_file, mode="w", encoding=encoding)) as f:
                DelimitedParser.write_dsv(canonical=canonical, file_stream=f, **kwargs)

    @staticmethod
    def _pickle_dump(data: dict, path_file: str, **kwargs) -> None:
        """ dumps a pickle file"""
        protocol = kwargs.pop('protocol', pickle.HIGHEST_PROTOCOL)
        fix_imports = kwargs.pop('fix_imports', True)
        with threading.Lock():
            with closing(open(path_file, mode='wb')) as f:
                pickle.dump(data, f, protocol=protocol, fix_imports=fix_imports)
