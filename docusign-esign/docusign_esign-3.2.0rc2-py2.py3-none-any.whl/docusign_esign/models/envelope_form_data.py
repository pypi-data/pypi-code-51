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


class EnvelopeFormData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, email_subject=None, envelope_id=None, form_data=None, recipient_form_data=None, sent_date_time=None, status=None):
        """
        EnvelopeFormData - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'email_subject': 'str',
            'envelope_id': 'str',
            'form_data': 'list[FormDataItem]',
            'recipient_form_data': 'list[RecipientFormData]',
            'sent_date_time': 'str',
            'status': 'str'
        }

        self.attribute_map = {
            'email_subject': 'emailSubject',
            'envelope_id': 'envelopeId',
            'form_data': 'formData',
            'recipient_form_data': 'recipientFormData',
            'sent_date_time': 'sentDateTime',
            'status': 'status'
        }

        self._email_subject = email_subject
        self._envelope_id = envelope_id
        self._form_data = form_data
        self._recipient_form_data = recipient_form_data
        self._sent_date_time = sent_date_time
        self._status = status

    @property
    def email_subject(self):
        """
        Gets the email_subject of this EnvelopeFormData.
        Specifies the subject of the email that is sent to all recipients.  See [ML:Template Email Subject Merge Fields] for information about adding merge field information to the email subject.

        :return: The email_subject of this EnvelopeFormData.
        :rtype: str
        """
        return self._email_subject

    @email_subject.setter
    def email_subject(self, email_subject):
        """
        Sets the email_subject of this EnvelopeFormData.
        Specifies the subject of the email that is sent to all recipients.  See [ML:Template Email Subject Merge Fields] for information about adding merge field information to the email subject.

        :param email_subject: The email_subject of this EnvelopeFormData.
        :type: str
        """

        self._email_subject = email_subject

    @property
    def envelope_id(self):
        """
        Gets the envelope_id of this EnvelopeFormData.
        The envelope ID of the envelope status that failed to post.

        :return: The envelope_id of this EnvelopeFormData.
        :rtype: str
        """
        return self._envelope_id

    @envelope_id.setter
    def envelope_id(self, envelope_id):
        """
        Sets the envelope_id of this EnvelopeFormData.
        The envelope ID of the envelope status that failed to post.

        :param envelope_id: The envelope_id of this EnvelopeFormData.
        :type: str
        """

        self._envelope_id = envelope_id

    @property
    def form_data(self):
        """
        Gets the form_data of this EnvelopeFormData.
        

        :return: The form_data of this EnvelopeFormData.
        :rtype: list[FormDataItem]
        """
        return self._form_data

    @form_data.setter
    def form_data(self, form_data):
        """
        Sets the form_data of this EnvelopeFormData.
        

        :param form_data: The form_data of this EnvelopeFormData.
        :type: list[FormDataItem]
        """

        self._form_data = form_data

    @property
    def recipient_form_data(self):
        """
        Gets the recipient_form_data of this EnvelopeFormData.
        

        :return: The recipient_form_data of this EnvelopeFormData.
        :rtype: list[RecipientFormData]
        """
        return self._recipient_form_data

    @recipient_form_data.setter
    def recipient_form_data(self, recipient_form_data):
        """
        Sets the recipient_form_data of this EnvelopeFormData.
        

        :param recipient_form_data: The recipient_form_data of this EnvelopeFormData.
        :type: list[RecipientFormData]
        """

        self._recipient_form_data = recipient_form_data

    @property
    def sent_date_time(self):
        """
        Gets the sent_date_time of this EnvelopeFormData.
        The date and time the envelope was sent.

        :return: The sent_date_time of this EnvelopeFormData.
        :rtype: str
        """
        return self._sent_date_time

    @sent_date_time.setter
    def sent_date_time(self, sent_date_time):
        """
        Sets the sent_date_time of this EnvelopeFormData.
        The date and time the envelope was sent.

        :param sent_date_time: The sent_date_time of this EnvelopeFormData.
        :type: str
        """

        self._sent_date_time = sent_date_time

    @property
    def status(self):
        """
        Gets the status of this EnvelopeFormData.
        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.

        :return: The status of this EnvelopeFormData.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this EnvelopeFormData.
        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.

        :param status: The status of this EnvelopeFormData.
        :type: str
        """

        self._status = status

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
