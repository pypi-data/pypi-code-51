# -*- coding: utf-8 -*-

__all__ = ['PluginManager']

import consul
import logging
import time

from spaceone.core import config
from spaceone.core import pygrpc
from spaceone.core.error import *
from spaceone.core.auth.jwt.jwt_util import JWTUtil
from spaceone.core.manager import BaseManager
from spaceone.core.pygrpc.message_type import *

from spaceone.repository.model import *
from spaceone.repository.error.custom import *
from spaceone.repository.manager.plugin_manager import PluginManager

_LOGGER = logging.getLogger(__name__)


INTERVAL = 10
def _validate_token(token):
    if isinstance(token, dict):
        protocol = token['protocol']
        if protocol == 'consul':
            consul_instance = Consul(token['config'])
            value = False
            count = 0
            while value is False:
                value = consul_instance.patch_token(token['uri'])
                _LOGGER.warn(f'[_validate_token] token: {value}')
                if value:
                    break
                time.sleep(INTERVAL)

            token = value

    _LOGGER.debug(f'[_validate_token] token: {token}')
    return token


class RemotePluginManager(PluginManager):
    """
    self.repository (=repository_vo)
    Remote Plugin make gRPC call to remote repository (like marketplace)
    If connector gets plugin_info, this is gRPC message.
    """

    def register_plugin(self, params):
        def _rollback(plugin_vo):
            plugin_vo.delete()

        self.plugin_model.create(params)
        self.transaction.add_rollback(_rollback, plugin_vo)

    def get_plugin(self, plugin_id, domain_id):
        """
        Args:
            - plugin_id
            - domain_id : my domain_id
        """
        conn = self._get_conn_from_repository(self.repository, domain_id)
        connector = self.locator.get_connector('RepositoryConnector', conn=conn) 

        # plugin_info, dict
        plugin_info = connector.get_plugin(plugin_id)
        return self._get_updated_plugin_info(plugin_info)        

    def list_plugins(self, query, domain_id):
        conn = self._get_conn_from_repository(self.repository, domain_id)
        connector = self.locator.get_connector('RepositoryConnector', conn=conn) 

        # Notice:
        # query should be JSON style query, not gRPC
        #

        response = connector.list_plugins(query)
        _LOGGER.debug(f'[remote list_plugin] {response}')

        for plugin_info in response.results:
            # Warning:
            # This is side effect coding, since plugin_vo is protobuf message
            self._get_updated_plugin_info(plugin_info)  
        return response.results, response.total_count

    def get_plugin_versions(self, plugin_id, domain_id):
        """ Get version of image

        version: tag list of docker image
        create RegistryConnector
        call get_tags()

        Returns:
            A list of docker tag
        """
        plugin = self.get_plugin(plugin_id, domain_id)

        connector = self.locator.get_connector("RegistryConnector")
        tags = connector.get_tags(plugin.image)
        return tags
       
    def _get_conn_from_repository(self, repo, domain_id):
        """
        self.repository (repository_vo)

        Args:
            - repo: repository_vo (= self.repository)
            - domain_id: domain_id of credential
        """
        cred_id = repo.credential_id
        credentials = self._issue_credentials(cred_id, domain_id)
        conn = {
            'endpoint': repo.endpoint,
            'version': repo.version,
            'credential': {'token': credentials['token']}
        }
        return conn

    def _get_updated_plugin_info(self, plugin_info):
        """
        plugin_info is Protobuf Message
        We want to change our plugin_info (especially repository_info)

        Args:
            - plugin_info: protobuf message
        """
        # domain_id is remote repository's domain_id
        # change to local repository's domain_id  
        # There is no way to find domain_id
        # TODO: plugin_info.domain_id = self.repository.domain_id

        plugin_info.repository_info.name = self.repository.name
        plugin_info.repository_info.repository_type = self.repository.repository_type
        return plugin_info

    ###############################
    # Credential/CredentialGroup
    ###############################
    def _issue_credentials(self, credential_id, domain_id):
        """ Return secret data
        """
        root_token = config.get_global('ROOT_TOKEN')
        root_token_info = config.get_global('ROOT_TOKEN_INFO')

        root_domain_id = domain_id
        if root_token is not "":
            root_domain_id = self._get_domain_id_from_token(root_token)
            _LOGGER.debug(f'[_issue_credentials] root_domain_id: {root_domain_id} vs domain_id: {domain_id}')
        elif root_token_info:
            # Patch from Consul
            _LOGGER.debug(f'[_issue_credentials] Patch root_token from Consul')
            root_token = _validate_token(root_token_info)
            root_domain_id = self._get_domain_id_from_token(root_token)
        else:
            _LOGGER.warn(f'[_issue_credentials] root_token is not configured, may be your are root')
            root_token = self.transaction.get_meta('token')

        connector = self.locator.get_connector('SecretConnector', token=root_token, domain_id=root_domain_id)
        cred = connector.issue_credentials(credential_id, root_domain_id)
        return cred.secret

    def _get_domain_id_from_token(self, token):
        decoded_token = JWTUtil.unverified_decode(token)
        return decoded_token['did']


class Consul:
    def __init__(self, config):
        """
        Args:
          - config: connection parameter

        Example:
            config = {
                    'host': 'consul.example.com',
                    'port': 8500
                }
        """
        self.config = self._validate_config(config)

    def _validate_config(self, config):
        """
        Parameter for Consul
        - host, port=8500, token=None, scheme=http, consistency=default, dc=None, verify=True, cert=None
        """
        options = ['host', 'port', 'token', 'scheme', 'consistency', 'dc', 'verify', 'cert']
        result = {}
        for item in options:
            value = config.get(item, None)
            if value:
              result[item] = value
        return result

    def patch_token(self, key):
        """
        Args:
            key: Query key (ex. /debug/supervisor/TOKEN)

        """
        try:
            conn = consul.Consul(**self.config)
            index, data = conn.kv.get(key)
            return data['Value'].decode('ascii')

        except Exception as e:
            return False
