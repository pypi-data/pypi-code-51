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


class PaymentGatewayAccountSetting(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, api_fields=None, authorization_code=None, credential_status=None, merchant_id=None):
        """
        PaymentGatewayAccountSetting - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'api_fields': 'str',
            'authorization_code': 'str',
            'credential_status': 'str',
            'merchant_id': 'str'
        }

        self.attribute_map = {
            'api_fields': 'apiFields',
            'authorization_code': 'authorizationCode',
            'credential_status': 'credentialStatus',
            'merchant_id': 'merchantId'
        }

        self._api_fields = api_fields
        self._authorization_code = authorization_code
        self._credential_status = credential_status
        self._merchant_id = merchant_id

    @property
    def api_fields(self):
        """
        Gets the api_fields of this PaymentGatewayAccountSetting.
        

        :return: The api_fields of this PaymentGatewayAccountSetting.
        :rtype: str
        """
        return self._api_fields

    @api_fields.setter
    def api_fields(self, api_fields):
        """
        Sets the api_fields of this PaymentGatewayAccountSetting.
        

        :param api_fields: The api_fields of this PaymentGatewayAccountSetting.
        :type: str
        """

        self._api_fields = api_fields

    @property
    def authorization_code(self):
        """
        Gets the authorization_code of this PaymentGatewayAccountSetting.
        

        :return: The authorization_code of this PaymentGatewayAccountSetting.
        :rtype: str
        """
        return self._authorization_code

    @authorization_code.setter
    def authorization_code(self, authorization_code):
        """
        Sets the authorization_code of this PaymentGatewayAccountSetting.
        

        :param authorization_code: The authorization_code of this PaymentGatewayAccountSetting.
        :type: str
        """

        self._authorization_code = authorization_code

    @property
    def credential_status(self):
        """
        Gets the credential_status of this PaymentGatewayAccountSetting.
        

        :return: The credential_status of this PaymentGatewayAccountSetting.
        :rtype: str
        """
        return self._credential_status

    @credential_status.setter
    def credential_status(self, credential_status):
        """
        Sets the credential_status of this PaymentGatewayAccountSetting.
        

        :param credential_status: The credential_status of this PaymentGatewayAccountSetting.
        :type: str
        """

        self._credential_status = credential_status

    @property
    def merchant_id(self):
        """
        Gets the merchant_id of this PaymentGatewayAccountSetting.
        

        :return: The merchant_id of this PaymentGatewayAccountSetting.
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """
        Sets the merchant_id of this PaymentGatewayAccountSetting.
        

        :param merchant_id: The merchant_id of this PaymentGatewayAccountSetting.
        :type: str
        """

        self._merchant_id = merchant_id

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
