# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class LogTailAttachment(pulumi.CustomResource):
    logtail_config_name: pulumi.Output[str]
    """
    The Logtail configuration name, which is unique in the same project.
    """
    machine_group_name: pulumi.Output[str]
    """
    The machine group name, which is unique in the same project.
    """
    project: pulumi.Output[str]
    """
    The project name to the log store belongs.
    """
    def __init__(__self__, resource_name, opts=None, logtail_config_name=None, machine_group_name=None, project=None, __props__=None, __name__=None, __opts__=None):
        """
        The Logtail access service is a log collection agent provided by Log Service.
        You can use Logtail to collect logs from servers such as Alibaba Cloud Elastic
        Compute Service (ECS) instances in real time in the Log Service console. [Refer to details](https://www.alibabacloud.com/help/doc-detail/29058.htm)

        This resource amis to attach one logtail configure to a machine group.

        > **NOTE:** One logtail configure can be attached to multiple machine groups and one machine group can attach several logtail configures.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/logtail_attachment.html.markdown.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] logtail_config_name: The Logtail configuration name, which is unique in the same project.
        :param pulumi.Input[str] machine_group_name: The machine group name, which is unique in the same project.
        :param pulumi.Input[str] project: The project name to the log store belongs.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if logtail_config_name is None:
                raise TypeError("Missing required property 'logtail_config_name'")
            __props__['logtail_config_name'] = logtail_config_name
            if machine_group_name is None:
                raise TypeError("Missing required property 'machine_group_name'")
            __props__['machine_group_name'] = machine_group_name
            if project is None:
                raise TypeError("Missing required property 'project'")
            __props__['project'] = project
        super(LogTailAttachment, __self__).__init__(
            'alicloud:log/logTailAttachment:LogTailAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, logtail_config_name=None, machine_group_name=None, project=None):
        """
        Get an existing LogTailAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] logtail_config_name: The Logtail configuration name, which is unique in the same project.
        :param pulumi.Input[str] machine_group_name: The machine group name, which is unique in the same project.
        :param pulumi.Input[str] project: The project name to the log store belongs.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["logtail_config_name"] = logtail_config_name
        __props__["machine_group_name"] = machine_group_name
        __props__["project"] = project
        return LogTailAttachment(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

