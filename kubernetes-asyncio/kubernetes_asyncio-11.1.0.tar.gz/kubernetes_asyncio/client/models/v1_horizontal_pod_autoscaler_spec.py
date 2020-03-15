# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.15.11
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes_asyncio.client.configuration import Configuration


class V1HorizontalPodAutoscalerSpec(object):
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
        'max_replicas': 'int',
        'min_replicas': 'int',
        'scale_target_ref': 'V1CrossVersionObjectReference',
        'target_cpu_utilization_percentage': 'int'
    }

    attribute_map = {
        'max_replicas': 'maxReplicas',
        'min_replicas': 'minReplicas',
        'scale_target_ref': 'scaleTargetRef',
        'target_cpu_utilization_percentage': 'targetCPUUtilizationPercentage'
    }

    def __init__(self, max_replicas=None, min_replicas=None, scale_target_ref=None, target_cpu_utilization_percentage=None, local_vars_configuration=None):  # noqa: E501
        """V1HorizontalPodAutoscalerSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._max_replicas = None
        self._min_replicas = None
        self._scale_target_ref = None
        self._target_cpu_utilization_percentage = None
        self.discriminator = None

        self.max_replicas = max_replicas
        if min_replicas is not None:
            self.min_replicas = min_replicas
        self.scale_target_ref = scale_target_ref
        if target_cpu_utilization_percentage is not None:
            self.target_cpu_utilization_percentage = target_cpu_utilization_percentage

    @property
    def max_replicas(self):
        """Gets the max_replicas of this V1HorizontalPodAutoscalerSpec.  # noqa: E501

        upper limit for the number of pods that can be set by the autoscaler; cannot be smaller than MinReplicas.  # noqa: E501

        :return: The max_replicas of this V1HorizontalPodAutoscalerSpec.  # noqa: E501
        :rtype: int
        """
        return self._max_replicas

    @max_replicas.setter
    def max_replicas(self, max_replicas):
        """Sets the max_replicas of this V1HorizontalPodAutoscalerSpec.

        upper limit for the number of pods that can be set by the autoscaler; cannot be smaller than MinReplicas.  # noqa: E501

        :param max_replicas: The max_replicas of this V1HorizontalPodAutoscalerSpec.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and max_replicas is None:  # noqa: E501
            raise ValueError("Invalid value for `max_replicas`, must not be `None`")  # noqa: E501

        self._max_replicas = max_replicas

    @property
    def min_replicas(self):
        """Gets the min_replicas of this V1HorizontalPodAutoscalerSpec.  # noqa: E501

        lower limit for the number of pods that can be set by the autoscaler, default 1.  # noqa: E501

        :return: The min_replicas of this V1HorizontalPodAutoscalerSpec.  # noqa: E501
        :rtype: int
        """
        return self._min_replicas

    @min_replicas.setter
    def min_replicas(self, min_replicas):
        """Sets the min_replicas of this V1HorizontalPodAutoscalerSpec.

        lower limit for the number of pods that can be set by the autoscaler, default 1.  # noqa: E501

        :param min_replicas: The min_replicas of this V1HorizontalPodAutoscalerSpec.  # noqa: E501
        :type: int
        """

        self._min_replicas = min_replicas

    @property
    def scale_target_ref(self):
        """Gets the scale_target_ref of this V1HorizontalPodAutoscalerSpec.  # noqa: E501


        :return: The scale_target_ref of this V1HorizontalPodAutoscalerSpec.  # noqa: E501
        :rtype: V1CrossVersionObjectReference
        """
        return self._scale_target_ref

    @scale_target_ref.setter
    def scale_target_ref(self, scale_target_ref):
        """Sets the scale_target_ref of this V1HorizontalPodAutoscalerSpec.


        :param scale_target_ref: The scale_target_ref of this V1HorizontalPodAutoscalerSpec.  # noqa: E501
        :type: V1CrossVersionObjectReference
        """
        if self.local_vars_configuration.client_side_validation and scale_target_ref is None:  # noqa: E501
            raise ValueError("Invalid value for `scale_target_ref`, must not be `None`")  # noqa: E501

        self._scale_target_ref = scale_target_ref

    @property
    def target_cpu_utilization_percentage(self):
        """Gets the target_cpu_utilization_percentage of this V1HorizontalPodAutoscalerSpec.  # noqa: E501

        target average CPU utilization (represented as a percentage of requested CPU) over all the pods; if not specified the default autoscaling policy will be used.  # noqa: E501

        :return: The target_cpu_utilization_percentage of this V1HorizontalPodAutoscalerSpec.  # noqa: E501
        :rtype: int
        """
        return self._target_cpu_utilization_percentage

    @target_cpu_utilization_percentage.setter
    def target_cpu_utilization_percentage(self, target_cpu_utilization_percentage):
        """Sets the target_cpu_utilization_percentage of this V1HorizontalPodAutoscalerSpec.

        target average CPU utilization (represented as a percentage of requested CPU) over all the pods; if not specified the default autoscaling policy will be used.  # noqa: E501

        :param target_cpu_utilization_percentage: The target_cpu_utilization_percentage of this V1HorizontalPodAutoscalerSpec.  # noqa: E501
        :type: int
        """

        self._target_cpu_utilization_percentage = target_cpu_utilization_percentage

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
        if not isinstance(other, V1HorizontalPodAutoscalerSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1HorizontalPodAutoscalerSpec):
            return True

        return self.to_dict() != other.to_dict()
