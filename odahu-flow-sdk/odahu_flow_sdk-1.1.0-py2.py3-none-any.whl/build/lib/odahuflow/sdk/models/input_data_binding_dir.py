# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from odahuflow.sdk.models.base_model_ import Model
from odahuflow.sdk.models.connection_spec import ConnectionSpec  # noqa: F401,E501
from odahuflow.sdk.models import util


class InputDataBindingDir(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, data_binding: ConnectionSpec=None, local_path: str=None, remote_path: str=None):  # noqa: E501
        """InputDataBindingDir - a model defined in Swagger

        :param data_binding: The data_binding of this InputDataBindingDir.  # noqa: E501
        :type data_binding: ConnectionSpec
        :param local_path: The local_path of this InputDataBindingDir.  # noqa: E501
        :type local_path: str
        :param remote_path: The remote_path of this InputDataBindingDir.  # noqa: E501
        :type remote_path: str
        """
        self.swagger_types = {
            'data_binding': ConnectionSpec,
            'local_path': str,
            'remote_path': str
        }

        self.attribute_map = {
            'data_binding': 'dataBinding',
            'local_path': 'localPath',
            'remote_path': 'remotePath'
        }

        self._data_binding = data_binding
        self._local_path = local_path
        self._remote_path = remote_path

    @classmethod
    def from_dict(cls, dikt) -> 'InputDataBindingDir':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InputDataBindingDir of this InputDataBindingDir.  # noqa: E501
        :rtype: InputDataBindingDir
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data_binding(self) -> ConnectionSpec:
        """Gets the data_binding of this InputDataBindingDir.

        Connection specific for data  # noqa: E501

        :return: The data_binding of this InputDataBindingDir.
        :rtype: ConnectionSpec
        """
        return self._data_binding

    @data_binding.setter
    def data_binding(self, data_binding: ConnectionSpec):
        """Sets the data_binding of this InputDataBindingDir.

        Connection specific for data  # noqa: E501

        :param data_binding: The data_binding of this InputDataBindingDir.
        :type data_binding: ConnectionSpec
        """

        self._data_binding = data_binding

    @property
    def local_path(self) -> str:
        """Gets the local_path of this InputDataBindingDir.

        Local path  # noqa: E501

        :return: The local_path of this InputDataBindingDir.
        :rtype: str
        """
        return self._local_path

    @local_path.setter
    def local_path(self, local_path: str):
        """Sets the local_path of this InputDataBindingDir.

        Local path  # noqa: E501

        :param local_path: The local_path of this InputDataBindingDir.
        :type local_path: str
        """

        self._local_path = local_path

    @property
    def remote_path(self) -> str:
        """Gets the remote_path of this InputDataBindingDir.

        Remote path  # noqa: E501

        :return: The remote_path of this InputDataBindingDir.
        :rtype: str
        """
        return self._remote_path

    @remote_path.setter
    def remote_path(self, remote_path: str):
        """Sets the remote_path of this InputDataBindingDir.

        Remote path  # noqa: E501

        :param remote_path: The remote_path of this InputDataBindingDir.
        :type remote_path: str
        """

        self._remote_path = remote_path
