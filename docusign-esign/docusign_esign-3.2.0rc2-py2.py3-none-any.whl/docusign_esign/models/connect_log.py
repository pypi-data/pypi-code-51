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


class ConnectLog(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, account_id=None, config_url=None, connect_debug_log=None, connect_id=None, created=None, email=None, envelope_id=None, error=None, failure_id=None, failure_uri=None, last_try=None, log_id=None, log_uri=None, retry_count=None, retry_uri=None, status=None, subject=None, user_name=None):
        """
        ConnectLog - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'account_id': 'str',
            'config_url': 'str',
            'connect_debug_log': 'list[ConnectDebugLog]',
            'connect_id': 'str',
            'created': 'str',
            'email': 'str',
            'envelope_id': 'str',
            'error': 'str',
            'failure_id': 'str',
            'failure_uri': 'str',
            'last_try': 'str',
            'log_id': 'str',
            'log_uri': 'str',
            'retry_count': 'str',
            'retry_uri': 'str',
            'status': 'str',
            'subject': 'str',
            'user_name': 'str'
        }

        self.attribute_map = {
            'account_id': 'accountId',
            'config_url': 'configUrl',
            'connect_debug_log': 'connectDebugLog',
            'connect_id': 'connectId',
            'created': 'created',
            'email': 'email',
            'envelope_id': 'envelopeId',
            'error': 'error',
            'failure_id': 'failureId',
            'failure_uri': 'failureUri',
            'last_try': 'lastTry',
            'log_id': 'logId',
            'log_uri': 'logUri',
            'retry_count': 'retryCount',
            'retry_uri': 'retryUri',
            'status': 'status',
            'subject': 'subject',
            'user_name': 'userName'
        }

        self._account_id = account_id
        self._config_url = config_url
        self._connect_debug_log = connect_debug_log
        self._connect_id = connect_id
        self._created = created
        self._email = email
        self._envelope_id = envelope_id
        self._error = error
        self._failure_id = failure_id
        self._failure_uri = failure_uri
        self._last_try = last_try
        self._log_id = log_id
        self._log_uri = log_uri
        self._retry_count = retry_count
        self._retry_uri = retry_uri
        self._status = status
        self._subject = subject
        self._user_name = user_name

    @property
    def account_id(self):
        """
        Gets the account_id of this ConnectLog.
        The account ID associated with the envelope.

        :return: The account_id of this ConnectLog.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """
        Sets the account_id of this ConnectLog.
        The account ID associated with the envelope.

        :param account_id: The account_id of this ConnectLog.
        :type: str
        """

        self._account_id = account_id

    @property
    def config_url(self):
        """
        Gets the config_url of this ConnectLog.
        The web address of the listener or Retrieving Service end point for Connect.

        :return: The config_url of this ConnectLog.
        :rtype: str
        """
        return self._config_url

    @config_url.setter
    def config_url(self, config_url):
        """
        Sets the config_url of this ConnectLog.
        The web address of the listener or Retrieving Service end point for Connect.

        :param config_url: The config_url of this ConnectLog.
        :type: str
        """

        self._config_url = config_url

    @property
    def connect_debug_log(self):
        """
        Gets the connect_debug_log of this ConnectLog.
        A complex element containing information about the Connect configuration, error details, date/time, description and payload.  This is only included in the response if the query additional_info=true is used.

        :return: The connect_debug_log of this ConnectLog.
        :rtype: list[ConnectDebugLog]
        """
        return self._connect_debug_log

    @connect_debug_log.setter
    def connect_debug_log(self, connect_debug_log):
        """
        Sets the connect_debug_log of this ConnectLog.
        A complex element containing information about the Connect configuration, error details, date/time, description and payload.  This is only included in the response if the query additional_info=true is used.

        :param connect_debug_log: The connect_debug_log of this ConnectLog.
        :type: list[ConnectDebugLog]
        """

        self._connect_debug_log = connect_debug_log

    @property
    def connect_id(self):
        """
        Gets the connect_id of this ConnectLog.
        The identifier for the Connect configuration that failed. If an account has multiple Connect configurations, this value is used to look up the Connect configuration for the failed post.

        :return: The connect_id of this ConnectLog.
        :rtype: str
        """
        return self._connect_id

    @connect_id.setter
    def connect_id(self, connect_id):
        """
        Sets the connect_id of this ConnectLog.
        The identifier for the Connect configuration that failed. If an account has multiple Connect configurations, this value is used to look up the Connect configuration for the failed post.

        :param connect_id: The connect_id of this ConnectLog.
        :type: str
        """

        self._connect_id = connect_id

    @property
    def created(self):
        """
        Gets the created of this ConnectLog.
        The date and time the entry was created.

        :return: The created of this ConnectLog.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this ConnectLog.
        The date and time the entry was created.

        :param created: The created of this ConnectLog.
        :type: str
        """

        self._created = created

    @property
    def email(self):
        """
        Gets the email of this ConnectLog.
        The email that sent the envelope.

        :return: The email of this ConnectLog.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this ConnectLog.
        The email that sent the envelope.

        :param email: The email of this ConnectLog.
        :type: str
        """

        self._email = email

    @property
    def envelope_id(self):
        """
        Gets the envelope_id of this ConnectLog.
        The envelope ID of the envelope status that failed to post.

        :return: The envelope_id of this ConnectLog.
        :rtype: str
        """
        return self._envelope_id

    @envelope_id.setter
    def envelope_id(self, envelope_id):
        """
        Sets the envelope_id of this ConnectLog.
        The envelope ID of the envelope status that failed to post.

        :param envelope_id: The envelope_id of this ConnectLog.
        :type: str
        """

        self._envelope_id = envelope_id

    @property
    def error(self):
        """
        Gets the error of this ConnectLog.
        The error that caused the Connect post to fail.

        :return: The error of this ConnectLog.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this ConnectLog.
        The error that caused the Connect post to fail.

        :param error: The error of this ConnectLog.
        :type: str
        """

        self._error = error

    @property
    def failure_id(self):
        """
        Gets the failure_id of this ConnectLog.
        The failure log ID for the failure.

        :return: The failure_id of this ConnectLog.
        :rtype: str
        """
        return self._failure_id

    @failure_id.setter
    def failure_id(self, failure_id):
        """
        Sets the failure_id of this ConnectLog.
        The failure log ID for the failure.

        :param failure_id: The failure_id of this ConnectLog.
        :type: str
        """

        self._failure_id = failure_id

    @property
    def failure_uri(self):
        """
        Gets the failure_uri of this ConnectLog.
        The URI for the failure.

        :return: The failure_uri of this ConnectLog.
        :rtype: str
        """
        return self._failure_uri

    @failure_uri.setter
    def failure_uri(self, failure_uri):
        """
        Sets the failure_uri of this ConnectLog.
        The URI for the failure.

        :param failure_uri: The failure_uri of this ConnectLog.
        :type: str
        """

        self._failure_uri = failure_uri

    @property
    def last_try(self):
        """
        Gets the last_try of this ConnectLog.
        The date and time the last attempt to post.

        :return: The last_try of this ConnectLog.
        :rtype: str
        """
        return self._last_try

    @last_try.setter
    def last_try(self, last_try):
        """
        Sets the last_try of this ConnectLog.
        The date and time the last attempt to post.

        :param last_try: The last_try of this ConnectLog.
        :type: str
        """

        self._last_try = last_try

    @property
    def log_id(self):
        """
        Gets the log_id of this ConnectLog.
        The Connect log ID for the entry.

        :return: The log_id of this ConnectLog.
        :rtype: str
        """
        return self._log_id

    @log_id.setter
    def log_id(self, log_id):
        """
        Sets the log_id of this ConnectLog.
        The Connect log ID for the entry.

        :param log_id: The log_id of this ConnectLog.
        :type: str
        """

        self._log_id = log_id

    @property
    def log_uri(self):
        """
        Gets the log_uri of this ConnectLog.
        The URI for the log item.

        :return: The log_uri of this ConnectLog.
        :rtype: str
        """
        return self._log_uri

    @log_uri.setter
    def log_uri(self, log_uri):
        """
        Sets the log_uri of this ConnectLog.
        The URI for the log item.

        :param log_uri: The log_uri of this ConnectLog.
        :type: str
        """

        self._log_uri = log_uri

    @property
    def retry_count(self):
        """
        Gets the retry_count of this ConnectLog.
        The number of times the Connect post has been retried.

        :return: The retry_count of this ConnectLog.
        :rtype: str
        """
        return self._retry_count

    @retry_count.setter
    def retry_count(self, retry_count):
        """
        Sets the retry_count of this ConnectLog.
        The number of times the Connect post has been retried.

        :param retry_count: The retry_count of this ConnectLog.
        :type: str
        """

        self._retry_count = retry_count

    @property
    def retry_uri(self):
        """
        Gets the retry_uri of this ConnectLog.
        The UEI to retry to publish the Connect failure.

        :return: The retry_uri of this ConnectLog.
        :rtype: str
        """
        return self._retry_uri

    @retry_uri.setter
    def retry_uri(self, retry_uri):
        """
        Sets the retry_uri of this ConnectLog.
        The UEI to retry to publish the Connect failure.

        :param retry_uri: The retry_uri of this ConnectLog.
        :type: str
        """

        self._retry_uri = retry_uri

    @property
    def status(self):
        """
        Gets the status of this ConnectLog.
        The new envelope status for the failed Connect post. The possible values are: Any, Voided, Created, Deleted, Sent, Delivered, Signed, Completed, Declined, TimedOut, Template, or Processing.

        :return: The status of this ConnectLog.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ConnectLog.
        The new envelope status for the failed Connect post. The possible values are: Any, Voided, Created, Deleted, Sent, Delivered, Signed, Completed, Declined, TimedOut, Template, or Processing.

        :param status: The status of this ConnectLog.
        :type: str
        """

        self._status = status

    @property
    def subject(self):
        """
        Gets the subject of this ConnectLog.
        The envelope subject.

        :return: The subject of this ConnectLog.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this ConnectLog.
        The envelope subject.

        :param subject: The subject of this ConnectLog.
        :type: str
        """

        self._subject = subject

    @property
    def user_name(self):
        """
        Gets the user_name of this ConnectLog.
        The name of the envelope sender.

        :return: The user_name of this ConnectLog.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this ConnectLog.
        The name of the envelope sender.

        :param user_name: The user_name of this ConnectLog.
        :type: str
        """

        self._user_name = user_name

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
