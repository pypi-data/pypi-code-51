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


class ServiceInformation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, build_branch=None, build_branch_deployed_date_time=None, build_sha=None, build_version=None, linked_sites=None, service_versions=None):
        """
        ServiceInformation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'build_branch': 'str',
            'build_branch_deployed_date_time': 'str',
            'build_sha': 'str',
            'build_version': 'str',
            'linked_sites': 'list[str]',
            'service_versions': 'list[ServiceVersion]'
        }

        self.attribute_map = {
            'build_branch': 'buildBranch',
            'build_branch_deployed_date_time': 'buildBranchDeployedDateTime',
            'build_sha': 'buildSHA',
            'build_version': 'buildVersion',
            'linked_sites': 'linkedSites',
            'service_versions': 'serviceVersions'
        }

        self._build_branch = build_branch
        self._build_branch_deployed_date_time = build_branch_deployed_date_time
        self._build_sha = build_sha
        self._build_version = build_version
        self._linked_sites = linked_sites
        self._service_versions = service_versions

    @property
    def build_branch(self):
        """
        Gets the build_branch of this ServiceInformation.
        Reserved: TBD

        :return: The build_branch of this ServiceInformation.
        :rtype: str
        """
        return self._build_branch

    @build_branch.setter
    def build_branch(self, build_branch):
        """
        Sets the build_branch of this ServiceInformation.
        Reserved: TBD

        :param build_branch: The build_branch of this ServiceInformation.
        :type: str
        """

        self._build_branch = build_branch

    @property
    def build_branch_deployed_date_time(self):
        """
        Gets the build_branch_deployed_date_time of this ServiceInformation.
        Reserved: TBD

        :return: The build_branch_deployed_date_time of this ServiceInformation.
        :rtype: str
        """
        return self._build_branch_deployed_date_time

    @build_branch_deployed_date_time.setter
    def build_branch_deployed_date_time(self, build_branch_deployed_date_time):
        """
        Sets the build_branch_deployed_date_time of this ServiceInformation.
        Reserved: TBD

        :param build_branch_deployed_date_time: The build_branch_deployed_date_time of this ServiceInformation.
        :type: str
        """

        self._build_branch_deployed_date_time = build_branch_deployed_date_time

    @property
    def build_sha(self):
        """
        Gets the build_sha of this ServiceInformation.
        Reserved: TBD

        :return: The build_sha of this ServiceInformation.
        :rtype: str
        """
        return self._build_sha

    @build_sha.setter
    def build_sha(self, build_sha):
        """
        Sets the build_sha of this ServiceInformation.
        Reserved: TBD

        :param build_sha: The build_sha of this ServiceInformation.
        :type: str
        """

        self._build_sha = build_sha

    @property
    def build_version(self):
        """
        Gets the build_version of this ServiceInformation.
        Reserved: TBD

        :return: The build_version of this ServiceInformation.
        :rtype: str
        """
        return self._build_version

    @build_version.setter
    def build_version(self, build_version):
        """
        Sets the build_version of this ServiceInformation.
        Reserved: TBD

        :param build_version: The build_version of this ServiceInformation.
        :type: str
        """

        self._build_version = build_version

    @property
    def linked_sites(self):
        """
        Gets the linked_sites of this ServiceInformation.
        

        :return: The linked_sites of this ServiceInformation.
        :rtype: list[str]
        """
        return self._linked_sites

    @linked_sites.setter
    def linked_sites(self, linked_sites):
        """
        Sets the linked_sites of this ServiceInformation.
        

        :param linked_sites: The linked_sites of this ServiceInformation.
        :type: list[str]
        """

        self._linked_sites = linked_sites

    @property
    def service_versions(self):
        """
        Gets the service_versions of this ServiceInformation.
        

        :return: The service_versions of this ServiceInformation.
        :rtype: list[ServiceVersion]
        """
        return self._service_versions

    @service_versions.setter
    def service_versions(self, service_versions):
        """
        Sets the service_versions of this ServiceInformation.
        

        :param service_versions: The service_versions of this ServiceInformation.
        :type: list[ServiceVersion]
        """

        self._service_versions = service_versions

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
