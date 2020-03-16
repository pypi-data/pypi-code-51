# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class Kubernetes(pulumi.CustomResource):
    availability_zone: pulumi.Output[str]
    """
    The Zone where new kubernetes cluster will be located. If it is not be specified, the `vswitch_ids` should be set, its value will be vswitch's zone.
    """
    client_cert: pulumi.Output[str]
    """
    The path of client certificate, like `~/.kube/client-cert.pem`.
    """
    client_key: pulumi.Output[str]
    """
    The path of client key, like `~/.kube/client-key.pem`.
    """
    cluster_ca_cert: pulumi.Output[str]
    """
    The path of cluster ca certificate, like `~/.kube/cluster-ca-cert.pem`
    """
    cluster_network_type: pulumi.Output[str]
    """
    The network that cluster uses, use `flannel` or `terway`.
    """
    connections: pulumi.Output[dict]
    """
    Map of kubernetes cluster connection information. It contains several attributes to `Block Connections`.

      * `api_server_internet` (`str`) - API Server Internet endpoint.
      * `api_server_intranet` (`str`) - API Server Intranet endpoint.
      * `master_public_ip` (`str`) - Master node SSH IP address.
      * `service_domain` (`str`) - Service Access Domain.
    """
    enable_ssh: pulumi.Output[bool]
    """
    Whether to allow to SSH login kubernetes. Default to false.
    """
    force_update: pulumi.Output[bool]
    """
    Whether to force the update of kubernetes cluster arguments. Default to false.
    """
    image_id: pulumi.Output[str]
    install_cloud_monitor: pulumi.Output[bool]
    """
    Whether to install cloud monitor for the kubernetes' node.
    """
    is_outdated: pulumi.Output[bool]
    """
    Whether to use outdated instance type. Default to false.
    """
    key_name: pulumi.Output[str]
    """
    The keypair of ssh login cluster node, you have to create it first.
    """
    kms_encrypted_password: pulumi.Output[str]
    """
    An KMS encrypts password used to a cs kubernetes. It is conflicted with `password` and `key_name`.
    """
    kms_encryption_context: pulumi.Output[dict]
    """
    An KMS encryption context used to decrypt `kms_encrypted_password` before creating or updating a cs kubernetes with `kms_encrypted_password`. See [Encryption Context](https://www.alibabacloud.com/help/doc-detail/42975.htm). It is valid when `kms_encrypted_password` is set.
    """
    kube_config: pulumi.Output[str]
    """
    The path of kube config, like `~/.kube/config`.
    """
    log_config: pulumi.Output[dict]
    """
    A list of one element containing information about the associated log store. It contains the following attributes:

      * `project` (`str`) - Log Service project name, cluster logs will output to this project.
      * `type` (`str`) - Type of collecting logs, only `SLS` are supported currently.
    """
    master_auto_renew: pulumi.Output[bool]
    """
    Enable master payment auto-renew, defaults to false.
    """
    master_auto_renew_period: pulumi.Output[float]
    """
    Master payment auto-renew period. When period unit is `Month`, it can be one of {“1”, “2”, “3”, “6”, “12”}.  When period unit is `Week`, it can be one of {“1”, “2”, “3”}.
    """
    master_disk_category: pulumi.Output[str]
    """
    The system disk category of master node. Its valid value are `cloud_ssd` and `cloud_efficiency`. Default to `cloud_efficiency`.
    """
    master_disk_size: pulumi.Output[float]
    """
    The system disk size of master node. Its valid value range [20~500] in GB. Default to 20.
    """
    master_instance_charge_type: pulumi.Output[str]
    """
    Master payment type. `PrePaid` or `PostPaid`, defaults to `PostPaid`.
    """
    master_instance_type: pulumi.Output[str]
    """
    (Required, Force new resource) The instance type of master node.
    """
    master_instance_types: pulumi.Output[list]
    master_nodes: pulumi.Output[list]
    """
    List of cluster master nodes. It contains several attributes to `Block Nodes`.

      * `id` (`str`) - ID of the node.
      * `name` (`str`) - The kubernetes cluster's name. It is the only in one Alicloud account.
      * `private_ip` (`str`) - The private IP address of node.
    """
    master_period: pulumi.Output[float]
    """
    Master payment period. When period unit is `Month`, it can be one of { “1”, “2”, “3”, “4”, “5”, “6”, “7”, “8”, “9”, “12”, “24”, “36”,”48”,”60”}.  When period unit is `Week`, it can be one of {“1”, “2”, “3”, “4”}.
    """
    master_period_unit: pulumi.Output[str]
    """
    Master payment period unit. `Month` or `Week`, defaults to `Month`.
    """
    name: pulumi.Output[str]
    """
    The kubernetes cluster's name. It is the only in one Alicloud account.
    """
    name_prefix: pulumi.Output[str]
    nat_gateway_id: pulumi.Output[str]
    """
    The ID of nat gateway used to launch kubernetes cluster.
    """
    new_nat_gateway: pulumi.Output[bool]
    """
    Whether to create a new nat gateway while creating kubernetes cluster. Default to true.
    """
    node_cidr_mask: pulumi.Output[float]
    """
    The network mask used on pods for each node, ranging from `24` to `28`.
    Larger this number is, less pods can be allocated on each node. Default value is `24`, means you can allocate 256 pods on each node.
    """
    nodes: pulumi.Output[list]
    password: pulumi.Output[str]
    """
    The password of ssh login cluster node. You have to specify one of `password` `key_name` `kms_encrypted_password` fields.
    """
    pod_cidr: pulumi.Output[str]
    """
    The CIDR block for the pod network. It will be allocated automatically when `vswitch_ids` is not specified.
    It cannot be duplicated with the VPC CIDR and CIDR used by Kubernetes cluster in VPC, cannot be modified after creation.
    Maximum number of hosts allowed in the cluster: 256. Refer to [Plan Kubernetes CIDR blocks under VPC](https://www.alibabacloud.com/help/doc-detail/64530.htm).
    """
    security_group_id: pulumi.Output[str]
    """
    The ID of security group where the current cluster worker node is located.
    """
    service_cidr: pulumi.Output[str]
    """
    The CIDR block for the service network. 
    It cannot be duplicated with the VPC CIDR and CIDR used by Kubernetes cluster in VPC, cannot be modified after creation.
    """
    slb_id: pulumi.Output[str]
    slb_internet: pulumi.Output[str]
    slb_internet_enabled: pulumi.Output[bool]
    """
    Whether to create internet load balancer for API Server. Default to true.
    """
    slb_intranet: pulumi.Output[str]
    """
    The ID of private load balancer where the current cluster master node is located.
    """
    user_ca: pulumi.Output[str]
    """
    The path of customized CA cert, you can use this CA to sign client certs to connect your cluster.
    """
    version: pulumi.Output[str]
    """
    Desired Kubernetes version. If you do not specify a value, the latest available version at resource creation is used and no upgrades will occur except you set a higher version number. The value must be configured and increased to upgrade the version when desired. Downgrades are not supported by ACK.
    """
    vpc_id: pulumi.Output[str]
    """
    The ID of VPC where the current cluster is located.
    """
    vswitch_id: pulumi.Output[str]
    """
    (Force new resource) The vswitch where new kubernetes cluster will be located. If it is not specified, a new VPC and VSwicth will be built. It must be in the zone which `availability_zone` specified.
    """
    vswitch_ids: pulumi.Output[list]
    """
    The vswitch where new kubernetes cluster will be located. Specify one or more vswitch's id. It must be in the zone which `availability_zone` specified.
    """
    worker_auto_renew: pulumi.Output[bool]
    """
    Enable worker payment auto-renew, defaults to false.
    """
    worker_auto_renew_period: pulumi.Output[float]
    """
    Worker payment auto-renew period. When period unit is `Month`, it can be one of {“1”, “2”, “3”, “6”, “12”}.  When period unit is `Week`, it can be one of {“1”, “2”, “3”}.
    """
    worker_data_disk_category: pulumi.Output[str]
    """
    The data disk category of worker node. Its valid value are `cloud_ssd` and `cloud_efficiency`, if not set, data disk will not be created.
    """
    worker_data_disk_size: pulumi.Output[float]
    """
    The data disk size of worker node. Its valid value range [20~32768] in GB. When `worker_data_disk_category` is presented, it defaults to 40.
    """
    worker_disk_category: pulumi.Output[str]
    """
    The system disk category of worker node. Its valid value are `cloud_ssd` and `cloud_efficiency`. Default to `cloud_efficiency`.
    """
    worker_disk_size: pulumi.Output[float]
    """
    The system disk size of worker node. Its valid value range [20~32768] in GB. Default to 20.
    """
    worker_instance_charge_type: pulumi.Output[str]
    """
    Worker payment type. `PrePaid` or `PostPaid`, defaults to `PostPaid`.
    """
    worker_instance_type: pulumi.Output[str]
    """
    (Required, Force new resource) The instance type of worker node.
    """
    worker_instance_types: pulumi.Output[list]
    worker_nodes: pulumi.Output[list]
    """
    List of cluster worker nodes. It contains several attributes to `Block Nodes`.

      * `id` (`str`) - ID of the node.
      * `name` (`str`) - The kubernetes cluster's name. It is the only in one Alicloud account.
      * `private_ip` (`str`) - The private IP address of node.
    """
    worker_number: pulumi.Output[float]
    """
    The worker node number of the kubernetes cluster. Default to 3. It is limited up to 50 and if you want to enlarge it, please apply white list or contact with us.
    """
    worker_numbers: pulumi.Output[list]
    worker_period: pulumi.Output[float]
    """
    Worker payment period. When period unit is `Month`, it can be one of { “1”, “2”, “3”, “4”, “5”, “6”, “7”, “8”, “9”, “12”, “24”, “36”,”48”,”60”}.  When period unit is `Week`, it can be one of {“1”, “2”, “3”, “4”}.
    """
    worker_period_unit: pulumi.Output[str]
    """
    Worker payment period unit. `Month` or `Week`, defaults to `Month`.
    """
    def __init__(__self__, resource_name, opts=None, availability_zone=None, client_cert=None, client_key=None, cluster_ca_cert=None, cluster_network_type=None, enable_ssh=None, force_update=None, image_id=None, install_cloud_monitor=None, is_outdated=None, key_name=None, kms_encrypted_password=None, kms_encryption_context=None, kube_config=None, log_config=None, master_auto_renew=None, master_auto_renew_period=None, master_disk_category=None, master_disk_size=None, master_instance_charge_type=None, master_instance_type=None, master_instance_types=None, master_period=None, master_period_unit=None, name=None, name_prefix=None, new_nat_gateway=None, node_cidr_mask=None, nodes=None, password=None, pod_cidr=None, service_cidr=None, slb_internet_enabled=None, user_ca=None, version=None, vswitch_id=None, vswitch_ids=None, worker_auto_renew=None, worker_auto_renew_period=None, worker_data_disk_category=None, worker_data_disk_size=None, worker_disk_category=None, worker_disk_size=None, worker_instance_charge_type=None, worker_instance_type=None, worker_instance_types=None, worker_number=None, worker_numbers=None, worker_period=None, worker_period_unit=None, __props__=None, __name__=None, __opts__=None):
        """
        Create a Kubernetes resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] availability_zone: The Zone where new kubernetes cluster will be located. If it is not be specified, the `vswitch_ids` should be set, its value will be vswitch's zone.
        :param pulumi.Input[str] client_cert: The path of client certificate, like `~/.kube/client-cert.pem`.
        :param pulumi.Input[str] client_key: The path of client key, like `~/.kube/client-key.pem`.
        :param pulumi.Input[str] cluster_ca_cert: The path of cluster ca certificate, like `~/.kube/cluster-ca-cert.pem`
        :param pulumi.Input[str] cluster_network_type: The network that cluster uses, use `flannel` or `terway`.
        :param pulumi.Input[bool] enable_ssh: Whether to allow to SSH login kubernetes. Default to false.
        :param pulumi.Input[bool] force_update: Whether to force the update of kubernetes cluster arguments. Default to false.
        :param pulumi.Input[bool] install_cloud_monitor: Whether to install cloud monitor for the kubernetes' node.
        :param pulumi.Input[bool] is_outdated: Whether to use outdated instance type. Default to false.
        :param pulumi.Input[str] key_name: The keypair of ssh login cluster node, you have to create it first.
        :param pulumi.Input[str] kms_encrypted_password: An KMS encrypts password used to a cs kubernetes. It is conflicted with `password` and `key_name`.
        :param pulumi.Input[dict] kms_encryption_context: An KMS encryption context used to decrypt `kms_encrypted_password` before creating or updating a cs kubernetes with `kms_encrypted_password`. See [Encryption Context](https://www.alibabacloud.com/help/doc-detail/42975.htm). It is valid when `kms_encrypted_password` is set.
        :param pulumi.Input[str] kube_config: The path of kube config, like `~/.kube/config`.
        :param pulumi.Input[dict] log_config: A list of one element containing information about the associated log store. It contains the following attributes:
        :param pulumi.Input[bool] master_auto_renew: Enable master payment auto-renew, defaults to false.
        :param pulumi.Input[float] master_auto_renew_period: Master payment auto-renew period. When period unit is `Month`, it can be one of {“1”, “2”, “3”, “6”, “12”}.  When period unit is `Week`, it can be one of {“1”, “2”, “3”}.
        :param pulumi.Input[str] master_disk_category: The system disk category of master node. Its valid value are `cloud_ssd` and `cloud_efficiency`. Default to `cloud_efficiency`.
        :param pulumi.Input[float] master_disk_size: The system disk size of master node. Its valid value range [20~500] in GB. Default to 20.
        :param pulumi.Input[str] master_instance_charge_type: Master payment type. `PrePaid` or `PostPaid`, defaults to `PostPaid`.
        :param pulumi.Input[str] master_instance_type: (Required, Force new resource) The instance type of master node.
        :param pulumi.Input[float] master_period: Master payment period. When period unit is `Month`, it can be one of { “1”, “2”, “3”, “4”, “5”, “6”, “7”, “8”, “9”, “12”, “24”, “36”,”48”,”60”}.  When period unit is `Week`, it can be one of {“1”, “2”, “3”, “4”}.
        :param pulumi.Input[str] master_period_unit: Master payment period unit. `Month` or `Week`, defaults to `Month`.
        :param pulumi.Input[str] name: The kubernetes cluster's name. It is the only in one Alicloud account.
        :param pulumi.Input[bool] new_nat_gateway: Whether to create a new nat gateway while creating kubernetes cluster. Default to true.
        :param pulumi.Input[float] node_cidr_mask: The network mask used on pods for each node, ranging from `24` to `28`.
               Larger this number is, less pods can be allocated on each node. Default value is `24`, means you can allocate 256 pods on each node.
        :param pulumi.Input[str] password: The password of ssh login cluster node. You have to specify one of `password` `key_name` `kms_encrypted_password` fields.
        :param pulumi.Input[str] pod_cidr: The CIDR block for the pod network. It will be allocated automatically when `vswitch_ids` is not specified.
               It cannot be duplicated with the VPC CIDR and CIDR used by Kubernetes cluster in VPC, cannot be modified after creation.
               Maximum number of hosts allowed in the cluster: 256. Refer to [Plan Kubernetes CIDR blocks under VPC](https://www.alibabacloud.com/help/doc-detail/64530.htm).
        :param pulumi.Input[str] service_cidr: The CIDR block for the service network. 
               It cannot be duplicated with the VPC CIDR and CIDR used by Kubernetes cluster in VPC, cannot be modified after creation.
        :param pulumi.Input[bool] slb_internet_enabled: Whether to create internet load balancer for API Server. Default to true.
        :param pulumi.Input[str] user_ca: The path of customized CA cert, you can use this CA to sign client certs to connect your cluster.
        :param pulumi.Input[str] version: Desired Kubernetes version. If you do not specify a value, the latest available version at resource creation is used and no upgrades will occur except you set a higher version number. The value must be configured and increased to upgrade the version when desired. Downgrades are not supported by ACK.
        :param pulumi.Input[str] vswitch_id: (Force new resource) The vswitch where new kubernetes cluster will be located. If it is not specified, a new VPC and VSwicth will be built. It must be in the zone which `availability_zone` specified.
        :param pulumi.Input[list] vswitch_ids: The vswitch where new kubernetes cluster will be located. Specify one or more vswitch's id. It must be in the zone which `availability_zone` specified.
        :param pulumi.Input[bool] worker_auto_renew: Enable worker payment auto-renew, defaults to false.
        :param pulumi.Input[float] worker_auto_renew_period: Worker payment auto-renew period. When period unit is `Month`, it can be one of {“1”, “2”, “3”, “6”, “12”}.  When period unit is `Week`, it can be one of {“1”, “2”, “3”}.
        :param pulumi.Input[str] worker_data_disk_category: The data disk category of worker node. Its valid value are `cloud_ssd` and `cloud_efficiency`, if not set, data disk will not be created.
        :param pulumi.Input[float] worker_data_disk_size: The data disk size of worker node. Its valid value range [20~32768] in GB. When `worker_data_disk_category` is presented, it defaults to 40.
        :param pulumi.Input[str] worker_disk_category: The system disk category of worker node. Its valid value are `cloud_ssd` and `cloud_efficiency`. Default to `cloud_efficiency`.
        :param pulumi.Input[float] worker_disk_size: The system disk size of worker node. Its valid value range [20~32768] in GB. Default to 20.
        :param pulumi.Input[str] worker_instance_charge_type: Worker payment type. `PrePaid` or `PostPaid`, defaults to `PostPaid`.
        :param pulumi.Input[str] worker_instance_type: (Required, Force new resource) The instance type of worker node.
        :param pulumi.Input[float] worker_number: The worker node number of the kubernetes cluster. Default to 3. It is limited up to 50 and if you want to enlarge it, please apply white list or contact with us.
        :param pulumi.Input[float] worker_period: Worker payment period. When period unit is `Month`, it can be one of { “1”, “2”, “3”, “4”, “5”, “6”, “7”, “8”, “9”, “12”, “24”, “36”,”48”,”60”}.  When period unit is `Week`, it can be one of {“1”, “2”, “3”, “4”}.
        :param pulumi.Input[str] worker_period_unit: Worker payment period unit. `Month` or `Week`, defaults to `Month`.

        The **log_config** object supports the following:

          * `project` (`pulumi.Input[str]`) - Log Service project name, cluster logs will output to this project.
          * `type` (`pulumi.Input[str]`) - Type of collecting logs, only `SLS` are supported currently.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['availability_zone'] = availability_zone
            __props__['client_cert'] = client_cert
            __props__['client_key'] = client_key
            __props__['cluster_ca_cert'] = cluster_ca_cert
            __props__['cluster_network_type'] = cluster_network_type
            __props__['enable_ssh'] = enable_ssh
            __props__['force_update'] = force_update
            __props__['image_id'] = image_id
            __props__['install_cloud_monitor'] = install_cloud_monitor
            __props__['is_outdated'] = is_outdated
            __props__['key_name'] = key_name
            __props__['kms_encrypted_password'] = kms_encrypted_password
            __props__['kms_encryption_context'] = kms_encryption_context
            __props__['kube_config'] = kube_config
            __props__['log_config'] = log_config
            __props__['master_auto_renew'] = master_auto_renew
            __props__['master_auto_renew_period'] = master_auto_renew_period
            __props__['master_disk_category'] = master_disk_category
            __props__['master_disk_size'] = master_disk_size
            __props__['master_instance_charge_type'] = master_instance_charge_type
            __props__['master_instance_type'] = master_instance_type
            if master_instance_types is None:
                raise TypeError("Missing required property 'master_instance_types'")
            __props__['master_instance_types'] = master_instance_types
            __props__['master_period'] = master_period
            __props__['master_period_unit'] = master_period_unit
            __props__['name'] = name
            __props__['name_prefix'] = name_prefix
            __props__['new_nat_gateway'] = new_nat_gateway
            __props__['node_cidr_mask'] = node_cidr_mask
            __props__['nodes'] = nodes
            __props__['password'] = password
            __props__['pod_cidr'] = pod_cidr
            __props__['service_cidr'] = service_cidr
            __props__['slb_internet_enabled'] = slb_internet_enabled
            __props__['user_ca'] = user_ca
            __props__['version'] = version
            __props__['vswitch_id'] = vswitch_id
            __props__['vswitch_ids'] = vswitch_ids
            __props__['worker_auto_renew'] = worker_auto_renew
            __props__['worker_auto_renew_period'] = worker_auto_renew_period
            __props__['worker_data_disk_category'] = worker_data_disk_category
            __props__['worker_data_disk_size'] = worker_data_disk_size
            __props__['worker_disk_category'] = worker_disk_category
            __props__['worker_disk_size'] = worker_disk_size
            __props__['worker_instance_charge_type'] = worker_instance_charge_type
            __props__['worker_instance_type'] = worker_instance_type
            if worker_instance_types is None:
                raise TypeError("Missing required property 'worker_instance_types'")
            __props__['worker_instance_types'] = worker_instance_types
            __props__['worker_number'] = worker_number
            if worker_numbers is None:
                raise TypeError("Missing required property 'worker_numbers'")
            __props__['worker_numbers'] = worker_numbers
            __props__['worker_period'] = worker_period
            __props__['worker_period_unit'] = worker_period_unit
            __props__['connections'] = None
            __props__['master_nodes'] = None
            __props__['nat_gateway_id'] = None
            __props__['security_group_id'] = None
            __props__['slb_id'] = None
            __props__['slb_internet'] = None
            __props__['slb_intranet'] = None
            __props__['vpc_id'] = None
            __props__['worker_nodes'] = None
        super(Kubernetes, __self__).__init__(
            'alicloud:cs/kubernetes:Kubernetes',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, availability_zone=None, client_cert=None, client_key=None, cluster_ca_cert=None, cluster_network_type=None, connections=None, enable_ssh=None, force_update=None, image_id=None, install_cloud_monitor=None, is_outdated=None, key_name=None, kms_encrypted_password=None, kms_encryption_context=None, kube_config=None, log_config=None, master_auto_renew=None, master_auto_renew_period=None, master_disk_category=None, master_disk_size=None, master_instance_charge_type=None, master_instance_type=None, master_instance_types=None, master_nodes=None, master_period=None, master_period_unit=None, name=None, name_prefix=None, nat_gateway_id=None, new_nat_gateway=None, node_cidr_mask=None, nodes=None, password=None, pod_cidr=None, security_group_id=None, service_cidr=None, slb_id=None, slb_internet=None, slb_internet_enabled=None, slb_intranet=None, user_ca=None, version=None, vpc_id=None, vswitch_id=None, vswitch_ids=None, worker_auto_renew=None, worker_auto_renew_period=None, worker_data_disk_category=None, worker_data_disk_size=None, worker_disk_category=None, worker_disk_size=None, worker_instance_charge_type=None, worker_instance_type=None, worker_instance_types=None, worker_nodes=None, worker_number=None, worker_numbers=None, worker_period=None, worker_period_unit=None):
        """
        Get an existing Kubernetes resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] availability_zone: The Zone where new kubernetes cluster will be located. If it is not be specified, the `vswitch_ids` should be set, its value will be vswitch's zone.
        :param pulumi.Input[str] client_cert: The path of client certificate, like `~/.kube/client-cert.pem`.
        :param pulumi.Input[str] client_key: The path of client key, like `~/.kube/client-key.pem`.
        :param pulumi.Input[str] cluster_ca_cert: The path of cluster ca certificate, like `~/.kube/cluster-ca-cert.pem`
        :param pulumi.Input[str] cluster_network_type: The network that cluster uses, use `flannel` or `terway`.
        :param pulumi.Input[dict] connections: Map of kubernetes cluster connection information. It contains several attributes to `Block Connections`.
        :param pulumi.Input[bool] enable_ssh: Whether to allow to SSH login kubernetes. Default to false.
        :param pulumi.Input[bool] force_update: Whether to force the update of kubernetes cluster arguments. Default to false.
        :param pulumi.Input[bool] install_cloud_monitor: Whether to install cloud monitor for the kubernetes' node.
        :param pulumi.Input[bool] is_outdated: Whether to use outdated instance type. Default to false.
        :param pulumi.Input[str] key_name: The keypair of ssh login cluster node, you have to create it first.
        :param pulumi.Input[str] kms_encrypted_password: An KMS encrypts password used to a cs kubernetes. It is conflicted with `password` and `key_name`.
        :param pulumi.Input[dict] kms_encryption_context: An KMS encryption context used to decrypt `kms_encrypted_password` before creating or updating a cs kubernetes with `kms_encrypted_password`. See [Encryption Context](https://www.alibabacloud.com/help/doc-detail/42975.htm). It is valid when `kms_encrypted_password` is set.
        :param pulumi.Input[str] kube_config: The path of kube config, like `~/.kube/config`.
        :param pulumi.Input[dict] log_config: A list of one element containing information about the associated log store. It contains the following attributes:
        :param pulumi.Input[bool] master_auto_renew: Enable master payment auto-renew, defaults to false.
        :param pulumi.Input[float] master_auto_renew_period: Master payment auto-renew period. When period unit is `Month`, it can be one of {“1”, “2”, “3”, “6”, “12”}.  When period unit is `Week`, it can be one of {“1”, “2”, “3”}.
        :param pulumi.Input[str] master_disk_category: The system disk category of master node. Its valid value are `cloud_ssd` and `cloud_efficiency`. Default to `cloud_efficiency`.
        :param pulumi.Input[float] master_disk_size: The system disk size of master node. Its valid value range [20~500] in GB. Default to 20.
        :param pulumi.Input[str] master_instance_charge_type: Master payment type. `PrePaid` or `PostPaid`, defaults to `PostPaid`.
        :param pulumi.Input[str] master_instance_type: (Required, Force new resource) The instance type of master node.
        :param pulumi.Input[list] master_nodes: List of cluster master nodes. It contains several attributes to `Block Nodes`.
        :param pulumi.Input[float] master_period: Master payment period. When period unit is `Month`, it can be one of { “1”, “2”, “3”, “4”, “5”, “6”, “7”, “8”, “9”, “12”, “24”, “36”,”48”,”60”}.  When period unit is `Week`, it can be one of {“1”, “2”, “3”, “4”}.
        :param pulumi.Input[str] master_period_unit: Master payment period unit. `Month` or `Week`, defaults to `Month`.
        :param pulumi.Input[str] name: The kubernetes cluster's name. It is the only in one Alicloud account.
        :param pulumi.Input[str] nat_gateway_id: The ID of nat gateway used to launch kubernetes cluster.
        :param pulumi.Input[bool] new_nat_gateway: Whether to create a new nat gateway while creating kubernetes cluster. Default to true.
        :param pulumi.Input[float] node_cidr_mask: The network mask used on pods for each node, ranging from `24` to `28`.
               Larger this number is, less pods can be allocated on each node. Default value is `24`, means you can allocate 256 pods on each node.
        :param pulumi.Input[str] password: The password of ssh login cluster node. You have to specify one of `password` `key_name` `kms_encrypted_password` fields.
        :param pulumi.Input[str] pod_cidr: The CIDR block for the pod network. It will be allocated automatically when `vswitch_ids` is not specified.
               It cannot be duplicated with the VPC CIDR and CIDR used by Kubernetes cluster in VPC, cannot be modified after creation.
               Maximum number of hosts allowed in the cluster: 256. Refer to [Plan Kubernetes CIDR blocks under VPC](https://www.alibabacloud.com/help/doc-detail/64530.htm).
        :param pulumi.Input[str] security_group_id: The ID of security group where the current cluster worker node is located.
        :param pulumi.Input[str] service_cidr: The CIDR block for the service network. 
               It cannot be duplicated with the VPC CIDR and CIDR used by Kubernetes cluster in VPC, cannot be modified after creation.
        :param pulumi.Input[bool] slb_internet_enabled: Whether to create internet load balancer for API Server. Default to true.
        :param pulumi.Input[str] slb_intranet: The ID of private load balancer where the current cluster master node is located.
        :param pulumi.Input[str] user_ca: The path of customized CA cert, you can use this CA to sign client certs to connect your cluster.
        :param pulumi.Input[str] version: Desired Kubernetes version. If you do not specify a value, the latest available version at resource creation is used and no upgrades will occur except you set a higher version number. The value must be configured and increased to upgrade the version when desired. Downgrades are not supported by ACK.
        :param pulumi.Input[str] vpc_id: The ID of VPC where the current cluster is located.
        :param pulumi.Input[str] vswitch_id: (Force new resource) The vswitch where new kubernetes cluster will be located. If it is not specified, a new VPC and VSwicth will be built. It must be in the zone which `availability_zone` specified.
        :param pulumi.Input[list] vswitch_ids: The vswitch where new kubernetes cluster will be located. Specify one or more vswitch's id. It must be in the zone which `availability_zone` specified.
        :param pulumi.Input[bool] worker_auto_renew: Enable worker payment auto-renew, defaults to false.
        :param pulumi.Input[float] worker_auto_renew_period: Worker payment auto-renew period. When period unit is `Month`, it can be one of {“1”, “2”, “3”, “6”, “12”}.  When period unit is `Week`, it can be one of {“1”, “2”, “3”}.
        :param pulumi.Input[str] worker_data_disk_category: The data disk category of worker node. Its valid value are `cloud_ssd` and `cloud_efficiency`, if not set, data disk will not be created.
        :param pulumi.Input[float] worker_data_disk_size: The data disk size of worker node. Its valid value range [20~32768] in GB. When `worker_data_disk_category` is presented, it defaults to 40.
        :param pulumi.Input[str] worker_disk_category: The system disk category of worker node. Its valid value are `cloud_ssd` and `cloud_efficiency`. Default to `cloud_efficiency`.
        :param pulumi.Input[float] worker_disk_size: The system disk size of worker node. Its valid value range [20~32768] in GB. Default to 20.
        :param pulumi.Input[str] worker_instance_charge_type: Worker payment type. `PrePaid` or `PostPaid`, defaults to `PostPaid`.
        :param pulumi.Input[str] worker_instance_type: (Required, Force new resource) The instance type of worker node.
        :param pulumi.Input[list] worker_nodes: List of cluster worker nodes. It contains several attributes to `Block Nodes`.
        :param pulumi.Input[float] worker_number: The worker node number of the kubernetes cluster. Default to 3. It is limited up to 50 and if you want to enlarge it, please apply white list or contact with us.
        :param pulumi.Input[float] worker_period: Worker payment period. When period unit is `Month`, it can be one of { “1”, “2”, “3”, “4”, “5”, “6”, “7”, “8”, “9”, “12”, “24”, “36”,”48”,”60”}.  When period unit is `Week`, it can be one of {“1”, “2”, “3”, “4”}.
        :param pulumi.Input[str] worker_period_unit: Worker payment period unit. `Month` or `Week`, defaults to `Month`.

        The **connections** object supports the following:

          * `api_server_internet` (`pulumi.Input[str]`) - API Server Internet endpoint.
          * `api_server_intranet` (`pulumi.Input[str]`) - API Server Intranet endpoint.
          * `master_public_ip` (`pulumi.Input[str]`) - Master node SSH IP address.
          * `service_domain` (`pulumi.Input[str]`) - Service Access Domain.

        The **log_config** object supports the following:

          * `project` (`pulumi.Input[str]`) - Log Service project name, cluster logs will output to this project.
          * `type` (`pulumi.Input[str]`) - Type of collecting logs, only `SLS` are supported currently.

        The **master_nodes** object supports the following:

          * `id` (`pulumi.Input[str]`) - ID of the node.
          * `name` (`pulumi.Input[str]`) - The kubernetes cluster's name. It is the only in one Alicloud account.
          * `private_ip` (`pulumi.Input[str]`) - The private IP address of node.

        The **worker_nodes** object supports the following:

          * `id` (`pulumi.Input[str]`) - ID of the node.
          * `name` (`pulumi.Input[str]`) - The kubernetes cluster's name. It is the only in one Alicloud account.
          * `private_ip` (`pulumi.Input[str]`) - The private IP address of node.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["availability_zone"] = availability_zone
        __props__["client_cert"] = client_cert
        __props__["client_key"] = client_key
        __props__["cluster_ca_cert"] = cluster_ca_cert
        __props__["cluster_network_type"] = cluster_network_type
        __props__["connections"] = connections
        __props__["enable_ssh"] = enable_ssh
        __props__["force_update"] = force_update
        __props__["image_id"] = image_id
        __props__["install_cloud_monitor"] = install_cloud_monitor
        __props__["is_outdated"] = is_outdated
        __props__["key_name"] = key_name
        __props__["kms_encrypted_password"] = kms_encrypted_password
        __props__["kms_encryption_context"] = kms_encryption_context
        __props__["kube_config"] = kube_config
        __props__["log_config"] = log_config
        __props__["master_auto_renew"] = master_auto_renew
        __props__["master_auto_renew_period"] = master_auto_renew_period
        __props__["master_disk_category"] = master_disk_category
        __props__["master_disk_size"] = master_disk_size
        __props__["master_instance_charge_type"] = master_instance_charge_type
        __props__["master_instance_type"] = master_instance_type
        __props__["master_instance_types"] = master_instance_types
        __props__["master_nodes"] = master_nodes
        __props__["master_period"] = master_period
        __props__["master_period_unit"] = master_period_unit
        __props__["name"] = name
        __props__["name_prefix"] = name_prefix
        __props__["nat_gateway_id"] = nat_gateway_id
        __props__["new_nat_gateway"] = new_nat_gateway
        __props__["node_cidr_mask"] = node_cidr_mask
        __props__["nodes"] = nodes
        __props__["password"] = password
        __props__["pod_cidr"] = pod_cidr
        __props__["security_group_id"] = security_group_id
        __props__["service_cidr"] = service_cidr
        __props__["slb_id"] = slb_id
        __props__["slb_internet"] = slb_internet
        __props__["slb_internet_enabled"] = slb_internet_enabled
        __props__["slb_intranet"] = slb_intranet
        __props__["user_ca"] = user_ca
        __props__["version"] = version
        __props__["vpc_id"] = vpc_id
        __props__["vswitch_id"] = vswitch_id
        __props__["vswitch_ids"] = vswitch_ids
        __props__["worker_auto_renew"] = worker_auto_renew
        __props__["worker_auto_renew_period"] = worker_auto_renew_period
        __props__["worker_data_disk_category"] = worker_data_disk_category
        __props__["worker_data_disk_size"] = worker_data_disk_size
        __props__["worker_disk_category"] = worker_disk_category
        __props__["worker_disk_size"] = worker_disk_size
        __props__["worker_instance_charge_type"] = worker_instance_charge_type
        __props__["worker_instance_type"] = worker_instance_type
        __props__["worker_instance_types"] = worker_instance_types
        __props__["worker_nodes"] = worker_nodes
        __props__["worker_number"] = worker_number
        __props__["worker_numbers"] = worker_numbers
        __props__["worker_period"] = worker_period
        __props__["worker_period_unit"] = worker_period_unit
        return Kubernetes(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

