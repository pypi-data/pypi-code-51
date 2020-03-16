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


class AccountSignatureProviderOption(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, signature_provider_option_display_name=None, signature_provider_option_id=None, signature_provider_option_name=None):
        """
        AccountSignatureProviderOption - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'signature_provider_option_display_name': 'str',
            'signature_provider_option_id': 'str',
            'signature_provider_option_name': 'str'
        }

        self.attribute_map = {
            'signature_provider_option_display_name': 'signatureProviderOptionDisplayName',
            'signature_provider_option_id': 'signatureProviderOptionId',
            'signature_provider_option_name': 'signatureProviderOptionName'
        }

        self._signature_provider_option_display_name = signature_provider_option_display_name
        self._signature_provider_option_id = signature_provider_option_id
        self._signature_provider_option_name = signature_provider_option_name

    @property
    def signature_provider_option_display_name(self):
        """
        Gets the signature_provider_option_display_name of this AccountSignatureProviderOption.
        

        :return: The signature_provider_option_display_name of this AccountSignatureProviderOption.
        :rtype: str
        """
        return self._signature_provider_option_display_name

    @signature_provider_option_display_name.setter
    def signature_provider_option_display_name(self, signature_provider_option_display_name):
        """
        Sets the signature_provider_option_display_name of this AccountSignatureProviderOption.
        

        :param signature_provider_option_display_name: The signature_provider_option_display_name of this AccountSignatureProviderOption.
        :type: str
        """

        self._signature_provider_option_display_name = signature_provider_option_display_name

    @property
    def signature_provider_option_id(self):
        """
        Gets the signature_provider_option_id of this AccountSignatureProviderOption.
        

        :return: The signature_provider_option_id of this AccountSignatureProviderOption.
        :rtype: str
        """
        return self._signature_provider_option_id

    @signature_provider_option_id.setter
    def signature_provider_option_id(self, signature_provider_option_id):
        """
        Sets the signature_provider_option_id of this AccountSignatureProviderOption.
        

        :param signature_provider_option_id: The signature_provider_option_id of this AccountSignatureProviderOption.
        :type: str
        """

        self._signature_provider_option_id = signature_provider_option_id

    @property
    def signature_provider_option_name(self):
        """
        Gets the signature_provider_option_name of this AccountSignatureProviderOption.
        

        :return: The signature_provider_option_name of this AccountSignatureProviderOption.
        :rtype: str
        """
        return self._signature_provider_option_name

    @signature_provider_option_name.setter
    def signature_provider_option_name(self, signature_provider_option_name):
        """
        Sets the signature_provider_option_name of this AccountSignatureProviderOption.
        

        :param signature_provider_option_name: The signature_provider_option_name of this AccountSignatureProviderOption.
        :type: str
        """

        self._signature_provider_option_name = signature_provider_option_name

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
