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


class CommentHistoryResult(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, comments=None, count=None, end_timetoken=None, start_timetoken=None):
        """
        CommentHistoryResult - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'comments': 'list[Comment]',
            'count': 'int',
            'end_timetoken': 'str',
            'start_timetoken': 'str'
        }

        self.attribute_map = {
            'comments': 'comments',
            'count': 'count',
            'end_timetoken': 'endTimetoken',
            'start_timetoken': 'startTimetoken'
        }

        self._comments = comments
        self._count = count
        self._end_timetoken = end_timetoken
        self._start_timetoken = start_timetoken

    @property
    def comments(self):
        """
        Gets the comments of this CommentHistoryResult.
        

        :return: The comments of this CommentHistoryResult.
        :rtype: list[Comment]
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """
        Sets the comments of this CommentHistoryResult.
        

        :param comments: The comments of this CommentHistoryResult.
        :type: list[Comment]
        """

        self._comments = comments

    @property
    def count(self):
        """
        Gets the count of this CommentHistoryResult.
        

        :return: The count of this CommentHistoryResult.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this CommentHistoryResult.
        

        :param count: The count of this CommentHistoryResult.
        :type: int
        """

        self._count = count

    @property
    def end_timetoken(self):
        """
        Gets the end_timetoken of this CommentHistoryResult.
        

        :return: The end_timetoken of this CommentHistoryResult.
        :rtype: str
        """
        return self._end_timetoken

    @end_timetoken.setter
    def end_timetoken(self, end_timetoken):
        """
        Sets the end_timetoken of this CommentHistoryResult.
        

        :param end_timetoken: The end_timetoken of this CommentHistoryResult.
        :type: str
        """

        self._end_timetoken = end_timetoken

    @property
    def start_timetoken(self):
        """
        Gets the start_timetoken of this CommentHistoryResult.
        

        :return: The start_timetoken of this CommentHistoryResult.
        :rtype: str
        """
        return self._start_timetoken

    @start_timetoken.setter
    def start_timetoken(self, start_timetoken):
        """
        Sets the start_timetoken of this CommentHistoryResult.
        

        :param start_timetoken: The start_timetoken of this CommentHistoryResult.
        :type: str
        """

        self._start_timetoken = start_timetoken

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
