# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class Application(pulumi.CustomResource):
    blue_green: pulumi.Output[bool]
    """
    Wherther to use "Blue Green" method when release a new version. Default to false.
    """
    blue_green_confirm: pulumi.Output[bool]
    """
    Whether to confirm a "Blue Green" application. Default to false. It will be ignored when `blue_green` is false.
    """
    cluster_name: pulumi.Output[str]
    """
    The swarm cluster's name.
    """
    default_domain: pulumi.Output[str]
    """
    The application default domain and it can be used to configure routing service.
    """
    description: pulumi.Output[str]
    """
    The description of application.
    """
    environment: pulumi.Output[dict]
    """
    A key/value map used to replace the variable parameter in the Compose template.
    """
    latest_image: pulumi.Output[bool]
    """
    Whether to use latest docker image while each updating application. Default to false.
    """
    name: pulumi.Output[str]
    """
    The application name. It should be 1-64 characters long, and can contain numbers, English letters and hyphens, but cannot start with hyphens.
    """
    services: pulumi.Output[list]
    """
    List of services in the application. It contains several attributes to `Block Nodes`.

      * `id` (`str`) - ID of the service.
      * `name` (`str`) - The application name. It should be 1-64 characters long, and can contain numbers, English letters and hyphens, but cannot start with hyphens.
      * `status` (`str`) - The current status of service.
      * `version` (`str`) - The application deploying version. Each updating, it must be different with current. Default to "1.0"
    """
    template: pulumi.Output[str]
    """
    The application deployment template and it must be [Docker Compose format](https://docs.docker.com/compose/).
    """
    version: pulumi.Output[str]
    """
    The application deploying version. Each updating, it must be different with current. Default to "1.0"
    """
    def __init__(__self__, resource_name, opts=None, blue_green=None, blue_green_confirm=None, cluster_name=None, description=None, environment=None, latest_image=None, name=None, template=None, version=None, __props__=None, __name__=None, __opts__=None):
        """
        > **DEPRECATED:** This resource manages applications in swarm cluster only, which is being deprecated and will be replaced by Kubernetes cluster.

        This resource use an orchestration template to define and deploy a multi-container application. An application is created by using an orchestration template.
        Each application can contain one or more services.

        > **NOTE:** Application orchestration template must be a valid Docker Compose YAML template.

        > **NOTE:** At present, this resource only support swarm cluster.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/cs_application.html.markdown.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] blue_green: Wherther to use "Blue Green" method when release a new version. Default to false.
        :param pulumi.Input[bool] blue_green_confirm: Whether to confirm a "Blue Green" application. Default to false. It will be ignored when `blue_green` is false.
        :param pulumi.Input[str] cluster_name: The swarm cluster's name.
        :param pulumi.Input[str] description: The description of application.
        :param pulumi.Input[dict] environment: A key/value map used to replace the variable parameter in the Compose template.
        :param pulumi.Input[bool] latest_image: Whether to use latest docker image while each updating application. Default to false.
        :param pulumi.Input[str] name: The application name. It should be 1-64 characters long, and can contain numbers, English letters and hyphens, but cannot start with hyphens.
        :param pulumi.Input[str] template: The application deployment template and it must be [Docker Compose format](https://docs.docker.com/compose/).
        :param pulumi.Input[str] version: The application deploying version. Each updating, it must be different with current. Default to "1.0"
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

            __props__['blue_green'] = blue_green
            __props__['blue_green_confirm'] = blue_green_confirm
            if cluster_name is None:
                raise TypeError("Missing required property 'cluster_name'")
            __props__['cluster_name'] = cluster_name
            __props__['description'] = description
            __props__['environment'] = environment
            __props__['latest_image'] = latest_image
            __props__['name'] = name
            if template is None:
                raise TypeError("Missing required property 'template'")
            __props__['template'] = template
            __props__['version'] = version
            __props__['default_domain'] = None
            __props__['services'] = None
        super(Application, __self__).__init__(
            'alicloud:cs/application:Application',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, blue_green=None, blue_green_confirm=None, cluster_name=None, default_domain=None, description=None, environment=None, latest_image=None, name=None, services=None, template=None, version=None):
        """
        Get an existing Application resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] blue_green: Wherther to use "Blue Green" method when release a new version. Default to false.
        :param pulumi.Input[bool] blue_green_confirm: Whether to confirm a "Blue Green" application. Default to false. It will be ignored when `blue_green` is false.
        :param pulumi.Input[str] cluster_name: The swarm cluster's name.
        :param pulumi.Input[str] default_domain: The application default domain and it can be used to configure routing service.
        :param pulumi.Input[str] description: The description of application.
        :param pulumi.Input[dict] environment: A key/value map used to replace the variable parameter in the Compose template.
        :param pulumi.Input[bool] latest_image: Whether to use latest docker image while each updating application. Default to false.
        :param pulumi.Input[str] name: The application name. It should be 1-64 characters long, and can contain numbers, English letters and hyphens, but cannot start with hyphens.
        :param pulumi.Input[list] services: List of services in the application. It contains several attributes to `Block Nodes`.
        :param pulumi.Input[str] template: The application deployment template and it must be [Docker Compose format](https://docs.docker.com/compose/).
        :param pulumi.Input[str] version: The application deploying version. Each updating, it must be different with current. Default to "1.0"

        The **services** object supports the following:

          * `id` (`pulumi.Input[str]`) - ID of the service.
          * `name` (`pulumi.Input[str]`) - The application name. It should be 1-64 characters long, and can contain numbers, English letters and hyphens, but cannot start with hyphens.
          * `status` (`pulumi.Input[str]`) - The current status of service.
          * `version` (`pulumi.Input[str]`) - The application deploying version. Each updating, it must be different with current. Default to "1.0"
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["blue_green"] = blue_green
        __props__["blue_green_confirm"] = blue_green_confirm
        __props__["cluster_name"] = cluster_name
        __props__["default_domain"] = default_domain
        __props__["description"] = description
        __props__["environment"] = environment
        __props__["latest_image"] = latest_image
        __props__["name"] = name
        __props__["services"] = services
        __props__["template"] = template
        __props__["version"] = version
        return Application(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

