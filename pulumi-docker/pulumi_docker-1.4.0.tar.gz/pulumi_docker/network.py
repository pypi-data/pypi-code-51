# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class Network(pulumi.CustomResource):
    attachable: pulumi.Output[bool]
    """
    Enable manual container attachment to the network.
    Defaults to `false`.
    """
    check_duplicate: pulumi.Output[bool]
    """
    Requests daemon to check for networks
    with same name.
    """
    driver: pulumi.Output[str]
    """
    Name of the network driver to use. Defaults to
    `bridge` driver.
    """
    ingress: pulumi.Output[bool]
    """
    Create swarm routing-mesh network.
    Defaults to `false`.
    """
    internal: pulumi.Output[bool]
    """
    Restrict external access to the network.
    Defaults to `false`.
    """
    ipam_configs: pulumi.Output[list]
    """
    See IPAM config below for
    details.

      * `auxAddress` (`dict`)
      * `gateway` (`str`)
      * `ipRange` (`str`)
      * `subnet` (`str`)
    """
    ipam_driver: pulumi.Output[str]
    """
    Driver used by the custom IP scheme of the
    network.
    """
    ipv6: pulumi.Output[bool]
    """
    Enable IPv6 networking.
    Defaults to `false`.
    """
    labels: pulumi.Output[list]
    """
    See Labels below for details.

      * `label` (`str`) - Name of the label
        * `value` (Required, string) Value of the label
      * `value` (`str`)
    """
    name: pulumi.Output[str]
    """
    The name of the Docker network.
    """
    options: pulumi.Output[dict]
    """
    Network specific options to be used by
    the drivers.
    """
    scope: pulumi.Output[str]
    def __init__(__self__, resource_name, opts=None, attachable=None, check_duplicate=None, driver=None, ingress=None, internal=None, ipam_configs=None, ipam_driver=None, ipv6=None, labels=None, name=None, options=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a Docker Network. This can be used alongside
        [docker\_container](https://www.terraform.io/docs/providers/docker/r/container.html)
        to create virtual networks within the docker environment.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-docker/blob/master/website/docs/r/network.html.markdown.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] attachable: Enable manual container attachment to the network.
               Defaults to `false`.
        :param pulumi.Input[bool] check_duplicate: Requests daemon to check for networks
               with same name.
        :param pulumi.Input[str] driver: Name of the network driver to use. Defaults to
               `bridge` driver.
        :param pulumi.Input[bool] ingress: Create swarm routing-mesh network.
               Defaults to `false`.
        :param pulumi.Input[bool] internal: Restrict external access to the network.
               Defaults to `false`.
        :param pulumi.Input[list] ipam_configs: See IPAM config below for
               details.
        :param pulumi.Input[str] ipam_driver: Driver used by the custom IP scheme of the
               network.
        :param pulumi.Input[bool] ipv6: Enable IPv6 networking.
               Defaults to `false`.
        :param pulumi.Input[list] labels: See Labels below for details.
        :param pulumi.Input[str] name: The name of the Docker network.
        :param pulumi.Input[dict] options: Network specific options to be used by
               the drivers.

        The **ipam_configs** object supports the following:

          * `auxAddress` (`pulumi.Input[dict]`)
          * `gateway` (`pulumi.Input[str]`)
          * `ipRange` (`pulumi.Input[str]`)
          * `subnet` (`pulumi.Input[str]`)

        The **labels** object supports the following:

          * `label` (`pulumi.Input[str]`) - Name of the label
            * `value` (Required, string) Value of the label
          * `value` (`pulumi.Input[str]`)
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

            __props__['attachable'] = attachable
            __props__['check_duplicate'] = check_duplicate
            __props__['driver'] = driver
            __props__['ingress'] = ingress
            __props__['internal'] = internal
            __props__['ipam_configs'] = ipam_configs
            __props__['ipam_driver'] = ipam_driver
            __props__['ipv6'] = ipv6
            __props__['labels'] = labels
            __props__['name'] = name
            __props__['options'] = options
            __props__['scope'] = None
        super(Network, __self__).__init__(
            'docker:index/network:Network',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, attachable=None, check_duplicate=None, driver=None, ingress=None, internal=None, ipam_configs=None, ipam_driver=None, ipv6=None, labels=None, name=None, options=None, scope=None):
        """
        Get an existing Network resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] attachable: Enable manual container attachment to the network.
               Defaults to `false`.
        :param pulumi.Input[bool] check_duplicate: Requests daemon to check for networks
               with same name.
        :param pulumi.Input[str] driver: Name of the network driver to use. Defaults to
               `bridge` driver.
        :param pulumi.Input[bool] ingress: Create swarm routing-mesh network.
               Defaults to `false`.
        :param pulumi.Input[bool] internal: Restrict external access to the network.
               Defaults to `false`.
        :param pulumi.Input[list] ipam_configs: See IPAM config below for
               details.
        :param pulumi.Input[str] ipam_driver: Driver used by the custom IP scheme of the
               network.
        :param pulumi.Input[bool] ipv6: Enable IPv6 networking.
               Defaults to `false`.
        :param pulumi.Input[list] labels: See Labels below for details.
        :param pulumi.Input[str] name: The name of the Docker network.
        :param pulumi.Input[dict] options: Network specific options to be used by
               the drivers.

        The **ipam_configs** object supports the following:

          * `auxAddress` (`pulumi.Input[dict]`)
          * `gateway` (`pulumi.Input[str]`)
          * `ipRange` (`pulumi.Input[str]`)
          * `subnet` (`pulumi.Input[str]`)

        The **labels** object supports the following:

          * `label` (`pulumi.Input[str]`) - Name of the label
            * `value` (Required, string) Value of the label
          * `value` (`pulumi.Input[str]`)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["attachable"] = attachable
        __props__["check_duplicate"] = check_duplicate
        __props__["driver"] = driver
        __props__["ingress"] = ingress
        __props__["internal"] = internal
        __props__["ipam_configs"] = ipam_configs
        __props__["ipam_driver"] = ipam_driver
        __props__["ipv6"] = ipv6
        __props__["labels"] = labels
        __props__["name"] = name
        __props__["options"] = options
        __props__["scope"] = scope
        return Network(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

