# coding: utf-8

"""
    Nucleus API

    Nucleus text analytics APIs from SumUp Analytics. Example and documentation: https://www.sumup.ai/apis/#nucleus-documentation  # noqa: E501

    OpenAPI spec version: v3.2.4
    Contact: info@sumup.ai
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DocumentNewWordsL1Model(object):
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
        'query': 'list[str]',
        'new_words': 'list[str]',
        'new_sents': 'list[str]',
        'new_sents_titles': 'list[str]',
        'new_sents_urls': 'list[str]',
        'new_sents_docids': 'list[str]'
    }

    attribute_map = {
        'query': 'query',
        'new_words': 'new_words',
        'new_sents': 'new_sents',
        'new_sents_titles': 'new_sents_titles',
        'new_sents_urls': 'new_sents_urls',
        'new_sents_docids': 'new_sents_docids'
    }

    def __init__(self, query=None, new_words=None, new_sents=None, new_sents_titles=None, new_sents_urls=None, new_sents_docids=None):  # noqa: E501
        """DocumentNewWordsL1Model - a model defined in Swagger"""  # noqa: E501

        self._query = None
        self._new_words = None
        self._new_sents = None
        self._new_sents_titles = None
        self._new_sents_urls = None
        self._new_sents_docids = None
        self.discriminator = None

        if query is not None:
            self.query = query
        if new_words is not None:
            self.new_words = new_words
        if new_sents is not None:
            self.new_sents = new_sents
        if new_sents_titles is not None:
            self.new_sents_titles = new_sents_titles
        if new_sents_urls is not None:
            self.new_sents_urls = new_sents_urls
        if new_sents_docids is not None:
            self.new_sents_docids = new_sents_docids

    @property
    def query(self):
        """Gets the query of this DocumentNewWordsL1Model.  # noqa: E501


        :return: The query of this DocumentNewWordsL1Model.  # noqa: E501
        :rtype: list[str]
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this DocumentNewWordsL1Model.


        :param query: The query of this DocumentNewWordsL1Model.  # noqa: E501
        :type: list[str]
        """

        self._query = query

    @property
    def new_words(self):
        """Gets the new_words of this DocumentNewWordsL1Model.  # noqa: E501


        :return: The new_words of this DocumentNewWordsL1Model.  # noqa: E501
        :rtype: list[str]
        """
        return self._new_words

    @new_words.setter
    def new_words(self, new_words):
        """Sets the new_words of this DocumentNewWordsL1Model.


        :param new_words: The new_words of this DocumentNewWordsL1Model.  # noqa: E501
        :type: list[str]
        """

        self._new_words = new_words

    @property
    def new_sents(self):
        """Gets the new_sents of this DocumentNewWordsL1Model.  # noqa: E501


        :return: The new_sents of this DocumentNewWordsL1Model.  # noqa: E501
        :rtype: list[str]
        """
        return self._new_sents

    @new_sents.setter
    def new_sents(self, new_sents):
        """Sets the new_sents of this DocumentNewWordsL1Model.


        :param new_sents: The new_sents of this DocumentNewWordsL1Model.  # noqa: E501
        :type: list[str]
        """

        self._new_sents = new_sents

    @property
    def new_sents_titles(self):
        """Gets the new_sents_titles of this DocumentNewWordsL1Model.  # noqa: E501


        :return: The new_sents_titles of this DocumentNewWordsL1Model.  # noqa: E501
        :rtype: list[str]
        """
        return self._new_sents_titles

    @new_sents_titles.setter
    def new_sents_titles(self, new_sents_titles):
        """Sets the new_sents_titles of this DocumentNewWordsL1Model.


        :param new_sents_titles: The new_sents_titles of this DocumentNewWordsL1Model.  # noqa: E501
        :type: list[str]
        """

        self._new_sents_titles = new_sents_titles

    @property
    def new_sents_urls(self):
        """Gets the new_sents_urls of this DocumentNewWordsL1Model.  # noqa: E501


        :return: The new_sents_urls of this DocumentNewWordsL1Model.  # noqa: E501
        :rtype: list[str]
        """
        return self._new_sents_urls

    @new_sents_urls.setter
    def new_sents_urls(self, new_sents_urls):
        """Sets the new_sents_urls of this DocumentNewWordsL1Model.


        :param new_sents_urls: The new_sents_urls of this DocumentNewWordsL1Model.  # noqa: E501
        :type: list[str]
        """

        self._new_sents_urls = new_sents_urls

    @property
    def new_sents_docids(self):
        """Gets the new_sents_docids of this DocumentNewWordsL1Model.  # noqa: E501


        :return: The new_sents_docids of this DocumentNewWordsL1Model.  # noqa: E501
        :rtype: list[str]
        """
        return self._new_sents_docids

    @new_sents_docids.setter
    def new_sents_docids(self, new_sents_docids):
        """Sets the new_sents_docids of this DocumentNewWordsL1Model.


        :param new_sents_docids: The new_sents_docids of this DocumentNewWordsL1Model.  # noqa: E501
        :type: list[str]
        """

        self._new_sents_docids = new_sents_docids

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
        if issubclass(DocumentNewWordsL1Model, dict):
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
        if not isinstance(other, DocumentNewWordsL1Model):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
