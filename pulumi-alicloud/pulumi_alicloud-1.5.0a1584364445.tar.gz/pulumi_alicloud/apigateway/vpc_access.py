# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class VpcAccess(pulumi.CustomResource):
    instance_id: pulumi.Output[str]
    """
    ID of the instance in VPC (ECS/Server Load Balance).
    """
    name: pulumi.Output[str]
    """
    The name of the vpc authorization. 
    """
    port: pulumi.Output[float]
    """
    ID of the port corresponding to the instance.
    """
    vpc_id: pulumi.Output[str]
    """
    The vpc id of the vpc authorization. 
    """
    def __init__(__self__, resource_name, opts=None, instance_id=None, name=None, port=None, vpc_id=None, __props__=None, __name__=None, __opts__=None):
        """
        Create a VpcAccess resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] instance_id: ID of the instance in VPC (ECS/Server Load Balance).
        :param pulumi.Input[str] name: The name of the vpc authorization. 
        :param pulumi.Input[float] port: ID of the port corresponding to the instance.
        :param pulumi.Input[str] vpc_id: The vpc id of the vpc authorization. 
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

            if instance_id is None:
                raise TypeError("Missing required property 'instance_id'")
            __props__['instance_id'] = instance_id
            __props__['name'] = name
            if port is None:
                raise TypeError("Missing required property 'port'")
            __props__['port'] = port
            if vpc_id is None:
                raise TypeError("Missing required property 'vpc_id'")
            __props__['vpc_id'] = vpc_id
        super(VpcAccess, __self__).__init__(
            'alicloud:apigateway/vpcAccess:VpcAccess',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, instance_id=None, name=None, port=None, vpc_id=None):
        """
        Get an existing VpcAccess resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] instance_id: ID of the instance in VPC (ECS/Server Load Balance).
        :param pulumi.Input[str] name: The name of the vpc authorization. 
        :param pulumi.Input[float] port: ID of the port corresponding to the instance.
        :param pulumi.Input[str] vpc_id: The vpc id of the vpc authorization. 
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["instance_id"] = instance_id
        __props__["name"] = name
        __props__["port"] = port
        __props__["vpc_id"] = vpc_id
        return VpcAccess(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

