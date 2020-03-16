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


class SmartSectionCollapsibleDisplaySettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, arrow_closed=None, arrow_color=None, arrow_location=None, arrow_open=None, arrow_size=None, arrow_style=None, container_style=None, label_style=None, only_arrow_is_clickable=None, outer_label_and_arrow_style=None):
        """
        SmartSectionCollapsibleDisplaySettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'arrow_closed': 'str',
            'arrow_color': 'str',
            'arrow_location': 'str',
            'arrow_open': 'str',
            'arrow_size': 'str',
            'arrow_style': 'str',
            'container_style': 'str',
            'label_style': 'str',
            'only_arrow_is_clickable': 'bool',
            'outer_label_and_arrow_style': 'str'
        }

        self.attribute_map = {
            'arrow_closed': 'arrowClosed',
            'arrow_color': 'arrowColor',
            'arrow_location': 'arrowLocation',
            'arrow_open': 'arrowOpen',
            'arrow_size': 'arrowSize',
            'arrow_style': 'arrowStyle',
            'container_style': 'containerStyle',
            'label_style': 'labelStyle',
            'only_arrow_is_clickable': 'onlyArrowIsClickable',
            'outer_label_and_arrow_style': 'outerLabelAndArrowStyle'
        }

        self._arrow_closed = arrow_closed
        self._arrow_color = arrow_color
        self._arrow_location = arrow_location
        self._arrow_open = arrow_open
        self._arrow_size = arrow_size
        self._arrow_style = arrow_style
        self._container_style = container_style
        self._label_style = label_style
        self._only_arrow_is_clickable = only_arrow_is_clickable
        self._outer_label_and_arrow_style = outer_label_and_arrow_style

    @property
    def arrow_closed(self):
        """
        Gets the arrow_closed of this SmartSectionCollapsibleDisplaySettings.
        

        :return: The arrow_closed of this SmartSectionCollapsibleDisplaySettings.
        :rtype: str
        """
        return self._arrow_closed

    @arrow_closed.setter
    def arrow_closed(self, arrow_closed):
        """
        Sets the arrow_closed of this SmartSectionCollapsibleDisplaySettings.
        

        :param arrow_closed: The arrow_closed of this SmartSectionCollapsibleDisplaySettings.
        :type: str
        """

        self._arrow_closed = arrow_closed

    @property
    def arrow_color(self):
        """
        Gets the arrow_color of this SmartSectionCollapsibleDisplaySettings.
        

        :return: The arrow_color of this SmartSectionCollapsibleDisplaySettings.
        :rtype: str
        """
        return self._arrow_color

    @arrow_color.setter
    def arrow_color(self, arrow_color):
        """
        Sets the arrow_color of this SmartSectionCollapsibleDisplaySettings.
        

        :param arrow_color: The arrow_color of this SmartSectionCollapsibleDisplaySettings.
        :type: str
        """

        self._arrow_color = arrow_color

    @property
    def arrow_location(self):
        """
        Gets the arrow_location of this SmartSectionCollapsibleDisplaySettings.
        

        :return: The arrow_location of this SmartSectionCollapsibleDisplaySettings.
        :rtype: str
        """
        return self._arrow_location

    @arrow_location.setter
    def arrow_location(self, arrow_location):
        """
        Sets the arrow_location of this SmartSectionCollapsibleDisplaySettings.
        

        :param arrow_location: The arrow_location of this SmartSectionCollapsibleDisplaySettings.
        :type: str
        """

        self._arrow_location = arrow_location

    @property
    def arrow_open(self):
        """
        Gets the arrow_open of this SmartSectionCollapsibleDisplaySettings.
        

        :return: The arrow_open of this SmartSectionCollapsibleDisplaySettings.
        :rtype: str
        """
        return self._arrow_open

    @arrow_open.setter
    def arrow_open(self, arrow_open):
        """
        Sets the arrow_open of this SmartSectionCollapsibleDisplaySettings.
        

        :param arrow_open: The arrow_open of this SmartSectionCollapsibleDisplaySettings.
        :type: str
        """

        self._arrow_open = arrow_open

    @property
    def arrow_size(self):
        """
        Gets the arrow_size of this SmartSectionCollapsibleDisplaySettings.
        

        :return: The arrow_size of this SmartSectionCollapsibleDisplaySettings.
        :rtype: str
        """
        return self._arrow_size

    @arrow_size.setter
    def arrow_size(self, arrow_size):
        """
        Sets the arrow_size of this SmartSectionCollapsibleDisplaySettings.
        

        :param arrow_size: The arrow_size of this SmartSectionCollapsibleDisplaySettings.
        :type: str
        """

        self._arrow_size = arrow_size

    @property
    def arrow_style(self):
        """
        Gets the arrow_style of this SmartSectionCollapsibleDisplaySettings.
        

        :return: The arrow_style of this SmartSectionCollapsibleDisplaySettings.
        :rtype: str
        """
        return self._arrow_style

    @arrow_style.setter
    def arrow_style(self, arrow_style):
        """
        Sets the arrow_style of this SmartSectionCollapsibleDisplaySettings.
        

        :param arrow_style: The arrow_style of this SmartSectionCollapsibleDisplaySettings.
        :type: str
        """

        self._arrow_style = arrow_style

    @property
    def container_style(self):
        """
        Gets the container_style of this SmartSectionCollapsibleDisplaySettings.
        

        :return: The container_style of this SmartSectionCollapsibleDisplaySettings.
        :rtype: str
        """
        return self._container_style

    @container_style.setter
    def container_style(self, container_style):
        """
        Sets the container_style of this SmartSectionCollapsibleDisplaySettings.
        

        :param container_style: The container_style of this SmartSectionCollapsibleDisplaySettings.
        :type: str
        """

        self._container_style = container_style

    @property
    def label_style(self):
        """
        Gets the label_style of this SmartSectionCollapsibleDisplaySettings.
        

        :return: The label_style of this SmartSectionCollapsibleDisplaySettings.
        :rtype: str
        """
        return self._label_style

    @label_style.setter
    def label_style(self, label_style):
        """
        Sets the label_style of this SmartSectionCollapsibleDisplaySettings.
        

        :param label_style: The label_style of this SmartSectionCollapsibleDisplaySettings.
        :type: str
        """

        self._label_style = label_style

    @property
    def only_arrow_is_clickable(self):
        """
        Gets the only_arrow_is_clickable of this SmartSectionCollapsibleDisplaySettings.
        

        :return: The only_arrow_is_clickable of this SmartSectionCollapsibleDisplaySettings.
        :rtype: bool
        """
        return self._only_arrow_is_clickable

    @only_arrow_is_clickable.setter
    def only_arrow_is_clickable(self, only_arrow_is_clickable):
        """
        Sets the only_arrow_is_clickable of this SmartSectionCollapsibleDisplaySettings.
        

        :param only_arrow_is_clickable: The only_arrow_is_clickable of this SmartSectionCollapsibleDisplaySettings.
        :type: bool
        """

        self._only_arrow_is_clickable = only_arrow_is_clickable

    @property
    def outer_label_and_arrow_style(self):
        """
        Gets the outer_label_and_arrow_style of this SmartSectionCollapsibleDisplaySettings.
        

        :return: The outer_label_and_arrow_style of this SmartSectionCollapsibleDisplaySettings.
        :rtype: str
        """
        return self._outer_label_and_arrow_style

    @outer_label_and_arrow_style.setter
    def outer_label_and_arrow_style(self, outer_label_and_arrow_style):
        """
        Sets the outer_label_and_arrow_style of this SmartSectionCollapsibleDisplaySettings.
        

        :param outer_label_and_arrow_style: The outer_label_and_arrow_style of this SmartSectionCollapsibleDisplaySettings.
        :type: str
        """

        self._outer_label_and_arrow_style = outer_label_and_arrow_style

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
