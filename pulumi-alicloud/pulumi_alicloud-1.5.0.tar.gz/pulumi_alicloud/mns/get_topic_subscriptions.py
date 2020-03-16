# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetTopicSubscriptionsResult:
    """
    A collection of values returned by getTopicSubscriptions.
    """
    def __init__(__self__, id=None, name_prefix=None, names=None, output_file=None, subscriptions=None, topic_name=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
        if name_prefix and not isinstance(name_prefix, str):
            raise TypeError("Expected argument 'name_prefix' to be a str")
        __self__.name_prefix = name_prefix
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        __self__.names = names
        """
        A list of subscription names.
        """
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        __self__.output_file = output_file
        if subscriptions and not isinstance(subscriptions, list):
            raise TypeError("Expected argument 'subscriptions' to be a list")
        __self__.subscriptions = subscriptions
        """
        A list of subscriptions. Each element contains the following attributes:
        """
        if topic_name and not isinstance(topic_name, str):
            raise TypeError("Expected argument 'topic_name' to be a str")
        __self__.topic_name = topic_name
class AwaitableGetTopicSubscriptionsResult(GetTopicSubscriptionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTopicSubscriptionsResult(
            id=self.id,
            name_prefix=self.name_prefix,
            names=self.names,
            output_file=self.output_file,
            subscriptions=self.subscriptions,
            topic_name=self.topic_name)

def get_topic_subscriptions(name_prefix=None,output_file=None,topic_name=None,opts=None):
    """
    This data source provides a list of MNS topic subscriptions in an Alibaba Cloud account according to the specified parameters.

    > This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/mns_topic_subscriptions.html.markdown.


    :param str name_prefix: A string to filter resulting subscriptions of the topic by their name prefixs.
    :param str topic_name: Two topics on a single account in the same region cannot have the same name. A topic name must start with an English letter or a digit, and can contain English letters, digits, and hyphens, with the length not exceeding 256 characters.
    """
    __args__ = dict()


    __args__['namePrefix'] = name_prefix
    __args__['outputFile'] = output_file
    __args__['topicName'] = topic_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('alicloud:mns/getTopicSubscriptions:getTopicSubscriptions', __args__, opts=opts).value

    return AwaitableGetTopicSubscriptionsResult(
        id=__ret__.get('id'),
        name_prefix=__ret__.get('namePrefix'),
        names=__ret__.get('names'),
        output_file=__ret__.get('outputFile'),
        subscriptions=__ret__.get('subscriptions'),
        topic_name=__ret__.get('topicName'))
