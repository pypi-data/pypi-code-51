# coding: utf-8

"""
    Nomad Envoy

    This is the API descriptor for the Nomad Envoy API, responsible for order creation and product lists.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: paul@samarkand.global
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ProductSku(object):
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
        'sku_number': 'str',
        'price': 'float',
        'rrp': 'float',
        'group_buying_price': 'float',
        'images': 'Images',
        'barcode': 'str',
        'color': 'str',
        'size': 'str',
        'quantity': 'int',
        'is_onsale': 'bool',
        'net_weight': 'float',
        'gross_weight': 'float',
        'shipping_cost': 'float',
        'shipping_time': 'int',
        'model': 'str',
        'spec': 'str',
        'customs_unit_code': 'str',
        'customs_unit_code_package': 'str',
        'customs_unit_code_weight': 'str'
    }

    attribute_map = {
        'sku_number': 'skuNumber',
        'price': 'price',
        'rrp': 'rrp',
        'group_buying_price': 'groupBuyingPrice',
        'images': 'images',
        'barcode': 'barcode',
        'color': 'color',
        'size': 'size',
        'quantity': 'quantity',
        'is_onsale': 'isOnsale',
        'net_weight': 'netWeight',
        'gross_weight': 'grossWeight',
        'shipping_cost': 'shippingCost',
        'shipping_time': 'shippingTime',
        'model': 'model',
        'spec': 'spec',
        'customs_unit_code': 'customsUnitCode',
        'customs_unit_code_package': 'customsUnitCodePackage',
        'customs_unit_code_weight': 'customsUnitCodeWeight'
    }

    def __init__(self, sku_number=None, price=None, rrp=None, group_buying_price=None, images=None, barcode=None, color=None, size=None, quantity=None, is_onsale=None, net_weight=None, gross_weight=None, shipping_cost=None, shipping_time=None, model=None, spec=None, customs_unit_code=None, customs_unit_code_package=None, customs_unit_code_weight='035'):  # noqa: E501
        """ProductSku - a model defined in OpenAPI"""  # noqa: E501

        self._sku_number = None
        self._price = None
        self._rrp = None
        self._group_buying_price = None
        self._images = None
        self._barcode = None
        self._color = None
        self._size = None
        self._quantity = None
        self._is_onsale = None
        self._net_weight = None
        self._gross_weight = None
        self._shipping_cost = None
        self._shipping_time = None
        self._model = None
        self._spec = None
        self._customs_unit_code = None
        self._customs_unit_code_package = None
        self._customs_unit_code_weight = None
        self.discriminator = None

        if sku_number is not None:
            self.sku_number = sku_number
        if price is not None:
            self.price = price
        if rrp is not None:
            self.rrp = rrp
        if group_buying_price is not None:
            self.group_buying_price = group_buying_price
        if images is not None:
            self.images = images
        if barcode is not None:
            self.barcode = barcode
        if color is not None:
            self.color = color
        if size is not None:
            self.size = size
        if quantity is not None:
            self.quantity = quantity
        if is_onsale is not None:
            self.is_onsale = is_onsale
        if net_weight is not None:
            self.net_weight = net_weight
        if gross_weight is not None:
            self.gross_weight = gross_weight
        if shipping_cost is not None:
            self.shipping_cost = shipping_cost
        if shipping_time is not None:
            self.shipping_time = shipping_time
        if model is not None:
            self.model = model
        if spec is not None:
            self.spec = spec
        if customs_unit_code is not None:
            self.customs_unit_code = customs_unit_code
        if customs_unit_code_package is not None:
            self.customs_unit_code_package = customs_unit_code_package
        if customs_unit_code_weight is not None:
            self.customs_unit_code_weight = customs_unit_code_weight

    @property
    def sku_number(self):
        """Gets the sku_number of this ProductSku.  # noqa: E501


        :return: The sku_number of this ProductSku.  # noqa: E501
        :rtype: str
        """
        return self._sku_number

    @sku_number.setter
    def sku_number(self, sku_number):
        """Sets the sku_number of this ProductSku.


        :param sku_number: The sku_number of this ProductSku.  # noqa: E501
        :type: str
        """

        self._sku_number = sku_number

    @property
    def price(self):
        """Gets the price of this ProductSku.  # noqa: E501

        The selling price of current SKU.  # noqa: E501

        :return: The price of this ProductSku.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this ProductSku.

        The selling price of current SKU.  # noqa: E501

        :param price: The price of this ProductSku.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def rrp(self):
        """Gets the rrp of this ProductSku.  # noqa: E501

        recommended retail price  # noqa: E501

        :return: The rrp of this ProductSku.  # noqa: E501
        :rtype: float
        """
        return self._rrp

    @rrp.setter
    def rrp(self, rrp):
        """Sets the rrp of this ProductSku.

        recommended retail price  # noqa: E501

        :param rrp: The rrp of this ProductSku.  # noqa: E501
        :type: float
        """

        self._rrp = rrp

    @property
    def group_buying_price(self):
        """Gets the group_buying_price of this ProductSku.  # noqa: E501

        group buying price  # noqa: E501

        :return: The group_buying_price of this ProductSku.  # noqa: E501
        :rtype: float
        """
        return self._group_buying_price

    @group_buying_price.setter
    def group_buying_price(self, group_buying_price):
        """Sets the group_buying_price of this ProductSku.

        group buying price  # noqa: E501

        :param group_buying_price: The group_buying_price of this ProductSku.  # noqa: E501
        :type: float
        """

        self._group_buying_price = group_buying_price

    @property
    def images(self):
        """Gets the images of this ProductSku.  # noqa: E501


        :return: The images of this ProductSku.  # noqa: E501
        :rtype: Images
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this ProductSku.


        :param images: The images of this ProductSku.  # noqa: E501
        :type: Images
        """

        self._images = images

    @property
    def barcode(self):
        """Gets the barcode of this ProductSku.  # noqa: E501


        :return: The barcode of this ProductSku.  # noqa: E501
        :rtype: str
        """
        return self._barcode

    @barcode.setter
    def barcode(self, barcode):
        """Sets the barcode of this ProductSku.


        :param barcode: The barcode of this ProductSku.  # noqa: E501
        :type: str
        """

        self._barcode = barcode

    @property
    def color(self):
        """Gets the color of this ProductSku.  # noqa: E501


        :return: The color of this ProductSku.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this ProductSku.


        :param color: The color of this ProductSku.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def size(self):
        """Gets the size of this ProductSku.  # noqa: E501


        :return: The size of this ProductSku.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ProductSku.


        :param size: The size of this ProductSku.  # noqa: E501
        :type: str
        """

        self._size = size

    @property
    def quantity(self):
        """Gets the quantity of this ProductSku.  # noqa: E501

        The stock level of current SKU in current product.  # noqa: E501

        :return: The quantity of this ProductSku.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this ProductSku.

        The stock level of current SKU in current product.  # noqa: E501

        :param quantity: The quantity of this ProductSku.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

    @property
    def is_onsale(self):
        """Gets the is_onsale of this ProductSku.  # noqa: E501


        :return: The is_onsale of this ProductSku.  # noqa: E501
        :rtype: bool
        """
        return self._is_onsale

    @is_onsale.setter
    def is_onsale(self, is_onsale):
        """Sets the is_onsale of this ProductSku.


        :param is_onsale: The is_onsale of this ProductSku.  # noqa: E501
        :type: bool
        """

        self._is_onsale = is_onsale

    @property
    def net_weight(self):
        """Gets the net_weight of this ProductSku.  # noqa: E501

        The default net weight of current SKU. If not present, then switch back to the default value of product  # noqa: E501

        :return: The net_weight of this ProductSku.  # noqa: E501
        :rtype: float
        """
        return self._net_weight

    @net_weight.setter
    def net_weight(self, net_weight):
        """Sets the net_weight of this ProductSku.

        The default net weight of current SKU. If not present, then switch back to the default value of product  # noqa: E501

        :param net_weight: The net_weight of this ProductSku.  # noqa: E501
        :type: float
        """

        self._net_weight = net_weight

    @property
    def gross_weight(self):
        """Gets the gross_weight of this ProductSku.  # noqa: E501

        The default gross weight of current SKU. If not present, then switch back to the default value of product  # noqa: E501

        :return: The gross_weight of this ProductSku.  # noqa: E501
        :rtype: float
        """
        return self._gross_weight

    @gross_weight.setter
    def gross_weight(self, gross_weight):
        """Sets the gross_weight of this ProductSku.

        The default gross weight of current SKU. If not present, then switch back to the default value of product  # noqa: E501

        :param gross_weight: The gross_weight of this ProductSku.  # noqa: E501
        :type: float
        """

        self._gross_weight = gross_weight

    @property
    def shipping_cost(self):
        """Gets the shipping_cost of this ProductSku.  # noqa: E501

        The shipping cost of current SKU. Will overwrite product's.  # noqa: E501

        :return: The shipping_cost of this ProductSku.  # noqa: E501
        :rtype: float
        """
        return self._shipping_cost

    @shipping_cost.setter
    def shipping_cost(self, shipping_cost):
        """Sets the shipping_cost of this ProductSku.

        The shipping cost of current SKU. Will overwrite product's.  # noqa: E501

        :param shipping_cost: The shipping_cost of this ProductSku.  # noqa: E501
        :type: float
        """

        self._shipping_cost = shipping_cost

    @property
    def shipping_time(self):
        """Gets the shipping_time of this ProductSku.  # noqa: E501

        The days that take to ship and deliver to customer's door. Will overwrite product's.  # noqa: E501

        :return: The shipping_time of this ProductSku.  # noqa: E501
        :rtype: int
        """
        return self._shipping_time

    @shipping_time.setter
    def shipping_time(self, shipping_time):
        """Sets the shipping_time of this ProductSku.

        The days that take to ship and deliver to customer's door. Will overwrite product's.  # noqa: E501

        :param shipping_time: The shipping_time of this ProductSku.  # noqa: E501
        :type: int
        """

        self._shipping_time = shipping_time

    @property
    def model(self):
        """Gets the model of this ProductSku.  # noqa: E501

        The model of current sku.  # noqa: E501

        :return: The model of this ProductSku.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this ProductSku.

        The model of current sku.  # noqa: E501

        :param model: The model of this ProductSku.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def spec(self):
        """Gets the spec of this ProductSku.  # noqa: E501

        The spec of current sku.  # noqa: E501

        :return: The spec of this ProductSku.  # noqa: E501
        :rtype: str
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this ProductSku.

        The spec of current sku.  # noqa: E501

        :param spec: The spec of this ProductSku.  # noqa: E501
        :type: str
        """

        self._spec = spec

    @property
    def customs_unit_code(self):
        """Gets the customs_unit_code of this ProductSku.  # noqa: E501

        aka customsUnitCodeSKU. The quantity unit code of current sku for customs purpose. Both Chinese or number are ok.  # noqa: E501

        :return: The customs_unit_code of this ProductSku.  # noqa: E501
        :rtype: str
        """
        return self._customs_unit_code

    @customs_unit_code.setter
    def customs_unit_code(self, customs_unit_code):
        """Sets the customs_unit_code of this ProductSku.

        aka customsUnitCodeSKU. The quantity unit code of current sku for customs purpose. Both Chinese or number are ok.  # noqa: E501

        :param customs_unit_code: The customs_unit_code of this ProductSku.  # noqa: E501
        :type: str
        """

        self._customs_unit_code = customs_unit_code

    @property
    def customs_unit_code_package(self):
        """Gets the customs_unit_code_package of this ProductSku.  # noqa: E501

        The quantity unit code customs purpose. Declaration Unit, 申报单位.  # noqa: E501

        :return: The customs_unit_code_package of this ProductSku.  # noqa: E501
        :rtype: str
        """
        return self._customs_unit_code_package

    @customs_unit_code_package.setter
    def customs_unit_code_package(self, customs_unit_code_package):
        """Sets the customs_unit_code_package of this ProductSku.

        The quantity unit code customs purpose. Declaration Unit, 申报单位.  # noqa: E501

        :param customs_unit_code_package: The customs_unit_code_package of this ProductSku.  # noqa: E501
        :type: str
        """

        self._customs_unit_code_package = customs_unit_code_package

    @property
    def customs_unit_code_weight(self):
        """Gets the customs_unit_code_weight of this ProductSku.  # noqa: E501

        The weight unit code for customs purpose.  # noqa: E501

        :return: The customs_unit_code_weight of this ProductSku.  # noqa: E501
        :rtype: str
        """
        return self._customs_unit_code_weight

    @customs_unit_code_weight.setter
    def customs_unit_code_weight(self, customs_unit_code_weight):
        """Sets the customs_unit_code_weight of this ProductSku.

        The weight unit code for customs purpose.  # noqa: E501

        :param customs_unit_code_weight: The customs_unit_code_weight of this ProductSku.  # noqa: E501
        :type: str
        """

        self._customs_unit_code_weight = customs_unit_code_weight

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
        if not isinstance(other, ProductSku):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
