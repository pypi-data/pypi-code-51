# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetPlaintextResult:
    """
    A collection of values returned by getPlaintext.
    """
    def __init__(__self__, ciphertext_blob=None, encryption_context=None, id=None, key_id=None, plaintext=None):
        if ciphertext_blob and not isinstance(ciphertext_blob, str):
            raise TypeError("Expected argument 'ciphertext_blob' to be a str")
        __self__.ciphertext_blob = ciphertext_blob
        if encryption_context and not isinstance(encryption_context, dict):
            raise TypeError("Expected argument 'encryption_context' to be a dict")
        __self__.encryption_context = encryption_context
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
        if key_id and not isinstance(key_id, str):
            raise TypeError("Expected argument 'key_id' to be a str")
        __self__.key_id = key_id
        """
        The globally unique ID of the CMK. It is the ID of the CMK used to decrypt ciphertext.
        """
        if plaintext and not isinstance(plaintext, str):
            raise TypeError("Expected argument 'plaintext' to be a str")
        __self__.plaintext = plaintext
        """
        The decrypted plaintext.
        """
class AwaitableGetPlaintextResult(GetPlaintextResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPlaintextResult(
            ciphertext_blob=self.ciphertext_blob,
            encryption_context=self.encryption_context,
            id=self.id,
            key_id=self.key_id,
            plaintext=self.plaintext)

def get_plaintext(ciphertext_blob=None,encryption_context=None,opts=None):
    """
    Use this data source to access information about an existing resource.

    :param str ciphertext_blob: The ciphertext to be decrypted.
    """
    __args__ = dict()


    __args__['ciphertextBlob'] = ciphertext_blob
    __args__['encryptionContext'] = encryption_context
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('alicloud:kms/getPlaintext:getPlaintext', __args__, opts=opts).value

    return AwaitableGetPlaintextResult(
        ciphertext_blob=__ret__.get('ciphertextBlob'),
        encryption_context=__ret__.get('encryptionContext'),
        id=__ret__.get('id'),
        key_id=__ret__.get('keyId'),
        plaintext=__ret__.get('plaintext'))
