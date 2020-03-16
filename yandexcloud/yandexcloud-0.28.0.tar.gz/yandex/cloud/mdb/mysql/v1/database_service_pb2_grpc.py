# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from yandex.cloud.mdb.mysql.v1 import database_pb2 as yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_database__pb2
from yandex.cloud.mdb.mysql.v1 import database_service_pb2 as yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_database__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class DatabaseServiceStub(object):
  """A set of methods for managing MySQL databases.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Get = channel.unary_unary(
        '/yandex.cloud.mdb.mysql.v1.DatabaseService/Get',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_database__service__pb2.GetDatabaseRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_database__pb2.Database.FromString,
        )
    self.List = channel.unary_unary(
        '/yandex.cloud.mdb.mysql.v1.DatabaseService/List',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_database__service__pb2.ListDatabasesRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_database__service__pb2.ListDatabasesResponse.FromString,
        )
    self.Create = channel.unary_unary(
        '/yandex.cloud.mdb.mysql.v1.DatabaseService/Create',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_database__service__pb2.CreateDatabaseRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.Delete = channel.unary_unary(
        '/yandex.cloud.mdb.mysql.v1.DatabaseService/Delete',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_database__service__pb2.DeleteDatabaseRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )


class DatabaseServiceServicer(object):
  """A set of methods for managing MySQL databases.
  """

  def Get(self, request, context):
    """Returns the specified MySQL database.

    To get the list of available MySQL databases, make a [List] request.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def List(self, request, context):
    """Retrieves the list of MySQL databases in the specified cluster.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Create(self, request, context):
    """Creates a new MySQL database in the specified cluster.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    """Deletes the specified MySQL database.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DatabaseServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_database__service__pb2.GetDatabaseRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_database__pb2.Database.SerializeToString,
      ),
      'List': grpc.unary_unary_rpc_method_handler(
          servicer.List,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_database__service__pb2.ListDatabasesRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_database__service__pb2.ListDatabasesResponse.SerializeToString,
      ),
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_database__service__pb2.CreateDatabaseRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_database__service__pb2.DeleteDatabaseRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'yandex.cloud.mdb.mysql.v1.DatabaseService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
