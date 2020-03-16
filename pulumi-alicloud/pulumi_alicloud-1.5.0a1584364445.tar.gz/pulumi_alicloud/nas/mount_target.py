# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class MountTarget(pulumi.CustomResource):
    access_group_name: pulumi.Output[str]
    """
    Permission group name.
    """
    file_system_id: pulumi.Output[str]
    """
    File system ID.
    """
    status: pulumi.Output[str]
    """
    Whether the MountTarget is active. An inactive MountTarget is inusable. Valid values are Active(default) and Inactive.
    """
    vswitch_id: pulumi.Output[str]
    """
    VSwitch ID.
    """
    def __init__(__self__, resource_name, opts=None, access_group_name=None, file_system_id=None, status=None, vswitch_id=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a Nas Mount Target resource.

        > NOTE: Available in v1.34.0+.

        > NOTE: Currently this resource support create a mount point in a classic network only when current region is China mainland regions.

        > NOTE: You must grant NAS with specific RAM permissions when creating a classic mount targets,
        and it only can be achieved by creating a classic mount target mannually.
        See [Add a mount point](https://www.alibabacloud.com/help/doc-detail/60431.htm) and [Why do I need RAM permissions to create a mount point in a classic network](https://www.alibabacloud.com/help/faq-detail/42176.htm).

        > This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/nas_mount_target.html.markdown.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_group_name: Permission group name.
        :param pulumi.Input[str] file_system_id: File system ID.
        :param pulumi.Input[str] status: Whether the MountTarget is active. An inactive MountTarget is inusable. Valid values are Active(default) and Inactive.
        :param pulumi.Input[str] vswitch_id: VSwitch ID.
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

            if access_group_name is None:
                raise TypeError("Missing required property 'access_group_name'")
            __props__['access_group_name'] = access_group_name
            if file_system_id is None:
                raise TypeError("Missing required property 'file_system_id'")
            __props__['file_system_id'] = file_system_id
            __props__['status'] = status
            __props__['vswitch_id'] = vswitch_id
        super(MountTarget, __self__).__init__(
            'alicloud:nas/mountTarget:MountTarget',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, access_group_name=None, file_system_id=None, status=None, vswitch_id=None):
        """
        Get an existing MountTarget resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_group_name: Permission group name.
        :param pulumi.Input[str] file_system_id: File system ID.
        :param pulumi.Input[str] status: Whether the MountTarget is active. An inactive MountTarget is inusable. Valid values are Active(default) and Inactive.
        :param pulumi.Input[str] vswitch_id: VSwitch ID.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["access_group_name"] = access_group_name
        __props__["file_system_id"] = file_system_id
        __props__["status"] = status
        __props__["vswitch_id"] = vswitch_id
        return MountTarget(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

