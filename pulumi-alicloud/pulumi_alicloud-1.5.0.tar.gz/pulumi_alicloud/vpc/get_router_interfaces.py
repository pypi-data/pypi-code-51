# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetRouterInterfacesResult:
    """
    A collection of values returned by getRouterInterfaces.
    """
    def __init__(__self__, id=None, ids=None, interfaces=None, name_regex=None, names=None, opposite_interface_id=None, opposite_interface_owner_id=None, output_file=None, role=None, router_id=None, router_type=None, specification=None, status=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        __self__.ids = ids
        """
        A list of router interface IDs.
        """
        if interfaces and not isinstance(interfaces, list):
            raise TypeError("Expected argument 'interfaces' to be a list")
        __self__.interfaces = interfaces
        """
        A list of router interfaces. Each element contains the following attributes:
        """
        if name_regex and not isinstance(name_regex, str):
            raise TypeError("Expected argument 'name_regex' to be a str")
        __self__.name_regex = name_regex
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        __self__.names = names
        """
        A list of router interface names.
        """
        if opposite_interface_id and not isinstance(opposite_interface_id, str):
            raise TypeError("Expected argument 'opposite_interface_id' to be a str")
        __self__.opposite_interface_id = opposite_interface_id
        """
        Peer router interface ID.
        """
        if opposite_interface_owner_id and not isinstance(opposite_interface_owner_id, str):
            raise TypeError("Expected argument 'opposite_interface_owner_id' to be a str")
        __self__.opposite_interface_owner_id = opposite_interface_owner_id
        """
        Account ID of the owner of the peer router interface.
        """
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        __self__.output_file = output_file
        if role and not isinstance(role, str):
            raise TypeError("Expected argument 'role' to be a str")
        __self__.role = role
        """
        Router interface role. Possible values: `InitiatingSide` and `AcceptingSide`.
        """
        if router_id and not isinstance(router_id, str):
            raise TypeError("Expected argument 'router_id' to be a str")
        __self__.router_id = router_id
        """
        ID of the VRouter located in the local region.
        """
        if router_type and not isinstance(router_type, str):
            raise TypeError("Expected argument 'router_type' to be a str")
        __self__.router_type = router_type
        """
        Router type in the local region. Possible values: `VRouter` and `VBR`.
        """
        if specification and not isinstance(specification, str):
            raise TypeError("Expected argument 'specification' to be a str")
        __self__.specification = specification
        """
        Router interface specification. Possible values: `Small.1`, `Middle.1`, `Large.2`, ...etc.
        """
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        __self__.status = status
        """
        Router interface status. Possible values: `Active`, `Inactive` and `Idle`.
        """
class AwaitableGetRouterInterfacesResult(GetRouterInterfacesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRouterInterfacesResult(
            id=self.id,
            ids=self.ids,
            interfaces=self.interfaces,
            name_regex=self.name_regex,
            names=self.names,
            opposite_interface_id=self.opposite_interface_id,
            opposite_interface_owner_id=self.opposite_interface_owner_id,
            output_file=self.output_file,
            role=self.role,
            router_id=self.router_id,
            router_type=self.router_type,
            specification=self.specification,
            status=self.status)

def get_router_interfaces(ids=None,name_regex=None,opposite_interface_id=None,opposite_interface_owner_id=None,output_file=None,role=None,router_id=None,router_type=None,specification=None,status=None,opts=None):
    """
    This data source provides information about [router interfaces](https://www.alibabacloud.com/help/doc-detail/52412.htm)
    that connect VPCs together.

    > This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/router_interfaces.html.markdown.


    :param list ids: A list of router interface IDs.
    :param str name_regex: A regex string used to filter by router interface name.
    :param str opposite_interface_id: ID of the peer router interface.
    :param str opposite_interface_owner_id: Account ID of the owner of the peer router interface.
    :param str role: Role of the router interface. Valid values are `InitiatingSide` (connection initiator) and 
           `AcceptingSide` (connection receiver). The value of this parameter must be `InitiatingSide` if the `router_type` is set to `VBR`.
    :param str router_id: ID of the VRouter located in the local region.
    :param str router_type: Router type in the local region. Valid values are `VRouter` and `VBR` (physical connection).
    :param str specification: Specification of the link, such as `Small.1` (10Mb), `Middle.1` (100Mb), `Large.2` (2Gb), ...etc.
    :param str status: Expected status. Valid values are `Active`, `Inactive` and `Idle`.
    """
    __args__ = dict()


    __args__['ids'] = ids
    __args__['nameRegex'] = name_regex
    __args__['oppositeInterfaceId'] = opposite_interface_id
    __args__['oppositeInterfaceOwnerId'] = opposite_interface_owner_id
    __args__['outputFile'] = output_file
    __args__['role'] = role
    __args__['routerId'] = router_id
    __args__['routerType'] = router_type
    __args__['specification'] = specification
    __args__['status'] = status
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('alicloud:vpc/getRouterInterfaces:getRouterInterfaces', __args__, opts=opts).value

    return AwaitableGetRouterInterfacesResult(
        id=__ret__.get('id'),
        ids=__ret__.get('ids'),
        interfaces=__ret__.get('interfaces'),
        name_regex=__ret__.get('nameRegex'),
        names=__ret__.get('names'),
        opposite_interface_id=__ret__.get('oppositeInterfaceId'),
        opposite_interface_owner_id=__ret__.get('oppositeInterfaceOwnerId'),
        output_file=__ret__.get('outputFile'),
        role=__ret__.get('role'),
        router_id=__ret__.get('routerId'),
        router_type=__ret__.get('routerType'),
        specification=__ret__.get('specification'),
        status=__ret__.get('status'))
