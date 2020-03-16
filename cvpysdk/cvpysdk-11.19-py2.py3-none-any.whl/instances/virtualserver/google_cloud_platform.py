# -*- coding: utf-8 -*-

# --------------------------------------------------------------------------
# Copyright Commvault Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# --------------------------------------------------------------------------

"""File for operating on a Virtual Server Amazon Instance.

GoogleCloudInstance is the only class defined in this file.

GoogleCloudInstance: Derived class from VirtualServer  Base class, representing a
                    Google Cloud Platform instance, and to perform operations on that instance

GoogleCloudInstance:
    __init__(agent_object,instance_name,instance_id)    --  initialize object of Google Cloud
                                                            Platform Instance object associated
                                                            with the VirtualServer Instance

"""

from ..vsinstance import VirtualServerInstance
from ...exception import SDKException
from ...instance import Instance


class GoogleCloudInstance(VirtualServerInstance):
    def __init__(self, agent, name, iid):
        self._vendor_id = 16
        self._server_name = []
        super(GoogleCloudInstance, self).__init__(agent, name, iid)

    def _get_instance_properties(self):
        """
        Get the properties of this instance

        Raise:
            SDK Exception:
                if response is not empty
                if response is not success
        """

        super(GoogleCloudInstance, self)._get_instance_properties()
        self._server_name = []
        if 'virtualServerInstance' in self._properties:
            _member_servers = self._properties["virtualServerInstance"] \
                ["associatedClients"]["memberServers"]
            for _each_client in _member_servers:
                client = _each_client['client']
                if 'clientName' in client.keys():
                    self._server_name.append(str(client['clientName']))

    def _get_instance_properties_json(self):
        """get the all instance related properties of this subclient.

           Returns:
                dict - all instance properties put inside a dict

        """
        instance_json = {
            "instanceProperties": {
                "isDeleted": False,
                "instance": self._instance,
                "instanceActivityControl": self._instanceActivityControl,
                "virtualServerInstance": {
                    "vsInstanceType": self._virtualserverinstance['vsInstanceType'],
                    "associatedClients": self._virtualserverinstance['associatedClients'],
                    "vmwareVendor": self._virtualserverinstance['vmwareVendor']
                }
            }
        }

        return instance_json

    @property
    def server_name(self):
        """getter for the domain name in the Google Cloud vendor json"""
        return self._server_name

    @property
    def server_host_name(self):
        """getter for the domain name in the Google CLoyd vendor json"""
        return self._server_name
