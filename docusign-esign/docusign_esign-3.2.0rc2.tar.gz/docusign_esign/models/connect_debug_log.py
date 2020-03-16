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


class ConnectDebugLog(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, connect_config=None, error_details=None, event_date_time=None, event_description=None, payload=None):
        """
        ConnectDebugLog - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'connect_config': 'str',
            'error_details': 'ErrorDetails',
            'event_date_time': 'str',
            'event_description': 'str',
            'payload': 'str'
        }

        self.attribute_map = {
            'connect_config': 'connectConfig',
            'error_details': 'errorDetails',
            'event_date_time': 'eventDateTime',
            'event_description': 'eventDescription',
            'payload': 'payload'
        }

        self._connect_config = connect_config
        self._error_details = error_details
        self._event_date_time = event_date_time
        self._event_description = event_description
        self._payload = payload

    @property
    def connect_config(self):
        """
        Gets the connect_config of this ConnectDebugLog.
        

        :return: The connect_config of this ConnectDebugLog.
        :rtype: str
        """
        return self._connect_config

    @connect_config.setter
    def connect_config(self, connect_config):
        """
        Sets the connect_config of this ConnectDebugLog.
        

        :param connect_config: The connect_config of this ConnectDebugLog.
        :type: str
        """

        self._connect_config = connect_config

    @property
    def error_details(self):
        """
        Gets the error_details of this ConnectDebugLog.

        :return: The error_details of this ConnectDebugLog.
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """
        Sets the error_details of this ConnectDebugLog.

        :param error_details: The error_details of this ConnectDebugLog.
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def event_date_time(self):
        """
        Gets the event_date_time of this ConnectDebugLog.
        

        :return: The event_date_time of this ConnectDebugLog.
        :rtype: str
        """
        return self._event_date_time

    @event_date_time.setter
    def event_date_time(self, event_date_time):
        """
        Sets the event_date_time of this ConnectDebugLog.
        

        :param event_date_time: The event_date_time of this ConnectDebugLog.
        :type: str
        """

        self._event_date_time = event_date_time

    @property
    def event_description(self):
        """
        Gets the event_description of this ConnectDebugLog.
        

        :return: The event_description of this ConnectDebugLog.
        :rtype: str
        """
        return self._event_description

    @event_description.setter
    def event_description(self, event_description):
        """
        Sets the event_description of this ConnectDebugLog.
        

        :param event_description: The event_description of this ConnectDebugLog.
        :type: str
        """

        self._event_description = event_description

    @property
    def payload(self):
        """
        Gets the payload of this ConnectDebugLog.
        

        :return: The payload of this ConnectDebugLog.
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """
        Sets the payload of this ConnectDebugLog.
        

        :param payload: The payload of this ConnectDebugLog.
        :type: str
        """

        self._payload = payload

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
