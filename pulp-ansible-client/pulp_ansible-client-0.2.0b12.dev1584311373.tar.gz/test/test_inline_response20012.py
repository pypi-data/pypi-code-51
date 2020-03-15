# coding: utf-8

"""
    Pulp 3 API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pulpcore.client.pulp_ansible
from pulpcore.client.pulp_ansible.models.inline_response20012 import InlineResponse20012  # noqa: E501
from pulpcore.client.pulp_ansible.rest import ApiException

class TestInlineResponse20012(unittest.TestCase):
    """InlineResponse20012 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20012
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulp_ansible.models.inline_response20012.InlineResponse20012()  # noqa: E501
        if include_optional :
            return InlineResponse20012(
                count = 56, 
                next = '0', 
                previous = '0', 
                results = [
                    pulpcore.client.pulp_ansible.models.galaxy_collection_version.GalaxyCollectionVersion(
                        version = '0', 
                        href = '0', 
                        namespace = '0', 
                        collection = '0', 
                        artifact = '0', 
                        metadata = pulpcore.client.pulp_ansible.models.metadata.Metadata(
                            authors = [
                                '0'
                                ], 
                            contents = pulpcore.client.pulp_ansible.models.contents.Contents(), 
                            dependencies = pulpcore.client.pulp_ansible.models.dependencies.Dependencies(), 
                            description = '0', 
                            documentation = '0', 
                            homepage = '0', 
                            issues = '0', 
                            license = [
                                '0'
                                ], 
                            repository = '0', 
                            tags = [
                                '0'
                                ], ), )
                    ]
            )
        else :
            return InlineResponse20012(
                count = 56,
                results = [
                    pulpcore.client.pulp_ansible.models.galaxy_collection_version.GalaxyCollectionVersion(
                        version = '0', 
                        href = '0', 
                        namespace = '0', 
                        collection = '0', 
                        artifact = '0', 
                        metadata = pulpcore.client.pulp_ansible.models.metadata.Metadata(
                            authors = [
                                '0'
                                ], 
                            contents = pulpcore.client.pulp_ansible.models.contents.Contents(), 
                            dependencies = pulpcore.client.pulp_ansible.models.dependencies.Dependencies(), 
                            description = '0', 
                            documentation = '0', 
                            homepage = '0', 
                            issues = '0', 
                            license = [
                                '0'
                                ], 
                            repository = '0', 
                            tags = [
                                '0'
                                ], ), )
                    ],
        )

    def testInlineResponse20012(self):
        """Test InlineResponse20012"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
