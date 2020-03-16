# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class PrivateKey(pulumi.CustomResource):
    algorithm: pulumi.Output[str]
    """
    The name of the algorithm to use for
    the key. Currently-supported values are "RSA" and "ECDSA".
    """
    ecdsa_curve: pulumi.Output[str]
    """
    When `algorithm` is "ECDSA", the name of the elliptic
    curve to use. May be any one of "P224", "P256", "P384" or "P521", with "P224" as the
    default.
    """
    private_key_pem: pulumi.Output[str]
    """
    The private key data in PEM format.
    """
    public_key_fingerprint_md5: pulumi.Output[str]
    """
    The md5 hash of the public key data in
    OpenSSH MD5 hash format, e.g. `aa:bb:cc:...`. Only available if the
    selected private key format is compatible, as per the rules for
    `public_key_openssh`.
    """
    public_key_openssh: pulumi.Output[str]
    """
    The public key data in OpenSSH `authorized_keys`
    format, if the selected private key format is compatible. All RSA keys
    are supported, and ECDSA keys with curves "P256", "P384" and "P521"
    are supported. This attribute is empty if an incompatible ECDSA curve
    is selected.
    """
    public_key_pem: pulumi.Output[str]
    """
    The public key data in PEM format.
    """
    rsa_bits: pulumi.Output[float]
    """
    When `algorithm` is "RSA", the size of the generated
    RSA key in bits. Defaults to 2048.
    """
    def __init__(__self__, resource_name, opts=None, algorithm=None, ecdsa_curve=None, rsa_bits=None, __props__=None, __name__=None, __opts__=None):
        """
        Create a PrivateKey resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] algorithm: The name of the algorithm to use for
               the key. Currently-supported values are "RSA" and "ECDSA".
        :param pulumi.Input[str] ecdsa_curve: When `algorithm` is "ECDSA", the name of the elliptic
               curve to use. May be any one of "P224", "P256", "P384" or "P521", with "P224" as the
               default.
        :param pulumi.Input[float] rsa_bits: When `algorithm` is "RSA", the size of the generated
               RSA key in bits. Defaults to 2048.
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

            if algorithm is None:
                raise TypeError("Missing required property 'algorithm'")
            __props__['algorithm'] = algorithm
            __props__['ecdsa_curve'] = ecdsa_curve
            __props__['rsa_bits'] = rsa_bits
            __props__['private_key_pem'] = None
            __props__['public_key_fingerprint_md5'] = None
            __props__['public_key_openssh'] = None
            __props__['public_key_pem'] = None
        super(PrivateKey, __self__).__init__(
            'tls:index/privateKey:PrivateKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, algorithm=None, ecdsa_curve=None, private_key_pem=None, public_key_fingerprint_md5=None, public_key_openssh=None, public_key_pem=None, rsa_bits=None):
        """
        Get an existing PrivateKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] algorithm: The name of the algorithm to use for
               the key. Currently-supported values are "RSA" and "ECDSA".
        :param pulumi.Input[str] ecdsa_curve: When `algorithm` is "ECDSA", the name of the elliptic
               curve to use. May be any one of "P224", "P256", "P384" or "P521", with "P224" as the
               default.
        :param pulumi.Input[str] private_key_pem: The private key data in PEM format.
        :param pulumi.Input[str] public_key_fingerprint_md5: The md5 hash of the public key data in
               OpenSSH MD5 hash format, e.g. `aa:bb:cc:...`. Only available if the
               selected private key format is compatible, as per the rules for
               `public_key_openssh`.
        :param pulumi.Input[str] public_key_openssh: The public key data in OpenSSH `authorized_keys`
               format, if the selected private key format is compatible. All RSA keys
               are supported, and ECDSA keys with curves "P256", "P384" and "P521"
               are supported. This attribute is empty if an incompatible ECDSA curve
               is selected.
        :param pulumi.Input[str] public_key_pem: The public key data in PEM format.
        :param pulumi.Input[float] rsa_bits: When `algorithm` is "RSA", the size of the generated
               RSA key in bits. Defaults to 2048.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["algorithm"] = algorithm
        __props__["ecdsa_curve"] = ecdsa_curve
        __props__["private_key_pem"] = private_key_pem
        __props__["public_key_fingerprint_md5"] = public_key_fingerprint_md5
        __props__["public_key_openssh"] = public_key_openssh
        __props__["public_key_pem"] = public_key_pem
        __props__["rsa_bits"] = rsa_bits
        return PrivateKey(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

