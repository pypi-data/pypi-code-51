# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class User(pulumi.CustomResource):
    comments: pulumi.Output[str]
    """
    Comment of the RAM user. This parameter can have a string of 1 to 128 characters.
    """
    display_name: pulumi.Output[str]
    """
    Name of the RAM user which for display. This name can have a string of 1 to 128 characters or Chinese characters, must contain only alphanumeric characters or Chinese characters or hyphens, such as "-",".", and must not end with a hyphen.
    """
    email: pulumi.Output[str]
    """
    Email of the RAM user.
    """
    force: pulumi.Output[bool]
    """
    This parameter is used for resource destroy. Default value is `false`.
    """
    mobile: pulumi.Output[str]
    """
    Phone number of the RAM user. This number must contain an international area code prefix, just look like this: 86-18600008888.
    """
    name: pulumi.Output[str]
    """
    Name of the RAM user. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as "-",".","_", and must not begin with a hyphen.
    """
    def __init__(__self__, resource_name, opts=None, comments=None, display_name=None, email=None, force=None, mobile=None, name=None, __props__=None, __name__=None, __opts__=None):
        """
        Create a User resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] comments: Comment of the RAM user. This parameter can have a string of 1 to 128 characters.
        :param pulumi.Input[str] display_name: Name of the RAM user which for display. This name can have a string of 1 to 128 characters or Chinese characters, must contain only alphanumeric characters or Chinese characters or hyphens, such as "-",".", and must not end with a hyphen.
        :param pulumi.Input[str] email: Email of the RAM user.
        :param pulumi.Input[bool] force: This parameter is used for resource destroy. Default value is `false`.
        :param pulumi.Input[str] mobile: Phone number of the RAM user. This number must contain an international area code prefix, just look like this: 86-18600008888.
        :param pulumi.Input[str] name: Name of the RAM user. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as "-",".","_", and must not begin with a hyphen.
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

            __props__['comments'] = comments
            __props__['display_name'] = display_name
            __props__['email'] = email
            __props__['force'] = force
            __props__['mobile'] = mobile
            __props__['name'] = name
        super(User, __self__).__init__(
            'alicloud:ram/user:User',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, comments=None, display_name=None, email=None, force=None, mobile=None, name=None):
        """
        Get an existing User resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] comments: Comment of the RAM user. This parameter can have a string of 1 to 128 characters.
        :param pulumi.Input[str] display_name: Name of the RAM user which for display. This name can have a string of 1 to 128 characters or Chinese characters, must contain only alphanumeric characters or Chinese characters or hyphens, such as "-",".", and must not end with a hyphen.
        :param pulumi.Input[str] email: Email of the RAM user.
        :param pulumi.Input[bool] force: This parameter is used for resource destroy. Default value is `false`.
        :param pulumi.Input[str] mobile: Phone number of the RAM user. This number must contain an international area code prefix, just look like this: 86-18600008888.
        :param pulumi.Input[str] name: Name of the RAM user. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as "-",".","_", and must not begin with a hyphen.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["comments"] = comments
        __props__["display_name"] = display_name
        __props__["email"] = email
        __props__["force"] = force
        __props__["mobile"] = mobile
        __props__["name"] = name
        return User(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

