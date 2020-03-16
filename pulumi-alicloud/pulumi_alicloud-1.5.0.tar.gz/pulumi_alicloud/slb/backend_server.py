# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class BackendServer(pulumi.CustomResource):
    backend_servers: pulumi.Output[list]
    """
    A list of instances to added backend server in the SLB. It contains three sub-fields as `Block server` follows.

      * `serverId` (`str`)
      * `type` (`str`)
      * `weight` (`float`)
    """
    delete_protection_validation: pulumi.Output[bool]
    """
    Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.
    """
    load_balancer_id: pulumi.Output[str]
    """
    ID of the load balancer.
    """
    def __init__(__self__, resource_name, opts=None, backend_servers=None, delete_protection_validation=None, load_balancer_id=None, __props__=None, __name__=None, __opts__=None):
        """
        Add a group of backend servers (ECS or ENI instance) to the Server Load Balancer or remove them from it.

        > **NOTE:** Available in 1.53.0+

        ## Block servers

        The servers mapping supports the following:

        * `server_id` - (Required) A list backend server ID (ECS instance ID).
        * `weight` - (Optional) Weight of the backend server. Valid value range: [0-100]. 
        * `type` - (Optional) Type of the backend server. Valid value ecs, eni. Default to eni.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/slb_backend_server.html.markdown.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] backend_servers: A list of instances to added backend server in the SLB. It contains three sub-fields as `Block server` follows.
        :param pulumi.Input[bool] delete_protection_validation: Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.
        :param pulumi.Input[str] load_balancer_id: ID of the load balancer.

        The **backend_servers** object supports the following:

          * `serverId` (`pulumi.Input[str]`)
          * `type` (`pulumi.Input[str]`)
          * `weight` (`pulumi.Input[float]`)
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

            __props__['backend_servers'] = backend_servers
            __props__['delete_protection_validation'] = delete_protection_validation
            if load_balancer_id is None:
                raise TypeError("Missing required property 'load_balancer_id'")
            __props__['load_balancer_id'] = load_balancer_id
        super(BackendServer, __self__).__init__(
            'alicloud:slb/backendServer:BackendServer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, backend_servers=None, delete_protection_validation=None, load_balancer_id=None):
        """
        Get an existing BackendServer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] backend_servers: A list of instances to added backend server in the SLB. It contains three sub-fields as `Block server` follows.
        :param pulumi.Input[bool] delete_protection_validation: Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.
        :param pulumi.Input[str] load_balancer_id: ID of the load balancer.

        The **backend_servers** object supports the following:

          * `serverId` (`pulumi.Input[str]`)
          * `type` (`pulumi.Input[str]`)
          * `weight` (`pulumi.Input[float]`)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["backend_servers"] = backend_servers
        __props__["delete_protection_validation"] = delete_protection_validation
        __props__["load_balancer_id"] = load_balancer_id
        return BackendServer(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

