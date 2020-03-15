# -*- coding: utf-8 -*-
import functools

from spaceone.api.inventory.v1 import ip_address_pb2
from spaceone.core.pygrpc.message_type import *
from spaceone.inventory.model.ip_address_model import IPAddress
from spaceone.inventory.info.subnet_info import SubnetInfo
from spaceone.inventory.info.network_info import NetworkInfo
from spaceone.inventory.info.zone_info import ZoneInfo

__all__ = ['IPInfo', 'IPsInfo']


def ResourceInfo(resource):
    info = {
        'type': resource.type,
        'id': resource.id
    }

    return ip_address_pb2.Resource(**info)


def IPInfo(ip_vo: IPAddress, minimal=False):
    info = {
        'ip_address': ip_vo.ip_address,
        'state': ip_vo.state
    }

    if not minimal:
        info.update({
            'subnet_info': SubnetInfo(ip_vo.subnet, minimal=True),
            'network_info': NetworkInfo(ip_vo.network, minimal=True),
            'zone_info': ZoneInfo(ip_vo.zone, minimal=True),
            'data': change_struct_type(ip_vo.data),
            'metadata': change_struct_type(ip_vo.metadata),
            'domain_id': ip_vo.domain_id,
            'updated_at': change_timestamp_type(ip_vo.updated_at)
        })

        if ip_vo.resource is not None:
            info.update({
                'resource': ResourceInfo(ip_vo.resource),
            })

    return ip_address_pb2.IPInfo(**info)


def IPsInfo(ip_vos, total_count, **kwargs):
    return ip_address_pb2.IPsInfo(results=list(map(functools.partial(IPInfo, **kwargs), ip_vos)), total_count=total_count)
