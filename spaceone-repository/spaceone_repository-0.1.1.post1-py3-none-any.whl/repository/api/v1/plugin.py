# -*- coding: utf-8 -*-

from spaceone.api.repository.v1 import plugin_pb2, plugin_pb2_grpc
from spaceone.core.pygrpc import BaseAPI


class Plugin(BaseAPI, plugin_pb2_grpc.PluginServicer):

    pb2 = plugin_pb2
    pb2_grpc = plugin_pb2_grpc

    def register(self, request, context):
        """Register Plugin.

        Returns:
            PluginInfo

        Raises:
            ERROR_NOT_FOUND: 
                - project_id is not valid value
                - service_type has wrong format
        """
        params, metadata = self.parse_request(request, context)
        with self.locator.get_service('PluginService', metadata) as plugin_svc:
            plugin_data = plugin_svc.register(params)
            return self.locator.get_info('PluginInfo', plugin_data)

    def update(self, request, context):
        params, metadata = self.parse_request(request, context)
        with self.locator.get_service('PluginService', metadata) as plugin_svc:
            plugin_data = plugin_svc.update(params)
            return self.locator.get_info('PluginInfo', plugin_data)

    def deregister(self, request, context):
        params, metadata = self.parse_request(request, context)
        with self.locator.get_service('PluginService', metadata) as plugin_svc:
            plugin_data = plugin_svc.deregister(params)
            return self.locator.get_info('EmptyInfo')

    def enable(self, request, context):
        params, metadata = self.parse_request(request, context)
        with self.locator.get_service('PluginService', metadata) as plugin_svc:
            plugin_data = plugin_svc.enable(params)
            return self.locator.get_info('PluginInfo', plugin_data)

    def disable(self, request, context):
        params, metadata = self.parse_request(request, context)
        with self.locator.get_service('PluginService', metadata) as plugin_svc:
            plugin_data = plugin_svc.disable(params)
            return self.locator.get_info('PluginInfo', plugin_data)

    def get_versions(self, request, context):
        params, metadata = self.parse_request(request, context)
        with self.locator.get_service('PluginService', metadata) as plugin_svc:
            version_data = plugin_svc.get_versions(params)
            return self.locator.get_info('VersionsInfo', version_data)

    def get(self, request, context):
        params, metadata = self.parse_request(request, context)
        with self.locator.get_service('PluginService', metadata) as plugin_svc:
            plugin_data = plugin_svc.get(params)
            return self.locator.get_info('PluginInfo', plugin_data)

    def list(self, request, context):
        params, metadata = self.parse_request(request, context)
        with self.locator.get_service('PluginService', metadata) as plugin_svc:
            plugins_data, total_count = plugin_svc.list(params)
            return self.locator.get_info('PluginsInfo', plugins_data, total_count) 
