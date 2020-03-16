# coding: utf-8

"""
    Flywheel

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 11.2.1-rc.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


## NOTE: This file is auto generated by the swagger code generator program.
## Do not edit the file manually.

import pprint
import re  # noqa: F401

import six

from flywheel.models.job_inputs_item import JobInputsItem  # noqa: F401,E501

# NOTE: This file is auto generated by the swagger code generator program.
# Do not edit the class manually.


class JobRequest(object):

    swagger_types = {
        'inputs': 'list[JobInputsItem]',
        'target': 'object',
        'outputs': 'list[object]'
    }

    attribute_map = {
        'inputs': 'inputs',
        'target': 'target',
        'outputs': 'outputs'
    }

    rattribute_map = {
        'inputs': 'inputs',
        'target': 'target',
        'outputs': 'outputs'
    }

    def __init__(self, inputs=None, target=None, outputs=None):  # noqa: E501
        """JobRequest - a model defined in Swagger"""
        super(JobRequest, self).__init__()

        self._inputs = None
        self._target = None
        self._outputs = None
        self.discriminator = None
        self.alt_discriminator = None

        if inputs is not None:
            self.inputs = inputs
        if target is not None:
            self.target = target
        if outputs is not None:
            self.outputs = outputs

    @property
    def inputs(self):
        """Gets the inputs of this JobRequest.


        :return: The inputs of this JobRequest.
        :rtype: list[JobInputsItem]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this JobRequest.


        :param inputs: The inputs of this JobRequest.  # noqa: E501
        :type: list[JobInputsItem]
        """

        self._inputs = inputs

    @property
    def target(self):
        """Gets the target of this JobRequest.


        :return: The target of this JobRequest.
        :rtype: object
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this JobRequest.


        :param target: The target of this JobRequest.  # noqa: E501
        :type: object
        """

        self._target = target

    @property
    def outputs(self):
        """Gets the outputs of this JobRequest.


        :return: The outputs of this JobRequest.
        :rtype: list[object]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this JobRequest.


        :param outputs: The outputs of this JobRequest.  # noqa: E501
        :type: list[object]
        """

        self._outputs = outputs


    @staticmethod
    def positional_to_model(value):
        """Converts a positional argument to a model value"""
        return value

    def return_value(self):
        """Unwraps return value from model"""
        return self

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, JobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

    # Container emulation
    def __getitem__(self, key):
        """Returns the value of key"""
        key = self._map_key(key)
        return getattr(self, key)

    def __setitem__(self, key, value):
        """Sets the value of key"""
        key = self._map_key(key)
        setattr(self, key, value)

    def __contains__(self, key):
        """Checks if the given value is a key in this object"""
        key = self._map_key(key, raise_on_error=False)
        return key is not None

    def keys(self):
        """Returns the list of json properties in the object"""
        return self.__class__.rattribute_map.keys()

    def values(self):
        """Returns the list of values in the object"""
        for key in self.__class__.attribute_map.keys():
            yield getattr(self, key)

    def items(self):
        """Returns the list of json property to value mapping"""
        for key, prop in self.__class__.rattribute_map.items():
            yield key, getattr(self, prop)

    def get(self, key, default=None):
        """Get the value of the provided json property, or default"""
        key = self._map_key(key, raise_on_error=False)
        if key:
            return getattr(self, key, default)
        return default

    def _map_key(self, key, raise_on_error=True):
        result = self.__class__.rattribute_map.get(key)
        if result is None:
            if raise_on_error:
                raise AttributeError('Invalid attribute name: {}'.format(key))
            return None
        return '_' + result
