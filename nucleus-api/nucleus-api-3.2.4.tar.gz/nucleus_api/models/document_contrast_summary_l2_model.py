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


class DocumentContrastSummaryL2Model(object):
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
        'sentences': 'list[str]',
        'sourceid': 'str'
    }

    attribute_map = {
        'sentences': 'sentences',
        'sourceid': 'sourceid'
    }

    def __init__(self, sentences=None, sourceid=None):  # noqa: E501
        """DocumentContrastSummaryL2Model - a model defined in Swagger"""  # noqa: E501

        self._sentences = None
        self._sourceid = None
        self.discriminator = None

        if sentences is not None:
            self.sentences = sentences
        if sourceid is not None:
            self.sourceid = sourceid

    @property
    def sentences(self):
        """Gets the sentences of this DocumentContrastSummaryL2Model.  # noqa: E501


        :return: The sentences of this DocumentContrastSummaryL2Model.  # noqa: E501
        :rtype: list[str]
        """
        return self._sentences

    @sentences.setter
    def sentences(self, sentences):
        """Sets the sentences of this DocumentContrastSummaryL2Model.


        :param sentences: The sentences of this DocumentContrastSummaryL2Model.  # noqa: E501
        :type: list[str]
        """

        self._sentences = sentences

    @property
    def sourceid(self):
        """Gets the sourceid of this DocumentContrastSummaryL2Model.  # noqa: E501

        The ID of the document the sentence comes from  # noqa: E501

        :return: The sourceid of this DocumentContrastSummaryL2Model.  # noqa: E501
        :rtype: str
        """
        return self._sourceid

    @sourceid.setter
    def sourceid(self, sourceid):
        """Sets the sourceid of this DocumentContrastSummaryL2Model.

        The ID of the document the sentence comes from  # noqa: E501

        :param sourceid: The sourceid of this DocumentContrastSummaryL2Model.  # noqa: E501
        :type: str
        """

        self._sourceid = sourceid

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
        if issubclass(DocumentContrastSummaryL2Model, dict):
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
        if not isinstance(other, DocumentContrastSummaryL2Model):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
