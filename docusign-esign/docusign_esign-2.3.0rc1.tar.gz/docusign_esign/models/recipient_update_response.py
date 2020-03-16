# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class RecipientUpdateResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, error_details=None, recipient_id=None, tabs=None):
        """
        RecipientUpdateResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'error_details': 'ErrorDetails',
            'recipient_id': 'str',
            'tabs': 'Tabs'
        }

        self.attribute_map = {
            'error_details': 'errorDetails',
            'recipient_id': 'recipientId',
            'tabs': 'tabs'
        }

        self._error_details = error_details
        self._recipient_id = recipient_id
        self._tabs = tabs

    @property
    def error_details(self):
        """
        Gets the error_details of this RecipientUpdateResponse.

        :return: The error_details of this RecipientUpdateResponse.
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """
        Sets the error_details of this RecipientUpdateResponse.

        :param error_details: The error_details of this RecipientUpdateResponse.
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def recipient_id(self):
        """
        Gets the recipient_id of this RecipientUpdateResponse.
        Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document.

        :return: The recipient_id of this RecipientUpdateResponse.
        :rtype: str
        """
        return self._recipient_id

    @recipient_id.setter
    def recipient_id(self, recipient_id):
        """
        Sets the recipient_id of this RecipientUpdateResponse.
        Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document.

        :param recipient_id: The recipient_id of this RecipientUpdateResponse.
        :type: str
        """

        self._recipient_id = recipient_id

    @property
    def tabs(self):
        """
        Gets the tabs of this RecipientUpdateResponse.

        :return: The tabs of this RecipientUpdateResponse.
        :rtype: Tabs
        """
        return self._tabs

    @tabs.setter
    def tabs(self, tabs):
        """
        Sets the tabs of this RecipientUpdateResponse.

        :param tabs: The tabs of this RecipientUpdateResponse.
        :type: Tabs
        """

        self._tabs = tabs

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
