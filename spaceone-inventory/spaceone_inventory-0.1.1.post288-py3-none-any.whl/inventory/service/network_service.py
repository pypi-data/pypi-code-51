# -*- coding: utf-8 -*-
from spaceone.core.service import *
from spaceone.inventory.manager.network_manager import NetworkManager
from spaceone.inventory.manager.subnet_manager import SubnetManager
from spaceone.inventory.manager.zone_manager import ZoneManager
from spaceone.inventory.manager.collection_data_manager import CollectionDataManager
from spaceone.inventory.lib.ip_address import IPAddress
from spaceone.inventory.error import *


@authentication_handler
@authorization_handler
@event_handler
class NetworkService(BaseService):

    def __init__(self, metadata):
        super().__init__(metadata)
        self.network_mgr: NetworkManager = self.locator.get_manager('NetworkManager')

    @transaction
    @check_required(['cidr', 'zone_id', 'domain_id'])
    def create(self, params):
        """
        Args:
            params (dict): {
                    'name': 'str',
                    'cidr': 'str',
                    'data': 'dict',
                    'tags': 'dict',
                    'zone_id': 'str',
                    'domain_id': 'str'
                }

        Returns:
            network_vo (object)

        """

        collection_data_mgr: CollectionDataManager = self.locator.get_manager('CollectionDataManager')

        domain_id = params['domain_id']

        collector_id = self.transaction.get_meta('collector_id')
        job_id = self.transaction.get_meta('job_id')

        params['collection_info'] = collection_data_mgr.create_new_history(params,
                                                                           domain_id,
                                                                           collector_id,
                                                                           exclude_keys=['domain_id'])

        zone_mgr: ZoneManager = self.locator.get_manager('ZoneManager')
        zone_vo = zone_mgr.get_zone(params.get('zone_id'), params.get('domain_id'))

        params.update({
            'zone': zone_vo,
            'region': zone_vo.region,
            'cidr': self._check_cidr(params.get('cidr'), zone_vo)
        })

        return self.network_mgr.create_network(params)

    @transaction
    @check_required(['network_id', 'domain_id'])
    def update(self, params):
        """
        Args:
            params (dict): {
                    'network_id': 'str',
                    'name': 'str',
                    'data': 'dict',
                    'tags': 'dict',
                    'domain_id': 'str'
                }

        Returns:
            network_vo (object)

        """

        collection_data_mgr: CollectionDataManager = self.locator.get_manager('CollectionDataManager')

        domain_id = params['domain_id']

        collector_id = self.transaction.get_meta('collector_id')
        job_id = self.transaction.get_meta('job_id')

        network_vo = self.network_mgr.get_network(params.get('network_id'), domain_id)

        params = collection_data_mgr.exclude_data_by_pinned_keys(params, network_vo.collection_info)
        params = collection_data_mgr.exclude_data_by_history(params,
                                                             domain_id,
                                                             network_vo.collection_info,
                                                             collector_id,
                                                             exclude_keys=['network_id', 'domain_id'])

        if 'data' in params:
            params['data'] = collection_data_mgr.merge_data(network_vo.data, params['data'])

        if 'metadata' in params:
            params['metadata'] = collection_data_mgr.merge_metadata(network_vo.metadata, params['metadata'])

        return self.network_mgr.update_network_by_vo(params, network_vo)

    @transaction
    @check_required(['network_id', 'keys', 'domain_id'])
    def pin_data(self, params):
        """
        Args:
            params (dict): {
                    'network_id': 'str',
                    'keys': 'list',
                    'domain_id': 'str'
                }

        Returns:
            cloud_service_vo (object)

        """

        collection_data_mgr: CollectionDataManager = self.locator.get_manager('CollectionDataManager')

        network_vo = self.network_mgr.get_network(params.get('network_id'), params.get('domain_id'))

        params['collection_info'] = collection_data_mgr.update_pinned_keys(params['keys'],
                                                                           network_vo.collection_info)

        return self.network_mgr.update_network_by_vo(params, network_vo)

    @transaction
    @check_required(['network_id', 'domain_id'])
    def delete(self, params):
        """
        Args:
            params (dict): {
                    'network_id': 'str',
                    'domain_id': 'str'
                }

        Returns:
            None

        """

        network_vo = self.network_mgr.get_network(params.get('network_id'), params.get('domain_id'))
        self._check_subnet(network_vo)
        self.network_mgr.delete_network_vo(network_vo)

    @transaction
    @check_required(['network_id', 'domain_id'])
    def get(self, params):
        """
        Args:
            params (dict): {
                    'network_id': 'str',
                    'domain_id': 'str'
                }

        Returns:
            network_vo (object)

        """

        return self.network_mgr.get_network(params.get('network_id'), params.get('domain_id'))

    @transaction
    @check_required(['domain_id'])
    @append_query_filter(['network_id', 'name', 'cidr', 'zone_id', 'region_id', 'domain_id'])
    def list(self, params):
        """
        Args:
            params (dict): {
                    'network_id': 'str',
                    'name': 'str',
                    'cidr': 'str',
                    'zone_id': 'str',
                    'region_id': 'str',
                    'domain_id': 'str',
                    'query': 'dict'
                }

        Returns:
            results (list)
            total_count (int)

        """

        return self.network_mgr.list_networks(params.get('query', {}))

    @staticmethod
    def _check_duplicate_cidr(cidr1, cidr2):
        if IPAddress.check_duplicate_cidr_range(cidr1, cidr2):
            raise ERROR_DUPLICATE_CIDR(cidr1=cidr1, cidr2=cidr2)

    def _check_cidr(self, cidr, zone_vo):
        cidr = IPAddress.check_valid_network(cidr)

        if cidr is False:
            raise ERROR_INVALID_NETWORK(cidr=cidr)

        '''
        net_vos, total_count = self.network_mgr.list_networks({
            'filter': [{
                'k': 'zone',
                'v': zone_vo.id,
                'o': 'eq'
            }]
        })

        list(map(lambda net_vo: self._check_duplicate_cidr(cidr, net_vo.cidr), net_vos))
        '''

        return cidr

    def _check_subnet(self, network_vo):
        subnet_mgr: SubnetManager = self.locator.get_manager('SubnetManager')
        subnet_vos, total_count = subnet_mgr.list_subnets({'filter': [{'k': 'network', 'v': network_vo.id, 'o': 'eq'}]})
        if total_count > 0:
            raise ERROR_EXIST_SUBNET_IN_NETWORK(subnet_id=subnet_vos[0].subnet_id, network_id=network_vo.network_id)
