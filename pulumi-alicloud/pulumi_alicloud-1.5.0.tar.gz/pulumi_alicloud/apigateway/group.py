# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class Group(pulumi.CustomResource):
    description: pulumi.Output[str]
    """
    The description of the api gateway group. Defaults to null.
    """
    name: pulumi.Output[str]
    """
    The name of the api gateway group. Defaults to null.
    """
    sub_domain: pulumi.Output[str]
    """
    (Available in 1.69.0+)	Second-level domain name automatically assigned to the API group.
    """
    vpc_domain: pulumi.Output[str]
    """
    (Available in 1.69.0+)	Second-level VPC domain name automatically assigned to the API group.
    """
    def __init__(__self__, resource_name, opts=None, description=None, name=None, __props__=None, __name__=None, __opts__=None):
        """
        Create a Group resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the api gateway group. Defaults to null.
        :param pulumi.Input[str] name: The name of the api gateway group. Defaults to null.
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

            if description is None:
                raise TypeError("Missing required property 'description'")
            __props__['description'] = description
            __props__['name'] = name
            __props__['sub_domain'] = None
            __props__['vpc_domain'] = None
        super(Group, __self__).__init__(
            'alicloud:apigateway/group:Group',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, description=None, name=None, sub_domain=None, vpc_domain=None):
        """
        Get an existing Group resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the api gateway group. Defaults to null.
        :param pulumi.Input[str] name: The name of the api gateway group. Defaults to null.
        :param pulumi.Input[str] sub_domain: (Available in 1.69.0+)	Second-level domain name automatically assigned to the API group.
        :param pulumi.Input[str] vpc_domain: (Available in 1.69.0+)	Second-level VPC domain name automatically assigned to the API group.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["description"] = description
        __props__["name"] = name
        __props__["sub_domain"] = sub_domain
        __props__["vpc_domain"] = vpc_domain
        return Group(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

