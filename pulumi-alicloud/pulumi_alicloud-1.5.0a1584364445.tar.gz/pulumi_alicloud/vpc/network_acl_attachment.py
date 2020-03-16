# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class NetworkAclAttachment(pulumi.CustomResource):
    network_acl_id: pulumi.Output[str]
    """
    The id of the network acl, the field can't be changed.
    """
    resources: pulumi.Output[list]
    """
    List of the resources associated with the network acl. The details see Block Resources.

      * `resourceId` (`str`) - The resource id that the network acl will associate with.
      * `resourceType` (`str`) - The resource id that the network acl will associate with. Only support `VSwitch` now.
    """
    def __init__(__self__, resource_name, opts=None, network_acl_id=None, resources=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a network acl attachment resource to associate network acls to vswitches.

        > **NOTE:** Available in 1.44.0+. Currently, the resource are only available in Hongkong(cn-hongkong), India(ap-south-1), and Indonesia(ap-southeast-1) regions.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/network_acl_attachment.html.markdown.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] network_acl_id: The id of the network acl, the field can't be changed.
        :param pulumi.Input[list] resources: List of the resources associated with the network acl. The details see Block Resources.

        The **resources** object supports the following:

          * `resourceId` (`pulumi.Input[str]`) - The resource id that the network acl will associate with.
          * `resourceType` (`pulumi.Input[str]`) - The resource id that the network acl will associate with. Only support `VSwitch` now.
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

            if network_acl_id is None:
                raise TypeError("Missing required property 'network_acl_id'")
            __props__['network_acl_id'] = network_acl_id
            if resources is None:
                raise TypeError("Missing required property 'resources'")
            __props__['resources'] = resources
        super(NetworkAclAttachment, __self__).__init__(
            'alicloud:vpc/networkAclAttachment:NetworkAclAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, network_acl_id=None, resources=None):
        """
        Get an existing NetworkAclAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] network_acl_id: The id of the network acl, the field can't be changed.
        :param pulumi.Input[list] resources: List of the resources associated with the network acl. The details see Block Resources.

        The **resources** object supports the following:

          * `resourceId` (`pulumi.Input[str]`) - The resource id that the network acl will associate with.
          * `resourceType` (`pulumi.Input[str]`) - The resource id that the network acl will associate with. Only support `VSwitch` now.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["network_acl_id"] = network_acl_id
        __props__["resources"] = resources
        return NetworkAclAttachment(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

