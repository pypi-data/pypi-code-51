# coding: utf-8

"""
    Flip API

    Flip  # noqa: E501

    The version of the OpenAPI document: 3.1
    Contact: cloudsupport@telestream.net
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from telestream_cloud_flip.configuration import Configuration


class CopyProfileBody(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'dest_factory_id': 'str',
        'profile_name': 'str'
    }

    attribute_map = {
        'dest_factory_id': 'dest_factory_id',
        'profile_name': 'profile_name'
    }

    def __init__(self, dest_factory_id=None, profile_name=None, local_vars_configuration=None):  # noqa: E501
        """CopyProfileBody - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dest_factory_id = None
        self._profile_name = None
        self.discriminator = None

        self.dest_factory_id = dest_factory_id
        self.profile_name = profile_name

    @property
    def dest_factory_id(self):
        """Gets the dest_factory_id of this CopyProfileBody.  # noqa: E501

        an id of a target Factory that will own a copy of the Profile  # noqa: E501

        :return: The dest_factory_id of this CopyProfileBody.  # noqa: E501
        :rtype: str
        """
        return self._dest_factory_id

    @dest_factory_id.setter
    def dest_factory_id(self, dest_factory_id):
        """Sets the dest_factory_id of this CopyProfileBody.

        an id of a target Factory that will own a copy of the Profile  # noqa: E501

        :param dest_factory_id: The dest_factory_id of this CopyProfileBody.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and dest_factory_id is None:  # noqa: E501
            raise ValueError("Invalid value for `dest_factory_id`, must not be `None`")  # noqa: E501

        self._dest_factory_id = dest_factory_id

    @property
    def profile_name(self):
        """Gets the profile_name of this CopyProfileBody.  # noqa: E501

        a name for a copy of the Profile  # noqa: E501

        :return: The profile_name of this CopyProfileBody.  # noqa: E501
        :rtype: str
        """
        return self._profile_name

    @profile_name.setter
    def profile_name(self, profile_name):
        """Sets the profile_name of this CopyProfileBody.

        a name for a copy of the Profile  # noqa: E501

        :param profile_name: The profile_name of this CopyProfileBody.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and profile_name is None:  # noqa: E501
            raise ValueError("Invalid value for `profile_name`, must not be `None`")  # noqa: E501

        self._profile_name = profile_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CopyProfileBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CopyProfileBody):
            return True

        return self.to_dict() != other.to_dict()
