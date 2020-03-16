# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class SslVpnServer(pulumi.CustomResource):
    cipher: pulumi.Output[str]
    """
    The encryption algorithm used by the SSL-VPN server. Valid value: AES-128-CBC (default)| AES-192-CBC | AES-256-CBC | none
    """
    client_ip_pool: pulumi.Output[str]
    """
    The CIDR block from which access addresses are allocated to the virtual network interface card of the client.
    """
    compress: pulumi.Output[bool]
    """
    Specify whether to compress the communication. Valid value: true (default) | false
    """
    connections: pulumi.Output[float]
    """
    The number of current connections.
    """
    internet_ip: pulumi.Output[str]
    """
    The internet IP of the SSL-VPN server.
    """
    local_subnet: pulumi.Output[str]
    """
    The CIDR block to be accessed by the client through the SSL-VPN connection. It supports to set multi CIDRs by comma join ways, like `10.0.1.0/24,10.0.2.0/24,10.0.3.0/24`.
    """
    max_connections: pulumi.Output[float]
    """
    The maximum number of connections.
    """
    name: pulumi.Output[str]
    """
    The name of the SSL-VPN server.
    """
    port: pulumi.Output[float]
    """
    The port used by the SSL-VPN server. The default value is 1194.The following ports cannot be used: [22, 2222, 22222, 9000, 9001, 9002, 7505, 80, 443, 53, 68, 123, 4510, 4560, 500, 4500].
    """
    protocol: pulumi.Output[str]
    """
    The protocol used by the SSL-VPN server. Valid value: UDP(default) |TCP
    """
    vpn_gateway_id: pulumi.Output[str]
    """
    The ID of the VPN gateway.
    """
    def __init__(__self__, resource_name, opts=None, cipher=None, client_ip_pool=None, compress=None, local_subnet=None, name=None, port=None, protocol=None, vpn_gateway_id=None, __props__=None, __name__=None, __opts__=None):
        """
        Create a SslVpnServer resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cipher: The encryption algorithm used by the SSL-VPN server. Valid value: AES-128-CBC (default)| AES-192-CBC | AES-256-CBC | none
        :param pulumi.Input[str] client_ip_pool: The CIDR block from which access addresses are allocated to the virtual network interface card of the client.
        :param pulumi.Input[bool] compress: Specify whether to compress the communication. Valid value: true (default) | false
        :param pulumi.Input[str] local_subnet: The CIDR block to be accessed by the client through the SSL-VPN connection. It supports to set multi CIDRs by comma join ways, like `10.0.1.0/24,10.0.2.0/24,10.0.3.0/24`.
        :param pulumi.Input[str] name: The name of the SSL-VPN server.
        :param pulumi.Input[float] port: The port used by the SSL-VPN server. The default value is 1194.The following ports cannot be used: [22, 2222, 22222, 9000, 9001, 9002, 7505, 80, 443, 53, 68, 123, 4510, 4560, 500, 4500].
        :param pulumi.Input[str] protocol: The protocol used by the SSL-VPN server. Valid value: UDP(default) |TCP
        :param pulumi.Input[str] vpn_gateway_id: The ID of the VPN gateway.
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

            __props__['cipher'] = cipher
            if client_ip_pool is None:
                raise TypeError("Missing required property 'client_ip_pool'")
            __props__['client_ip_pool'] = client_ip_pool
            __props__['compress'] = compress
            if local_subnet is None:
                raise TypeError("Missing required property 'local_subnet'")
            __props__['local_subnet'] = local_subnet
            __props__['name'] = name
            __props__['port'] = port
            __props__['protocol'] = protocol
            if vpn_gateway_id is None:
                raise TypeError("Missing required property 'vpn_gateway_id'")
            __props__['vpn_gateway_id'] = vpn_gateway_id
            __props__['connections'] = None
            __props__['internet_ip'] = None
            __props__['max_connections'] = None
        super(SslVpnServer, __self__).__init__(
            'alicloud:vpn/sslVpnServer:SslVpnServer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, cipher=None, client_ip_pool=None, compress=None, connections=None, internet_ip=None, local_subnet=None, max_connections=None, name=None, port=None, protocol=None, vpn_gateway_id=None):
        """
        Get an existing SslVpnServer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cipher: The encryption algorithm used by the SSL-VPN server. Valid value: AES-128-CBC (default)| AES-192-CBC | AES-256-CBC | none
        :param pulumi.Input[str] client_ip_pool: The CIDR block from which access addresses are allocated to the virtual network interface card of the client.
        :param pulumi.Input[bool] compress: Specify whether to compress the communication. Valid value: true (default) | false
        :param pulumi.Input[float] connections: The number of current connections.
        :param pulumi.Input[str] internet_ip: The internet IP of the SSL-VPN server.
        :param pulumi.Input[str] local_subnet: The CIDR block to be accessed by the client through the SSL-VPN connection. It supports to set multi CIDRs by comma join ways, like `10.0.1.0/24,10.0.2.0/24,10.0.3.0/24`.
        :param pulumi.Input[float] max_connections: The maximum number of connections.
        :param pulumi.Input[str] name: The name of the SSL-VPN server.
        :param pulumi.Input[float] port: The port used by the SSL-VPN server. The default value is 1194.The following ports cannot be used: [22, 2222, 22222, 9000, 9001, 9002, 7505, 80, 443, 53, 68, 123, 4510, 4560, 500, 4500].
        :param pulumi.Input[str] protocol: The protocol used by the SSL-VPN server. Valid value: UDP(default) |TCP
        :param pulumi.Input[str] vpn_gateway_id: The ID of the VPN gateway.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["cipher"] = cipher
        __props__["client_ip_pool"] = client_ip_pool
        __props__["compress"] = compress
        __props__["connections"] = connections
        __props__["internet_ip"] = internet_ip
        __props__["local_subnet"] = local_subnet
        __props__["max_connections"] = max_connections
        __props__["name"] = name
        __props__["port"] = port
        __props__["protocol"] = protocol
        __props__["vpn_gateway_id"] = vpn_gateway_id
        return SslVpnServer(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

