# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UserSharedItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, error_details=None, shared=None, user=None):
        """
        UserSharedItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'error_details': 'ErrorDetails',
            'shared': 'str',
            'user': 'UserInfo'
        }

        self.attribute_map = {
            'error_details': 'errorDetails',
            'shared': 'shared',
            'user': 'user'
        }

        self._error_details = error_details
        self._shared = shared
        self._user = user

    @property
    def error_details(self):
        """
        Gets the error_details of this UserSharedItem.

        :return: The error_details of this UserSharedItem.
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """
        Sets the error_details of this UserSharedItem.

        :param error_details: The error_details of this UserSharedItem.
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def shared(self):
        """
        Gets the shared of this UserSharedItem.
        When set to **true**, this custom tab is shared.

        :return: The shared of this UserSharedItem.
        :rtype: str
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """
        Sets the shared of this UserSharedItem.
        When set to **true**, this custom tab is shared.

        :param shared: The shared of this UserSharedItem.
        :type: str
        """

        self._shared = shared

    @property
    def user(self):
        """
        Gets the user of this UserSharedItem.

        :return: The user of this UserSharedItem.
        :rtype: UserInfo
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this UserSharedItem.

        :param user: The user of this UserSharedItem.
        :type: UserInfo
        """

        self._user = user

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
