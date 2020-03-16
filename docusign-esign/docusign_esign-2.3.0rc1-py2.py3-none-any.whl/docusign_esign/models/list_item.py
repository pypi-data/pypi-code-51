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


class ListItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, selected=None, text=None, value=None):
        """
        ListItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'selected': 'str',
            'text': 'str',
            'value': 'str'
        }

        self.attribute_map = {
            'selected': 'selected',
            'text': 'text',
            'value': 'value'
        }

        self._selected = selected
        self._text = text
        self._value = value

    @property
    def selected(self):
        """
        Gets the selected of this ListItem.
        When set to **true**, indicates that this item is the default selection shown to a signer.   Only one selection can be set as the default.

        :return: The selected of this ListItem.
        :rtype: str
        """
        return self._selected

    @selected.setter
    def selected(self, selected):
        """
        Sets the selected of this ListItem.
        When set to **true**, indicates that this item is the default selection shown to a signer.   Only one selection can be set as the default.

        :param selected: The selected of this ListItem.
        :type: str
        """

        self._selected = selected

    @property
    def text(self):
        """
        Gets the text of this ListItem.
        Specifies the text that is shown in the dropdown list. 

        :return: The text of this ListItem.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this ListItem.
        Specifies the text that is shown in the dropdown list. 

        :param text: The text of this ListItem.
        :type: str
        """

        self._text = text

    @property
    def value(self):
        """
        Gets the value of this ListItem.
        Specifies the value that is used when the list item is selected.

        :return: The value of this ListItem.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this ListItem.
        Specifies the value that is used when the list item is selected.

        :param value: The value of this ListItem.
        :type: str
        """

        self._value = value

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
