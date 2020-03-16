# coding: utf-8

"""
    Nucleus API

    Nucleus text analytics APIs from SumUp Analytics. Example and documentation: https://www.sumup.ai/apis/#nucleus-documentation  # noqa: E501

    OpenAPI spec version: v3.2.4
    Contact: info@sumup.ai
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from nucleus_api.models.topic_transfer_l2_resp_model import TopicTransferL2RespModel  # noqa: F401,E501


class TopicTransferL1RespModel(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'doc_ids_t1': 'list[str]',
        'topics': 'list[TopicTransferL2RespModel]'
    }

    attribute_map = {
        'doc_ids_t1': 'doc_ids_t1',
        'topics': 'topics'
    }

    def __init__(self, doc_ids_t1=None, topics=None):  # noqa: E501
        """TopicTransferL1RespModel - a model defined in Swagger"""  # noqa: E501

        self._doc_ids_t1 = None
        self._topics = None
        self.discriminator = None

        if doc_ids_t1 is not None:
            self.doc_ids_t1 = doc_ids_t1
        if topics is not None:
            self.topics = topics

    @property
    def doc_ids_t1(self):
        """Gets the doc_ids_t1 of this TopicTransferL1RespModel.  # noqa: E501


        :return: The doc_ids_t1 of this TopicTransferL1RespModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._doc_ids_t1

    @doc_ids_t1.setter
    def doc_ids_t1(self, doc_ids_t1):
        """Sets the doc_ids_t1 of this TopicTransferL1RespModel.


        :param doc_ids_t1: The doc_ids_t1 of this TopicTransferL1RespModel.  # noqa: E501
        :type: list[str]
        """

        self._doc_ids_t1 = doc_ids_t1

    @property
    def topics(self):
        """Gets the topics of this TopicTransferL1RespModel.  # noqa: E501


        :return: The topics of this TopicTransferL1RespModel.  # noqa: E501
        :rtype: list[TopicTransferL2RespModel]
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        """Sets the topics of this TopicTransferL1RespModel.


        :param topics: The topics of this TopicTransferL1RespModel.  # noqa: E501
        :type: list[TopicTransferL2RespModel]
        """

        self._topics = topics

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(TopicTransferL1RespModel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TopicTransferL1RespModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
