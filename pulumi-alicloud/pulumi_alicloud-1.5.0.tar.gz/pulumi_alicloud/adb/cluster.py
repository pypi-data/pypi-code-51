# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class Cluster(pulumi.CustomResource):
    auto_renew_period: pulumi.Output[float]
    """
    Auto-renewal period of an cluster, in the unit of the month. It is valid when pay_type is `PrePaid`. Valid value:1, 2, 3, 6, 12, 24, 36, Default to 1.
    """
    db_cluster_category: pulumi.Output[str]
    """
    Cluster category. Value options: `Basic`, `Cluster`.
    """
    db_cluster_version: pulumi.Output[str]
    """
    Cluster version. Value options: `3.0`, Default to `3.0`.
    """
    db_node_class: pulumi.Output[str]
    """
    The db_node_class of cluster node.
    """
    db_node_count: pulumi.Output[float]
    """
    The db_node_count of cluster node.
    """
    db_node_storage: pulumi.Output[float]
    """
    The db_node_storage of cluster node.
    """
    description: pulumi.Output[str]
    """
    The description of cluster.
    """
    maintain_time: pulumi.Output[str]
    """
    Maintainable time period format of the instance: HH:MMZ-HH:MMZ (UTC time)
    """
    pay_type: pulumi.Output[str]
    """
    Valid values are `PrePaid`, `PostPaid`, Default to `PostPaid`. Currently, the resource can not supports change pay type.
    """
    period: pulumi.Output[float]
    """
    The duration that you will buy DB cluster (in month). It is valid when pay_type is `PrePaid`. Valid values: [1~9], 12, 24, 36. Default to 1.
    """
    renewal_status: pulumi.Output[str]
    """
    Valid values are `AutoRenewal`, `Normal`, `NotRenewal`, Default to `NotRenewal`.
    """
    security_ips: pulumi.Output[list]
    """
    List of IP addresses allowed to access all databases of an cluster. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource.
    - Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
    - Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
    """
    vswitch_id: pulumi.Output[str]
    """
    The virtual switch ID to launch DB instances in one VPC.
    """
    zone_id: pulumi.Output[str]
    """
    The Zone to launch the DB cluster.
    """
    def __init__(__self__, resource_name, opts=None, auto_renew_period=None, db_cluster_category=None, db_cluster_version=None, db_node_class=None, db_node_count=None, db_node_storage=None, description=None, maintain_time=None, pay_type=None, period=None, renewal_status=None, security_ips=None, tags=None, vswitch_id=None, zone_id=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a ADB cluster resource. A ADB cluster is an isolated database
        environment in the cloud. A ADB cluster can contain multiple user-created
        databases.

        > **NOTE:** Available in v1.71.0+.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/adb_cluster.html.markdown.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] auto_renew_period: Auto-renewal period of an cluster, in the unit of the month. It is valid when pay_type is `PrePaid`. Valid value:1, 2, 3, 6, 12, 24, 36, Default to 1.
        :param pulumi.Input[str] db_cluster_category: Cluster category. Value options: `Basic`, `Cluster`.
        :param pulumi.Input[str] db_cluster_version: Cluster version. Value options: `3.0`, Default to `3.0`.
        :param pulumi.Input[str] db_node_class: The db_node_class of cluster node.
        :param pulumi.Input[float] db_node_count: The db_node_count of cluster node.
        :param pulumi.Input[float] db_node_storage: The db_node_storage of cluster node.
        :param pulumi.Input[str] description: The description of cluster.
        :param pulumi.Input[str] maintain_time: Maintainable time period format of the instance: HH:MMZ-HH:MMZ (UTC time)
        :param pulumi.Input[str] pay_type: Valid values are `PrePaid`, `PostPaid`, Default to `PostPaid`. Currently, the resource can not supports change pay type.
        :param pulumi.Input[float] period: The duration that you will buy DB cluster (in month). It is valid when pay_type is `PrePaid`. Valid values: [1~9], 12, 24, 36. Default to 1.
        :param pulumi.Input[str] renewal_status: Valid values are `AutoRenewal`, `Normal`, `NotRenewal`, Default to `NotRenewal`.
        :param pulumi.Input[list] security_ips: List of IP addresses allowed to access all databases of an cluster. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
               - Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
               - Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
        :param pulumi.Input[str] vswitch_id: The virtual switch ID to launch DB instances in one VPC.
        :param pulumi.Input[str] zone_id: The Zone to launch the DB cluster.
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

            __props__['auto_renew_period'] = auto_renew_period
            if db_cluster_category is None:
                raise TypeError("Missing required property 'db_cluster_category'")
            __props__['db_cluster_category'] = db_cluster_category
            __props__['db_cluster_version'] = db_cluster_version
            if db_node_class is None:
                raise TypeError("Missing required property 'db_node_class'")
            __props__['db_node_class'] = db_node_class
            if db_node_count is None:
                raise TypeError("Missing required property 'db_node_count'")
            __props__['db_node_count'] = db_node_count
            if db_node_storage is None:
                raise TypeError("Missing required property 'db_node_storage'")
            __props__['db_node_storage'] = db_node_storage
            __props__['description'] = description
            __props__['maintain_time'] = maintain_time
            __props__['pay_type'] = pay_type
            __props__['period'] = period
            __props__['renewal_status'] = renewal_status
            __props__['security_ips'] = security_ips
            __props__['tags'] = tags
            __props__['vswitch_id'] = vswitch_id
            __props__['zone_id'] = zone_id
        super(Cluster, __self__).__init__(
            'alicloud:adb/cluster:Cluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, auto_renew_period=None, db_cluster_category=None, db_cluster_version=None, db_node_class=None, db_node_count=None, db_node_storage=None, description=None, maintain_time=None, pay_type=None, period=None, renewal_status=None, security_ips=None, tags=None, vswitch_id=None, zone_id=None):
        """
        Get an existing Cluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] auto_renew_period: Auto-renewal period of an cluster, in the unit of the month. It is valid when pay_type is `PrePaid`. Valid value:1, 2, 3, 6, 12, 24, 36, Default to 1.
        :param pulumi.Input[str] db_cluster_category: Cluster category. Value options: `Basic`, `Cluster`.
        :param pulumi.Input[str] db_cluster_version: Cluster version. Value options: `3.0`, Default to `3.0`.
        :param pulumi.Input[str] db_node_class: The db_node_class of cluster node.
        :param pulumi.Input[float] db_node_count: The db_node_count of cluster node.
        :param pulumi.Input[float] db_node_storage: The db_node_storage of cluster node.
        :param pulumi.Input[str] description: The description of cluster.
        :param pulumi.Input[str] maintain_time: Maintainable time period format of the instance: HH:MMZ-HH:MMZ (UTC time)
        :param pulumi.Input[str] pay_type: Valid values are `PrePaid`, `PostPaid`, Default to `PostPaid`. Currently, the resource can not supports change pay type.
        :param pulumi.Input[float] period: The duration that you will buy DB cluster (in month). It is valid when pay_type is `PrePaid`. Valid values: [1~9], 12, 24, 36. Default to 1.
        :param pulumi.Input[str] renewal_status: Valid values are `AutoRenewal`, `Normal`, `NotRenewal`, Default to `NotRenewal`.
        :param pulumi.Input[list] security_ips: List of IP addresses allowed to access all databases of an cluster. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
               - Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
               - Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
        :param pulumi.Input[str] vswitch_id: The virtual switch ID to launch DB instances in one VPC.
        :param pulumi.Input[str] zone_id: The Zone to launch the DB cluster.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["auto_renew_period"] = auto_renew_period
        __props__["db_cluster_category"] = db_cluster_category
        __props__["db_cluster_version"] = db_cluster_version
        __props__["db_node_class"] = db_node_class
        __props__["db_node_count"] = db_node_count
        __props__["db_node_storage"] = db_node_storage
        __props__["description"] = description
        __props__["maintain_time"] = maintain_time
        __props__["pay_type"] = pay_type
        __props__["period"] = period
        __props__["renewal_status"] = renewal_status
        __props__["security_ips"] = security_ips
        __props__["tags"] = tags
        __props__["vswitch_id"] = vswitch_id
        __props__["zone_id"] = zone_id
        return Cluster(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

