# coding: utf-8

"""
    Nomad Envoy

    This is the API descriptor for the Nomad Envoy API, responsible for order creation and product lists.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: paul@samarkand.global
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import nomad_envoy_cli
from nomad_envoy_cli.api.product_api import ProductApi  # noqa: E501
from nomad_envoy_cli.rest import ApiException


class TestProductApi(unittest.TestCase):
    """ProductApi unit test stubs"""

    def setUp(self):
        self.api = nomad_envoy_cli.api.product_api.ProductApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_product(self):
        """Test case for add_product

        addProduct  # noqa: E501
        """
        pass

    def test_delete_product(self):
        """Test case for delete_product

        deleteProduct  # noqa: E501
        """
        pass

    def test_get_products_by_field(self):
        """Test case for get_products_by_field

        getProductsByField  # noqa: E501
        """
        pass

    def test_update_product(self):
        """Test case for update_product

        updateProduct  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
