# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetEndpointsResult:
    """
    A collection of values returned by getEndpoints.
    """
    def __init__(__self__, db_cluster_id=None, db_endpoint_id=None, endpoints=None, id=None):
        if db_cluster_id and not isinstance(db_cluster_id, str):
            raise TypeError("Expected argument 'db_cluster_id' to be a str")
        __self__.db_cluster_id = db_cluster_id
        if db_endpoint_id and not isinstance(db_endpoint_id, str):
            raise TypeError("Expected argument 'db_endpoint_id' to be a str")
        __self__.db_endpoint_id = db_endpoint_id
        """
        The endpoint ID.
        """
        if endpoints and not isinstance(endpoints, list):
            raise TypeError("Expected argument 'endpoints' to be a list")
        __self__.endpoints = endpoints
        """
        A list of PolarDB cluster endpoints. Each element contains the following attributes:
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
class AwaitableGetEndpointsResult(GetEndpointsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEndpointsResult(
            db_cluster_id=self.db_cluster_id,
            db_endpoint_id=self.db_endpoint_id,
            endpoints=self.endpoints,
            id=self.id)

def get_endpoints(db_cluster_id=None,db_endpoint_id=None,opts=None):
    """
    The `polardb.getEndpoints` data source provides a collection of PolarDB endpoints available in Alibaba Cloud account.
    Filters support regular expression for the cluster name, searches by clusterId, and other filters which are listed below.

    > **NOTE:** Available in v1.68.0+.

    > This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/polardb_endpoints.html.markdown.


    :param str db_cluster_id: PolarDB cluster ID. 
    :param str db_endpoint_id: endpoint of the cluster.
    """
    __args__ = dict()


    __args__['dbClusterId'] = db_cluster_id
    __args__['dbEndpointId'] = db_endpoint_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('alicloud:polardb/getEndpoints:getEndpoints', __args__, opts=opts).value

    return AwaitableGetEndpointsResult(
        db_cluster_id=__ret__.get('dbClusterId'),
        db_endpoint_id=__ret__.get('dbEndpointId'),
        endpoints=__ret__.get('endpoints'),
        id=__ret__.get('id'))
