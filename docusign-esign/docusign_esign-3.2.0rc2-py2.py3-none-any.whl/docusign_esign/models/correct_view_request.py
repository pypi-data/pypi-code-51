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


class CorrectViewRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, return_url=None, suppress_navigation=None):
        """
        CorrectViewRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'return_url': 'str',
            'suppress_navigation': 'str'
        }

        self.attribute_map = {
            'return_url': 'returnUrl',
            'suppress_navigation': 'suppressNavigation'
        }

        self._return_url = return_url
        self._suppress_navigation = suppress_navigation

    @property
    def return_url(self):
        """
        Gets the return_url of this CorrectViewRequest.
        The url used after correct/send view session has ended. DocuSign redirects to the url and includes an event parameter that can be used by your app. The event parameters returned are:   * send (user corrected and sent the envelope) * save (user saved the envelope) * cancel (user canceled the transaction.) * error (there was an error when performing the correct or send) * sessionEnd (the session ended before the user completed a different action)  ###### Note: Include https:// in the URL or the redirect might not succeed on some browsers. 

        :return: The return_url of this CorrectViewRequest.
        :rtype: str
        """
        return self._return_url

    @return_url.setter
    def return_url(self, return_url):
        """
        Sets the return_url of this CorrectViewRequest.
        The url used after correct/send view session has ended. DocuSign redirects to the url and includes an event parameter that can be used by your app. The event parameters returned are:   * send (user corrected and sent the envelope) * save (user saved the envelope) * cancel (user canceled the transaction.) * error (there was an error when performing the correct or send) * sessionEnd (the session ended before the user completed a different action)  ###### Note: Include https:// in the URL or the redirect might not succeed on some browsers. 

        :param return_url: The return_url of this CorrectViewRequest.
        :type: str
        """

        self._return_url = return_url

    @property
    def suppress_navigation(self):
        """
        Gets the suppress_navigation of this CorrectViewRequest.
        Specifies whether the window is displayed with or without dressing.

        :return: The suppress_navigation of this CorrectViewRequest.
        :rtype: str
        """
        return self._suppress_navigation

    @suppress_navigation.setter
    def suppress_navigation(self, suppress_navigation):
        """
        Sets the suppress_navigation of this CorrectViewRequest.
        Specifies whether the window is displayed with or without dressing.

        :param suppress_navigation: The suppress_navigation of this CorrectViewRequest.
        :type: str
        """

        self._suppress_navigation = suppress_navigation

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
