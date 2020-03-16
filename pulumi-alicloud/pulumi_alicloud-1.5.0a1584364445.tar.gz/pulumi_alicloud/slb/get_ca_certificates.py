# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetCaCertificatesResult:
    """
    A collection of values returned by getCaCertificates.
    """
    def __init__(__self__, certificates=None, id=None, ids=None, name_regex=None, names=None, output_file=None, resource_group_id=None, tags=None):
        if certificates and not isinstance(certificates, list):
            raise TypeError("Expected argument 'certificates' to be a list")
        __self__.certificates = certificates
        """
        A list of SLB ca certificates. Each element contains the following attributes:
        """
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
        A list of SLB ca certificates IDs.
        """
        if name_regex and not isinstance(name_regex, str):
            raise TypeError("Expected argument 'name_regex' to be a str")
        __self__.name_regex = name_regex
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        __self__.names = names
        """
        A list of SLB ca certificates names.
        """
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        __self__.output_file = output_file
        if resource_group_id and not isinstance(resource_group_id, str):
            raise TypeError("Expected argument 'resource_group_id' to be a str")
        __self__.resource_group_id = resource_group_id
        """
        The resource group Id of CA certificate.
        """
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        __self__.tags = tags
        """
        (Available in v1.66.0+) A mapping of tags to assign to the resource.
        """
class AwaitableGetCaCertificatesResult(GetCaCertificatesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCaCertificatesResult(
            certificates=self.certificates,
            id=self.id,
            ids=self.ids,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file,
            resource_group_id=self.resource_group_id,
            tags=self.tags)

def get_ca_certificates(ids=None,name_regex=None,output_file=None,resource_group_id=None,tags=None,opts=None):
    """
    This data source provides the CA certificate list.

    > This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/slb_ca_certificates.html.markdown.


    :param list ids: A list of ca certificates IDs to filter results.
    :param str name_regex: A regex string to filter results by ca certificate name.
    :param str resource_group_id: The Id of resource group which ca certificates belongs.
    :param dict tags: A mapping of tags to assign to the resource.
    """
    __args__ = dict()


    __args__['ids'] = ids
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    __args__['resourceGroupId'] = resource_group_id
    __args__['tags'] = tags
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('alicloud:slb/getCaCertificates:getCaCertificates', __args__, opts=opts).value

    return AwaitableGetCaCertificatesResult(
        certificates=__ret__.get('certificates'),
        id=__ret__.get('id'),
        ids=__ret__.get('ids'),
        name_regex=__ret__.get('nameRegex'),
        names=__ret__.get('names'),
        output_file=__ret__.get('outputFile'),
        resource_group_id=__ret__.get('resourceGroupId'),
        tags=__ret__.get('tags'))
