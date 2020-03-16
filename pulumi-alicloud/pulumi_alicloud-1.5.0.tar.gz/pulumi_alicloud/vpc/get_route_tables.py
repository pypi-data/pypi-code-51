# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetRouteTablesResult:
    """
    A collection of values returned by getRouteTables.
    """
    def __init__(__self__, id=None, ids=None, name_regex=None, names=None, output_file=None, resource_group_id=None, tables=None, tags=None, vpc_id=None):
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
        (Optional) A list of Route Tables IDs.
        """
        if name_regex and not isinstance(name_regex, str):
            raise TypeError("Expected argument 'name_regex' to be a str")
        __self__.name_regex = name_regex
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        __self__.names = names
        """
        A list of Route Tables names.
        """
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        __self__.output_file = output_file
        if resource_group_id and not isinstance(resource_group_id, str):
            raise TypeError("Expected argument 'resource_group_id' to be a str")
        __self__.resource_group_id = resource_group_id
        """
        The Id of resource group which route tables belongs.
        """
        if tables and not isinstance(tables, list):
            raise TypeError("Expected argument 'tables' to be a list")
        __self__.tables = tables
        """
        A list of Route Tables. Each element contains the following attributes:
        """
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        __self__.tags = tags
        if vpc_id and not isinstance(vpc_id, str):
            raise TypeError("Expected argument 'vpc_id' to be a str")
        __self__.vpc_id = vpc_id
class AwaitableGetRouteTablesResult(GetRouteTablesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRouteTablesResult(
            id=self.id,
            ids=self.ids,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file,
            resource_group_id=self.resource_group_id,
            tables=self.tables,
            tags=self.tags,
            vpc_id=self.vpc_id)

def get_route_tables(ids=None,name_regex=None,output_file=None,resource_group_id=None,tags=None,vpc_id=None,opts=None):
    """
    This data source provides a list of Route Tables owned by an Alibaba Cloud account.

    > **NOTE:** Available in 1.36.0+.

    > This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/route_tables.html.markdown.


    :param list ids: A list of Route Tables IDs.
    :param str name_regex: A regex string to filter route tables by name.
    :param str resource_group_id: The Id of resource group which route tables belongs.
    :param dict tags: A mapping of tags to assign to the resource.
    :param str vpc_id: Vpc id of the route table.
    """
    __args__ = dict()


    __args__['ids'] = ids
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    __args__['resourceGroupId'] = resource_group_id
    __args__['tags'] = tags
    __args__['vpcId'] = vpc_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('alicloud:vpc/getRouteTables:getRouteTables', __args__, opts=opts).value

    return AwaitableGetRouteTablesResult(
        id=__ret__.get('id'),
        ids=__ret__.get('ids'),
        name_regex=__ret__.get('nameRegex'),
        names=__ret__.get('names'),
        output_file=__ret__.get('outputFile'),
        resource_group_id=__ret__.get('resourceGroupId'),
        tables=__ret__.get('tables'),
        tags=__ret__.get('tags'),
        vpc_id=__ret__.get('vpcId'))
