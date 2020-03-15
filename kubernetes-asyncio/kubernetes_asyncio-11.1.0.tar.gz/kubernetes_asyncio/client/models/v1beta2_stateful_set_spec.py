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


class V1beta2StatefulSetSpec(object):
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
        'pod_management_policy': 'str',
        'replicas': 'int',
        'revision_history_limit': 'int',
        'selector': 'V1LabelSelector',
        'service_name': 'str',
        'template': 'V1PodTemplateSpec',
        'update_strategy': 'V1beta2StatefulSetUpdateStrategy',
        'volume_claim_templates': 'list[V1PersistentVolumeClaim]'
    }

    attribute_map = {
        'pod_management_policy': 'podManagementPolicy',
        'replicas': 'replicas',
        'revision_history_limit': 'revisionHistoryLimit',
        'selector': 'selector',
        'service_name': 'serviceName',
        'template': 'template',
        'update_strategy': 'updateStrategy',
        'volume_claim_templates': 'volumeClaimTemplates'
    }

    def __init__(self, pod_management_policy=None, replicas=None, revision_history_limit=None, selector=None, service_name=None, template=None, update_strategy=None, volume_claim_templates=None, local_vars_configuration=None):  # noqa: E501
        """V1beta2StatefulSetSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pod_management_policy = None
        self._replicas = None
        self._revision_history_limit = None
        self._selector = None
        self._service_name = None
        self._template = None
        self._update_strategy = None
        self._volume_claim_templates = None
        self.discriminator = None

        if pod_management_policy is not None:
            self.pod_management_policy = pod_management_policy
        if replicas is not None:
            self.replicas = replicas
        if revision_history_limit is not None:
            self.revision_history_limit = revision_history_limit
        self.selector = selector
        self.service_name = service_name
        self.template = template
        if update_strategy is not None:
            self.update_strategy = update_strategy
        if volume_claim_templates is not None:
            self.volume_claim_templates = volume_claim_templates

    @property
    def pod_management_policy(self):
        """Gets the pod_management_policy of this V1beta2StatefulSetSpec.  # noqa: E501

        podManagementPolicy controls how pods are created during initial scale up, when replacing pods on nodes, or when scaling down. The default policy is `OrderedReady`, where pods are created in increasing order (pod-0, then pod-1, etc) and the controller will wait until each pod is ready before continuing. When scaling down, the pods are removed in the opposite order. The alternative policy is `Parallel` which will create pods in parallel to match the desired scale without waiting, and on scale down will delete all pods at once.  # noqa: E501

        :return: The pod_management_policy of this V1beta2StatefulSetSpec.  # noqa: E501
        :rtype: str
        """
        return self._pod_management_policy

    @pod_management_policy.setter
    def pod_management_policy(self, pod_management_policy):
        """Sets the pod_management_policy of this V1beta2StatefulSetSpec.

        podManagementPolicy controls how pods are created during initial scale up, when replacing pods on nodes, or when scaling down. The default policy is `OrderedReady`, where pods are created in increasing order (pod-0, then pod-1, etc) and the controller will wait until each pod is ready before continuing. When scaling down, the pods are removed in the opposite order. The alternative policy is `Parallel` which will create pods in parallel to match the desired scale without waiting, and on scale down will delete all pods at once.  # noqa: E501

        :param pod_management_policy: The pod_management_policy of this V1beta2StatefulSetSpec.  # noqa: E501
        :type: str
        """

        self._pod_management_policy = pod_management_policy

    @property
    def replicas(self):
        """Gets the replicas of this V1beta2StatefulSetSpec.  # noqa: E501

        replicas is the desired number of replicas of the given Template. These are replicas in the sense that they are instantiations of the same Template, but individual replicas also have a consistent identity. If unspecified, defaults to 1.  # noqa: E501

        :return: The replicas of this V1beta2StatefulSetSpec.  # noqa: E501
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """Sets the replicas of this V1beta2StatefulSetSpec.

        replicas is the desired number of replicas of the given Template. These are replicas in the sense that they are instantiations of the same Template, but individual replicas also have a consistent identity. If unspecified, defaults to 1.  # noqa: E501

        :param replicas: The replicas of this V1beta2StatefulSetSpec.  # noqa: E501
        :type: int
        """

        self._replicas = replicas

    @property
    def revision_history_limit(self):
        """Gets the revision_history_limit of this V1beta2StatefulSetSpec.  # noqa: E501

        revisionHistoryLimit is the maximum number of revisions that will be maintained in the StatefulSet's revision history. The revision history consists of all revisions not represented by a currently applied StatefulSetSpec version. The default value is 10.  # noqa: E501

        :return: The revision_history_limit of this V1beta2StatefulSetSpec.  # noqa: E501
        :rtype: int
        """
        return self._revision_history_limit

    @revision_history_limit.setter
    def revision_history_limit(self, revision_history_limit):
        """Sets the revision_history_limit of this V1beta2StatefulSetSpec.

        revisionHistoryLimit is the maximum number of revisions that will be maintained in the StatefulSet's revision history. The revision history consists of all revisions not represented by a currently applied StatefulSetSpec version. The default value is 10.  # noqa: E501

        :param revision_history_limit: The revision_history_limit of this V1beta2StatefulSetSpec.  # noqa: E501
        :type: int
        """

        self._revision_history_limit = revision_history_limit

    @property
    def selector(self):
        """Gets the selector of this V1beta2StatefulSetSpec.  # noqa: E501


        :return: The selector of this V1beta2StatefulSetSpec.  # noqa: E501
        :rtype: V1LabelSelector
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """Sets the selector of this V1beta2StatefulSetSpec.


        :param selector: The selector of this V1beta2StatefulSetSpec.  # noqa: E501
        :type: V1LabelSelector
        """
        if self.local_vars_configuration.client_side_validation and selector is None:  # noqa: E501
            raise ValueError("Invalid value for `selector`, must not be `None`")  # noqa: E501

        self._selector = selector

    @property
    def service_name(self):
        """Gets the service_name of this V1beta2StatefulSetSpec.  # noqa: E501

        serviceName is the name of the service that governs this StatefulSet. This service must exist before the StatefulSet, and is responsible for the network identity of the set. Pods get DNS/hostnames that follow the pattern: pod-specific-string.serviceName.default.svc.cluster.local where \"pod-specific-string\" is managed by the StatefulSet controller.  # noqa: E501

        :return: The service_name of this V1beta2StatefulSetSpec.  # noqa: E501
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this V1beta2StatefulSetSpec.

        serviceName is the name of the service that governs this StatefulSet. This service must exist before the StatefulSet, and is responsible for the network identity of the set. Pods get DNS/hostnames that follow the pattern: pod-specific-string.serviceName.default.svc.cluster.local where \"pod-specific-string\" is managed by the StatefulSet controller.  # noqa: E501

        :param service_name: The service_name of this V1beta2StatefulSetSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and service_name is None:  # noqa: E501
            raise ValueError("Invalid value for `service_name`, must not be `None`")  # noqa: E501

        self._service_name = service_name

    @property
    def template(self):
        """Gets the template of this V1beta2StatefulSetSpec.  # noqa: E501


        :return: The template of this V1beta2StatefulSetSpec.  # noqa: E501
        :rtype: V1PodTemplateSpec
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this V1beta2StatefulSetSpec.


        :param template: The template of this V1beta2StatefulSetSpec.  # noqa: E501
        :type: V1PodTemplateSpec
        """
        if self.local_vars_configuration.client_side_validation and template is None:  # noqa: E501
            raise ValueError("Invalid value for `template`, must not be `None`")  # noqa: E501

        self._template = template

    @property
    def update_strategy(self):
        """Gets the update_strategy of this V1beta2StatefulSetSpec.  # noqa: E501


        :return: The update_strategy of this V1beta2StatefulSetSpec.  # noqa: E501
        :rtype: V1beta2StatefulSetUpdateStrategy
        """
        return self._update_strategy

    @update_strategy.setter
    def update_strategy(self, update_strategy):
        """Sets the update_strategy of this V1beta2StatefulSetSpec.


        :param update_strategy: The update_strategy of this V1beta2StatefulSetSpec.  # noqa: E501
        :type: V1beta2StatefulSetUpdateStrategy
        """

        self._update_strategy = update_strategy

    @property
    def volume_claim_templates(self):
        """Gets the volume_claim_templates of this V1beta2StatefulSetSpec.  # noqa: E501

        volumeClaimTemplates is a list of claims that pods are allowed to reference. The StatefulSet controller is responsible for mapping network identities to claims in a way that maintains the identity of a pod. Every claim in this list must have at least one matching (by name) volumeMount in one container in the template. A claim in this list takes precedence over any volumes in the template, with the same name.  # noqa: E501

        :return: The volume_claim_templates of this V1beta2StatefulSetSpec.  # noqa: E501
        :rtype: list[V1PersistentVolumeClaim]
        """
        return self._volume_claim_templates

    @volume_claim_templates.setter
    def volume_claim_templates(self, volume_claim_templates):
        """Sets the volume_claim_templates of this V1beta2StatefulSetSpec.

        volumeClaimTemplates is a list of claims that pods are allowed to reference. The StatefulSet controller is responsible for mapping network identities to claims in a way that maintains the identity of a pod. Every claim in this list must have at least one matching (by name) volumeMount in one container in the template. A claim in this list takes precedence over any volumes in the template, with the same name.  # noqa: E501

        :param volume_claim_templates: The volume_claim_templates of this V1beta2StatefulSetSpec.  # noqa: E501
        :type: list[V1PersistentVolumeClaim]
        """

        self._volume_claim_templates = volume_claim_templates

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
        if not isinstance(other, V1beta2StatefulSetSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta2StatefulSetSpec):
            return True

        return self.to_dict() != other.to_dict()
