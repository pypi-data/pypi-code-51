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


class BillingPlanUpdateResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, account_payment_method=None, billing_plan_preview=None, currency_code=None, included_seats=None, payment_cycle=None, payment_method=None, plan_id=None, plan_name=None):
        """
        BillingPlanUpdateResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'account_payment_method': 'str',
            'billing_plan_preview': 'BillingPlanPreview',
            'currency_code': 'str',
            'included_seats': 'str',
            'payment_cycle': 'str',
            'payment_method': 'str',
            'plan_id': 'str',
            'plan_name': 'str'
        }

        self.attribute_map = {
            'account_payment_method': 'accountPaymentMethod',
            'billing_plan_preview': 'billingPlanPreview',
            'currency_code': 'currencyCode',
            'included_seats': 'includedSeats',
            'payment_cycle': 'paymentCycle',
            'payment_method': 'paymentMethod',
            'plan_id': 'planId',
            'plan_name': 'planName'
        }

        self._account_payment_method = account_payment_method
        self._billing_plan_preview = billing_plan_preview
        self._currency_code = currency_code
        self._included_seats = included_seats
        self._payment_cycle = payment_cycle
        self._payment_method = payment_method
        self._plan_id = plan_id
        self._plan_name = plan_name

    @property
    def account_payment_method(self):
        """
        Gets the account_payment_method of this BillingPlanUpdateResponse.
        

        :return: The account_payment_method of this BillingPlanUpdateResponse.
        :rtype: str
        """
        return self._account_payment_method

    @account_payment_method.setter
    def account_payment_method(self, account_payment_method):
        """
        Sets the account_payment_method of this BillingPlanUpdateResponse.
        

        :param account_payment_method: The account_payment_method of this BillingPlanUpdateResponse.
        :type: str
        """

        self._account_payment_method = account_payment_method

    @property
    def billing_plan_preview(self):
        """
        Gets the billing_plan_preview of this BillingPlanUpdateResponse.

        :return: The billing_plan_preview of this BillingPlanUpdateResponse.
        :rtype: BillingPlanPreview
        """
        return self._billing_plan_preview

    @billing_plan_preview.setter
    def billing_plan_preview(self, billing_plan_preview):
        """
        Sets the billing_plan_preview of this BillingPlanUpdateResponse.

        :param billing_plan_preview: The billing_plan_preview of this BillingPlanUpdateResponse.
        :type: BillingPlanPreview
        """

        self._billing_plan_preview = billing_plan_preview

    @property
    def currency_code(self):
        """
        Gets the currency_code of this BillingPlanUpdateResponse.
        Specifies the ISO currency code for the account.

        :return: The currency_code of this BillingPlanUpdateResponse.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """
        Sets the currency_code of this BillingPlanUpdateResponse.
        Specifies the ISO currency code for the account.

        :param currency_code: The currency_code of this BillingPlanUpdateResponse.
        :type: str
        """

        self._currency_code = currency_code

    @property
    def included_seats(self):
        """
        Gets the included_seats of this BillingPlanUpdateResponse.
        The number of seats (users) included.

        :return: The included_seats of this BillingPlanUpdateResponse.
        :rtype: str
        """
        return self._included_seats

    @included_seats.setter
    def included_seats(self, included_seats):
        """
        Sets the included_seats of this BillingPlanUpdateResponse.
        The number of seats (users) included.

        :param included_seats: The included_seats of this BillingPlanUpdateResponse.
        :type: str
        """

        self._included_seats = included_seats

    @property
    def payment_cycle(self):
        """
        Gets the payment_cycle of this BillingPlanUpdateResponse.
        

        :return: The payment_cycle of this BillingPlanUpdateResponse.
        :rtype: str
        """
        return self._payment_cycle

    @payment_cycle.setter
    def payment_cycle(self, payment_cycle):
        """
        Sets the payment_cycle of this BillingPlanUpdateResponse.
        

        :param payment_cycle: The payment_cycle of this BillingPlanUpdateResponse.
        :type: str
        """

        self._payment_cycle = payment_cycle

    @property
    def payment_method(self):
        """
        Gets the payment_method of this BillingPlanUpdateResponse.
        

        :return: The payment_method of this BillingPlanUpdateResponse.
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """
        Sets the payment_method of this BillingPlanUpdateResponse.
        

        :param payment_method: The payment_method of this BillingPlanUpdateResponse.
        :type: str
        """

        self._payment_method = payment_method

    @property
    def plan_id(self):
        """
        Gets the plan_id of this BillingPlanUpdateResponse.
        

        :return: The plan_id of this BillingPlanUpdateResponse.
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """
        Sets the plan_id of this BillingPlanUpdateResponse.
        

        :param plan_id: The plan_id of this BillingPlanUpdateResponse.
        :type: str
        """

        self._plan_id = plan_id

    @property
    def plan_name(self):
        """
        Gets the plan_name of this BillingPlanUpdateResponse.
        

        :return: The plan_name of this BillingPlanUpdateResponse.
        :rtype: str
        """
        return self._plan_name

    @plan_name.setter
    def plan_name(self, plan_name):
        """
        Sets the plan_name of this BillingPlanUpdateResponse.
        

        :param plan_name: The plan_name of this BillingPlanUpdateResponse.
        :type: str
        """

        self._plan_name = plan_name

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
