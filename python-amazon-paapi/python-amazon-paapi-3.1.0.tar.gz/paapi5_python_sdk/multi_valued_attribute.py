# coding: utf-8

"""
 Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

 Licensed under the Apache License, Version 2.0 (the "License").
 You may not use this file except in compliance with the License.
 A copy of the License is located at

     http://www.apache.org/licenses/LICENSE-2.0

 or in the "license" file accompanying this file. This file is distributed
 on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
 express or implied. See the License for the specific language governing
 permissions and limitations under the License.
"""

"""
    ProductAdvertisingAPI

    https://webservices.amazon.com/paapi5/documentation/index.html  # noqa: E501
"""


import pprint
import re  # noqa: F401

import six


class MultiValuedAttribute(object):
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
        'display_values': 'list[str]',
        'label': 'str',
        'locale': 'str'
    }

    attribute_map = {
        'display_values': 'DisplayValues',
        'label': 'Label',
        'locale': 'Locale'
    }

    def __init__(self, display_values=None, label=None, locale=None):  # noqa: E501
        """MultiValuedAttribute - a model defined in Swagger"""  # noqa: E501

        self._display_values = None
        self._label = None
        self._locale = None
        self.discriminator = None

        if display_values is not None:
            self.display_values = display_values
        if label is not None:
            self.label = label
        if locale is not None:
            self.locale = locale

    @property
    def display_values(self):
        """Gets the display_values of this MultiValuedAttribute.  # noqa: E501


        :return: The display_values of this MultiValuedAttribute.  # noqa: E501
        :rtype: list[str]
        """
        return self._display_values

    @display_values.setter
    def display_values(self, display_values):
        """Sets the display_values of this MultiValuedAttribute.


        :param display_values: The display_values of this MultiValuedAttribute.  # noqa: E501
        :type: list[str]
        """

        self._display_values = display_values

    @property
    def label(self):
        """Gets the label of this MultiValuedAttribute.  # noqa: E501


        :return: The label of this MultiValuedAttribute.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this MultiValuedAttribute.


        :param label: The label of this MultiValuedAttribute.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def locale(self):
        """Gets the locale of this MultiValuedAttribute.  # noqa: E501


        :return: The locale of this MultiValuedAttribute.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this MultiValuedAttribute.


        :param locale: The locale of this MultiValuedAttribute.  # noqa: E501
        :type: str
        """

        self._locale = locale

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
        if issubclass(MultiValuedAttribute, dict):
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
        if not isinstance(other, MultiValuedAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
