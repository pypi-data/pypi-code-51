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

import pulpcore.client.pulp_file
from pulpcore.client.pulp_file.models.file_file_content import FileFileContent  # noqa: E501
from pulpcore.client.pulp_file.rest import ApiException

class TestFileFileContent(unittest.TestCase):
    """FileFileContent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FileFileContent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulp_file.models.file_file_content.FileFileContent()  # noqa: E501
        if include_optional :
            return FileFileContent(
                pulp_href = '0', 
                pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                artifact = '0', 
                relative_path = '0', 
                md5 = '0', 
                sha1 = '0', 
                sha224 = '0', 
                sha256 = '0', 
                sha384 = '0', 
                sha512 = '0'
            )
        else :
            return FileFileContent(
                relative_path = '0',
        )

    def testFileFileContent(self):
        """Test FileFileContent"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
