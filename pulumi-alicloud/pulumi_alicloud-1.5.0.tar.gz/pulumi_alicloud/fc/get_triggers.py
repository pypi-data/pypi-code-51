# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetTriggersResult:
    """
    A collection of values returned by getTriggers.
    """
    def __init__(__self__, function_name=None, id=None, ids=None, name_regex=None, names=None, output_file=None, service_name=None, triggers=None):
        if function_name and not isinstance(function_name, str):
            raise TypeError("Expected argument 'function_name' to be a str")
        __self__.function_name = function_name
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
        A list of FC triggers ids.
        """
        if name_regex and not isinstance(name_regex, str):
            raise TypeError("Expected argument 'name_regex' to be a str")
        __self__.name_regex = name_regex
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        __self__.names = names
        """
        A list of FC triggers names.
        """
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        __self__.output_file = output_file
        if service_name and not isinstance(service_name, str):
            raise TypeError("Expected argument 'service_name' to be a str")
        __self__.service_name = service_name
        if triggers and not isinstance(triggers, list):
            raise TypeError("Expected argument 'triggers' to be a list")
        __self__.triggers = triggers
        """
        A list of FC triggers. Each element contains the following attributes:
        """
class AwaitableGetTriggersResult(GetTriggersResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTriggersResult(
            function_name=self.function_name,
            id=self.id,
            ids=self.ids,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file,
            service_name=self.service_name,
            triggers=self.triggers)

def get_triggers(function_name=None,ids=None,name_regex=None,output_file=None,service_name=None,opts=None):
    """
    This data source provides the Function Compute triggers of the current Alibaba Cloud user.

    > This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/fc_triggers.html.markdown.


    :param str function_name: FC function name.
    :param str name_regex: A regex string to filter results by FC trigger name.
           * `ids` (Optional, Available in 1.53.0+) - A list of FC triggers ids.
    :param str service_name: FC service name.
    """
    __args__ = dict()


    __args__['functionName'] = function_name
    __args__['ids'] = ids
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    __args__['serviceName'] = service_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('alicloud:fc/getTriggers:getTriggers', __args__, opts=opts).value

    return AwaitableGetTriggersResult(
        function_name=__ret__.get('functionName'),
        id=__ret__.get('id'),
        ids=__ret__.get('ids'),
        name_regex=__ret__.get('nameRegex'),
        names=__ret__.get('names'),
        output_file=__ret__.get('outputFile'),
        service_name=__ret__.get('serviceName'),
        triggers=__ret__.get('triggers'))
