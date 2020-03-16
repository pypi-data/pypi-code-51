# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class Topic(pulumi.CustomResource):
    compact_topic: pulumi.Output[bool]
    """
    Whether the topic is compactTopic or not. Compact topic must be a localTopic.
    """
    instance_id: pulumi.Output[str]
    """
    InstanceId of your Kafka resource, the topic will create in this instance.
    """
    local_topic: pulumi.Output[bool]
    """
    Whether the topic is localTopic or not.
    """
    partition_num: pulumi.Output[float]
    """
    The number of partitions of the topic. The number should between 1 and 48.
    """
    remark: pulumi.Output[str]
    """
    This attribute is a concise description of topic. The length cannot exceed 64.
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource.
    """
    topic: pulumi.Output[str]
    """
    Name of the topic. Two topics on a single instance cannot have the same name. The length cannot exceed 64 characters.
    """
    def __init__(__self__, resource_name, opts=None, compact_topic=None, instance_id=None, local_topic=None, partition_num=None, remark=None, tags=None, topic=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides an ALIKAFKA topic resource.

        > **NOTE:** Available in 1.56.0+

        > **NOTE:**  Only the following regions support create alikafka topic.
        [`cn-hangzhou`,`cn-beijing`,`cn-shenzhen`,`cn-shanghai`,`cn-qingdao`,`cn-hongkong`,`cn-huhehaote`,`cn-zhangjiakou`,`ap-southeast-1`,`ap-south-1`,`ap-southeast-5`]

        > This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/alikafka_topic.html.markdown.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] compact_topic: Whether the topic is compactTopic or not. Compact topic must be a localTopic.
        :param pulumi.Input[str] instance_id: InstanceId of your Kafka resource, the topic will create in this instance.
        :param pulumi.Input[bool] local_topic: Whether the topic is localTopic or not.
        :param pulumi.Input[float] partition_num: The number of partitions of the topic. The number should between 1 and 48.
        :param pulumi.Input[str] remark: This attribute is a concise description of topic. The length cannot exceed 64.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] topic: Name of the topic. Two topics on a single instance cannot have the same name. The length cannot exceed 64 characters.
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

            __props__['compact_topic'] = compact_topic
            if instance_id is None:
                raise TypeError("Missing required property 'instance_id'")
            __props__['instance_id'] = instance_id
            __props__['local_topic'] = local_topic
            __props__['partition_num'] = partition_num
            if remark is None:
                raise TypeError("Missing required property 'remark'")
            __props__['remark'] = remark
            __props__['tags'] = tags
            if topic is None:
                raise TypeError("Missing required property 'topic'")
            __props__['topic'] = topic
        super(Topic, __self__).__init__(
            'alicloud:alikafka/topic:Topic',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, compact_topic=None, instance_id=None, local_topic=None, partition_num=None, remark=None, tags=None, topic=None):
        """
        Get an existing Topic resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] compact_topic: Whether the topic is compactTopic or not. Compact topic must be a localTopic.
        :param pulumi.Input[str] instance_id: InstanceId of your Kafka resource, the topic will create in this instance.
        :param pulumi.Input[bool] local_topic: Whether the topic is localTopic or not.
        :param pulumi.Input[float] partition_num: The number of partitions of the topic. The number should between 1 and 48.
        :param pulumi.Input[str] remark: This attribute is a concise description of topic. The length cannot exceed 64.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] topic: Name of the topic. Two topics on a single instance cannot have the same name. The length cannot exceed 64 characters.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["compact_topic"] = compact_topic
        __props__["instance_id"] = instance_id
        __props__["local_topic"] = local_topic
        __props__["partition_num"] = partition_num
        __props__["remark"] = remark
        __props__["tags"] = tags
        __props__["topic"] = topic
        return Topic(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

