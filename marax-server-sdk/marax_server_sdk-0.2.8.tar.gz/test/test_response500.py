# coding: utf-8

"""
    marax-server-sdk

    Marax Server SDK to send transactional events from client server to marax server  # noqa: E501

    The version of the OpenAPI document: 0.2.0
    Contact: team@marax.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import marax_server_sdk
from marax_server_sdk.models.response500 import Response500  # noqa: E501
from marax_server_sdk.rest import ApiException

class TestResponse500(unittest.TestCase):
    """Response500 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Response500
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = marax_server_sdk.models.response500.Response500()  # noqa: E501
        if include_optional :
            return Response500(
                status = 'error', 
                message = 'Internal Server Error'
            )
        else :
            return Response500(
        )

    def testResponse500(self):
        """Test Response500"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
