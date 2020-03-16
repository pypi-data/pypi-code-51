# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from yandex.cloud.kms.v1 import symmetric_crypto_service_pb2 as yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2


class SymmetricCryptoServiceStub(object):
  """--- Data plane for KMS symmetric cryptography operations

  Set of methods that perform symmetric encryption and decryption.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Encrypt = channel.unary_unary(
        '/yandex.cloud.kms.v1.SymmetricCryptoService/Encrypt',
        request_serializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.SymmetricEncryptRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.SymmetricEncryptResponse.FromString,
        )
    self.Decrypt = channel.unary_unary(
        '/yandex.cloud.kms.v1.SymmetricCryptoService/Decrypt',
        request_serializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.SymmetricDecryptRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.SymmetricDecryptResponse.FromString,
        )
    self.ReEncrypt = channel.unary_unary(
        '/yandex.cloud.kms.v1.SymmetricCryptoService/ReEncrypt',
        request_serializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.SymmetricReEncryptRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.SymmetricReEncryptResponse.FromString,
        )
    self.GenerateDataKey = channel.unary_unary(
        '/yandex.cloud.kms.v1.SymmetricCryptoService/GenerateDataKey',
        request_serializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.GenerateDataKeyRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.GenerateDataKeyResponse.FromString,
        )


class SymmetricCryptoServiceServicer(object):
  """--- Data plane for KMS symmetric cryptography operations

  Set of methods that perform symmetric encryption and decryption.
  """

  def Encrypt(self, request, context):
    """Encrypts given plaintext with the specified key.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Decrypt(self, request, context):
    """Decrypts the given ciphertext with the specified key.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReEncrypt(self, request, context):
    """Re-encrypts a ciphertext with the specified KMS key.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GenerateDataKey(self, request, context):
    """Generates a new symmetric data encryption key (not a KMS key) and returns
    the generated key as plaintext and as ciphertext encrypted with the specified symmetric KMS key.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SymmetricCryptoServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Encrypt': grpc.unary_unary_rpc_method_handler(
          servicer.Encrypt,
          request_deserializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.SymmetricEncryptRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.SymmetricEncryptResponse.SerializeToString,
      ),
      'Decrypt': grpc.unary_unary_rpc_method_handler(
          servicer.Decrypt,
          request_deserializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.SymmetricDecryptRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.SymmetricDecryptResponse.SerializeToString,
      ),
      'ReEncrypt': grpc.unary_unary_rpc_method_handler(
          servicer.ReEncrypt,
          request_deserializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.SymmetricReEncryptRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.SymmetricReEncryptResponse.SerializeToString,
      ),
      'GenerateDataKey': grpc.unary_unary_rpc_method_handler(
          servicer.GenerateDataKey,
          request_deserializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.GenerateDataKeyRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.GenerateDataKeyResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'yandex.cloud.kms.v1.SymmetricCryptoService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
