# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/mysql/v1/user_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.mdb.mysql.v1 import user_pb2 as yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_user__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/mdb/mysql/v1/user_service.proto',
  package='yandex.cloud.mdb.mysql.v1',
  syntax='proto3',
  serialized_options=_b('\n\035yandex.cloud.api.mdb.mysql.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mysql/v1;mysql'),
  serialized_pb=_b('\n,yandex/cloud/mdb/mysql/v1/user_service.proto\x12\x19yandex.cloud.mdb.mysql.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\x1a$yandex/cloud/mdb/mysql/v1/user.proto\"d\n\x0eGetUserRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x30\n\tuser_name\x18\x02 \x01(\tB\x1d\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=63\xf2\xc7\x31\r[a-zA-Z0-9_]*\"r\n\x10ListUsersRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"\\\n\x11ListUsersResponse\x12.\n\x05users\x18\x01 \x03(\x0b\x32\x1f.yandex.cloud.mdb.mysql.v1.User\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"s\n\x11\x43reateUserRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12<\n\tuser_spec\x18\x02 \x01(\x0b\x32#.yandex.cloud.mdb.mysql.v1.UserSpecB\x04\xe8\xc7\x31\x01\";\n\x12\x43reateUserMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t\"\xf1\x01\n\x11UpdateUserRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x30\n\tuser_name\x18\x02 \x01(\tB\x1d\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=63\xf2\xc7\x31\r[a-zA-Z0-9_]*\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1b\n\x08password\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05\x38-128\x12:\n\x0bpermissions\x18\x05 \x03(\x0b\x32%.yandex.cloud.mdb.mysql.v1.Permission\";\n\x12UpdateUserMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t\"g\n\x11\x44\x65leteUserRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x30\n\tuser_name\x18\x02 \x01(\tB\x1d\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=63\xf2\xc7\x31\r[a-zA-Z0-9_]*\";\n\x12\x44\x65leteUserMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t\"\xb1\x01\n\x1aGrantUserPermissionRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x30\n\tuser_name\x18\x02 \x01(\tB\x1d\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=63\xf2\xc7\x31\r[a-zA-Z0-9_]*\x12?\n\npermission\x18\x03 \x01(\x0b\x32%.yandex.cloud.mdb.mysql.v1.PermissionB\x04\xe8\xc7\x31\x01\"D\n\x1bGrantUserPermissionMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t\"\xb2\x01\n\x1bRevokeUserPermissionRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x30\n\tuser_name\x18\x02 \x01(\tB\x1d\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=63\xf2\xc7\x31\r[a-zA-Z0-9_]*\x12?\n\npermission\x18\x03 \x01(\x0b\x32%.yandex.cloud.mdb.mysql.v1.PermissionB\x04\xe8\xc7\x31\x01\"E\n\x1cRevokeUserPermissionMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t2\xdb\n\n\x0bUserService\x12\x94\x01\n\x03Get\x12).yandex.cloud.mdb.mysql.v1.GetUserRequest\x1a\x1f.yandex.cloud.mdb.mysql.v1.User\"A\x82\xd3\xe4\x93\x02;\x12\x39/managed-mysql/v1/clusters/{cluster_id}/users/{user_name}\x12\x98\x01\n\x04List\x12+.yandex.cloud.mdb.mysql.v1.ListUsersRequest\x1a,.yandex.cloud.mdb.mysql.v1.ListUsersResponse\"5\x82\xd3\xe4\x93\x02/\x12-/managed-mysql/v1/clusters/{cluster_id}/users\x12\xb1\x01\n\x06\x43reate\x12,.yandex.cloud.mdb.mysql.v1.CreateUserRequest\x1a!.yandex.cloud.operation.Operation\"V\x82\xd3\xe4\x93\x02\x32\"-/managed-mysql/v1/clusters/{cluster_id}/users:\x01*\xb2\xd2*\x1a\n\x12\x43reateUserMetadata\x12\x04User\x12\xbd\x01\n\x06Update\x12,.yandex.cloud.mdb.mysql.v1.UpdateUserRequest\x1a!.yandex.cloud.operation.Operation\"b\x82\xd3\xe4\x93\x02>29/managed-mysql/v1/clusters/{cluster_id}/users/{user_name}:\x01*\xb2\xd2*\x1a\n\x12UpdateUserMetadata\x12\x04User\x12\xcb\x01\n\x06\x44\x65lete\x12,.yandex.cloud.mdb.mysql.v1.DeleteUserRequest\x1a!.yandex.cloud.operation.Operation\"p\x82\xd3\xe4\x93\x02;*9/managed-mysql/v1/clusters/{cluster_id}/users/{user_name}\xb2\xd2*+\n\x12\x44\x65leteUserMetadata\x12\x15google.protobuf.Empty\x12\xe8\x01\n\x0fGrantPermission\x12\x35.yandex.cloud.mdb.mysql.v1.GrantUserPermissionRequest\x1a!.yandex.cloud.operation.Operation\"{\x82\xd3\xe4\x93\x02N\"I/managed-mysql/v1/clusters/{cluster_id}/users/{user_name}:grantPermission:\x01*\xb2\xd2*#\n\x1bGrantUserPermissionMetadata\x12\x04User\x12\xec\x01\n\x10RevokePermission\x12\x36.yandex.cloud.mdb.mysql.v1.RevokeUserPermissionRequest\x1a!.yandex.cloud.operation.Operation\"}\x82\xd3\xe4\x93\x02O\"J/managed-mysql/v1/clusters/{cluster_id}/users/{user_name}:revokePermission:\x01*\xb2\xd2*$\n\x1cRevokeUserPermissionMetadata\x12\x04UserBd\n\x1dyandex.cloud.api.mdb.mysql.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mysql/v1;mysqlb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,yandex_dot_cloud_dot_api_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_operation_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_user__pb2.DESCRIPTOR,])




_GETUSERREQUEST = _descriptor.Descriptor(
  name='GetUserRequest',
  full_name='yandex.cloud.mdb.mysql.v1.GetUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.mysql.v1.GetUserRequest.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001\212\3101\004<=50'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='yandex.cloud.mdb.mysql.v1.GetUserRequest.user_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001\212\3101\004<=63\362\3071\r[a-zA-Z0-9_]*'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=282,
  serialized_end=382,
)


_LISTUSERSREQUEST = _descriptor.Descriptor(
  name='ListUsersRequest',
  full_name='yandex.cloud.mdb.mysql.v1.ListUsersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.mysql.v1.ListUsersRequest.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001\212\3101\004<=50'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='yandex.cloud.mdb.mysql.v1.ListUsersRequest.page_size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\372\3071\0060-1000'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='yandex.cloud.mdb.mysql.v1.ListUsersRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3101\005<=100'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=384,
  serialized_end=498,
)


_LISTUSERSRESPONSE = _descriptor.Descriptor(
  name='ListUsersResponse',
  full_name='yandex.cloud.mdb.mysql.v1.ListUsersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='users', full_name='yandex.cloud.mdb.mysql.v1.ListUsersResponse.users', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='yandex.cloud.mdb.mysql.v1.ListUsersResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=500,
  serialized_end=592,
)


_CREATEUSERREQUEST = _descriptor.Descriptor(
  name='CreateUserRequest',
  full_name='yandex.cloud.mdb.mysql.v1.CreateUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.mysql.v1.CreateUserRequest.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001\212\3101\004<=50'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_spec', full_name='yandex.cloud.mdb.mysql.v1.CreateUserRequest.user_spec', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=594,
  serialized_end=709,
)


_CREATEUSERMETADATA = _descriptor.Descriptor(
  name='CreateUserMetadata',
  full_name='yandex.cloud.mdb.mysql.v1.CreateUserMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.mysql.v1.CreateUserMetadata.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='yandex.cloud.mdb.mysql.v1.CreateUserMetadata.user_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=711,
  serialized_end=770,
)


_UPDATEUSERREQUEST = _descriptor.Descriptor(
  name='UpdateUserRequest',
  full_name='yandex.cloud.mdb.mysql.v1.UpdateUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.mysql.v1.UpdateUserRequest.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001\212\3101\004<=50'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='yandex.cloud.mdb.mysql.v1.UpdateUserRequest.user_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001\212\3101\004<=63\362\3071\r[a-zA-Z0-9_]*'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='yandex.cloud.mdb.mysql.v1.UpdateUserRequest.update_mask', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='yandex.cloud.mdb.mysql.v1.UpdateUserRequest.password', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3101\0058-128'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='permissions', full_name='yandex.cloud.mdb.mysql.v1.UpdateUserRequest.permissions', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=773,
  serialized_end=1014,
)


_UPDATEUSERMETADATA = _descriptor.Descriptor(
  name='UpdateUserMetadata',
  full_name='yandex.cloud.mdb.mysql.v1.UpdateUserMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.mysql.v1.UpdateUserMetadata.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='yandex.cloud.mdb.mysql.v1.UpdateUserMetadata.user_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1016,
  serialized_end=1075,
)


_DELETEUSERREQUEST = _descriptor.Descriptor(
  name='DeleteUserRequest',
  full_name='yandex.cloud.mdb.mysql.v1.DeleteUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.mysql.v1.DeleteUserRequest.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001\212\3101\004<=50'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='yandex.cloud.mdb.mysql.v1.DeleteUserRequest.user_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001\212\3101\004<=63\362\3071\r[a-zA-Z0-9_]*'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1077,
  serialized_end=1180,
)


_DELETEUSERMETADATA = _descriptor.Descriptor(
  name='DeleteUserMetadata',
  full_name='yandex.cloud.mdb.mysql.v1.DeleteUserMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.mysql.v1.DeleteUserMetadata.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='yandex.cloud.mdb.mysql.v1.DeleteUserMetadata.user_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1182,
  serialized_end=1241,
)


_GRANTUSERPERMISSIONREQUEST = _descriptor.Descriptor(
  name='GrantUserPermissionRequest',
  full_name='yandex.cloud.mdb.mysql.v1.GrantUserPermissionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.mysql.v1.GrantUserPermissionRequest.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001\212\3101\004<=50'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='yandex.cloud.mdb.mysql.v1.GrantUserPermissionRequest.user_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001\212\3101\004<=63\362\3071\r[a-zA-Z0-9_]*'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='permission', full_name='yandex.cloud.mdb.mysql.v1.GrantUserPermissionRequest.permission', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1244,
  serialized_end=1421,
)


_GRANTUSERPERMISSIONMETADATA = _descriptor.Descriptor(
  name='GrantUserPermissionMetadata',
  full_name='yandex.cloud.mdb.mysql.v1.GrantUserPermissionMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.mysql.v1.GrantUserPermissionMetadata.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='yandex.cloud.mdb.mysql.v1.GrantUserPermissionMetadata.user_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1423,
  serialized_end=1491,
)


_REVOKEUSERPERMISSIONREQUEST = _descriptor.Descriptor(
  name='RevokeUserPermissionRequest',
  full_name='yandex.cloud.mdb.mysql.v1.RevokeUserPermissionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.mysql.v1.RevokeUserPermissionRequest.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001\212\3101\004<=50'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='yandex.cloud.mdb.mysql.v1.RevokeUserPermissionRequest.user_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001\212\3101\004<=63\362\3071\r[a-zA-Z0-9_]*'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='permission', full_name='yandex.cloud.mdb.mysql.v1.RevokeUserPermissionRequest.permission', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1494,
  serialized_end=1672,
)


_REVOKEUSERPERMISSIONMETADATA = _descriptor.Descriptor(
  name='RevokeUserPermissionMetadata',
  full_name='yandex.cloud.mdb.mysql.v1.RevokeUserPermissionMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.mysql.v1.RevokeUserPermissionMetadata.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='yandex.cloud.mdb.mysql.v1.RevokeUserPermissionMetadata.user_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1674,
  serialized_end=1743,
)

_LISTUSERSRESPONSE.fields_by_name['users'].message_type = yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_user__pb2._USER
_CREATEUSERREQUEST.fields_by_name['user_spec'].message_type = yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_user__pb2._USERSPEC
_UPDATEUSERREQUEST.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_UPDATEUSERREQUEST.fields_by_name['permissions'].message_type = yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_user__pb2._PERMISSION
_GRANTUSERPERMISSIONREQUEST.fields_by_name['permission'].message_type = yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_user__pb2._PERMISSION
_REVOKEUSERPERMISSIONREQUEST.fields_by_name['permission'].message_type = yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_user__pb2._PERMISSION
DESCRIPTOR.message_types_by_name['GetUserRequest'] = _GETUSERREQUEST
DESCRIPTOR.message_types_by_name['ListUsersRequest'] = _LISTUSERSREQUEST
DESCRIPTOR.message_types_by_name['ListUsersResponse'] = _LISTUSERSRESPONSE
DESCRIPTOR.message_types_by_name['CreateUserRequest'] = _CREATEUSERREQUEST
DESCRIPTOR.message_types_by_name['CreateUserMetadata'] = _CREATEUSERMETADATA
DESCRIPTOR.message_types_by_name['UpdateUserRequest'] = _UPDATEUSERREQUEST
DESCRIPTOR.message_types_by_name['UpdateUserMetadata'] = _UPDATEUSERMETADATA
DESCRIPTOR.message_types_by_name['DeleteUserRequest'] = _DELETEUSERREQUEST
DESCRIPTOR.message_types_by_name['DeleteUserMetadata'] = _DELETEUSERMETADATA
DESCRIPTOR.message_types_by_name['GrantUserPermissionRequest'] = _GRANTUSERPERMISSIONREQUEST
DESCRIPTOR.message_types_by_name['GrantUserPermissionMetadata'] = _GRANTUSERPERMISSIONMETADATA
DESCRIPTOR.message_types_by_name['RevokeUserPermissionRequest'] = _REVOKEUSERPERMISSIONREQUEST
DESCRIPTOR.message_types_by_name['RevokeUserPermissionMetadata'] = _REVOKEUSERPERMISSIONMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetUserRequest = _reflection.GeneratedProtocolMessageType('GetUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERREQUEST,
  '__module__' : 'yandex.cloud.mdb.mysql.v1.user_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mysql.v1.GetUserRequest)
  })
_sym_db.RegisterMessage(GetUserRequest)

ListUsersRequest = _reflection.GeneratedProtocolMessageType('ListUsersRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTUSERSREQUEST,
  '__module__' : 'yandex.cloud.mdb.mysql.v1.user_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mysql.v1.ListUsersRequest)
  })
_sym_db.RegisterMessage(ListUsersRequest)

ListUsersResponse = _reflection.GeneratedProtocolMessageType('ListUsersResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTUSERSRESPONSE,
  '__module__' : 'yandex.cloud.mdb.mysql.v1.user_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mysql.v1.ListUsersResponse)
  })
_sym_db.RegisterMessage(ListUsersResponse)

CreateUserRequest = _reflection.GeneratedProtocolMessageType('CreateUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEUSERREQUEST,
  '__module__' : 'yandex.cloud.mdb.mysql.v1.user_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mysql.v1.CreateUserRequest)
  })
_sym_db.RegisterMessage(CreateUserRequest)

CreateUserMetadata = _reflection.GeneratedProtocolMessageType('CreateUserMetadata', (_message.Message,), {
  'DESCRIPTOR' : _CREATEUSERMETADATA,
  '__module__' : 'yandex.cloud.mdb.mysql.v1.user_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mysql.v1.CreateUserMetadata)
  })
_sym_db.RegisterMessage(CreateUserMetadata)

UpdateUserRequest = _reflection.GeneratedProtocolMessageType('UpdateUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEUSERREQUEST,
  '__module__' : 'yandex.cloud.mdb.mysql.v1.user_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mysql.v1.UpdateUserRequest)
  })
_sym_db.RegisterMessage(UpdateUserRequest)

UpdateUserMetadata = _reflection.GeneratedProtocolMessageType('UpdateUserMetadata', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEUSERMETADATA,
  '__module__' : 'yandex.cloud.mdb.mysql.v1.user_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mysql.v1.UpdateUserMetadata)
  })
_sym_db.RegisterMessage(UpdateUserMetadata)

DeleteUserRequest = _reflection.GeneratedProtocolMessageType('DeleteUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEUSERREQUEST,
  '__module__' : 'yandex.cloud.mdb.mysql.v1.user_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mysql.v1.DeleteUserRequest)
  })
_sym_db.RegisterMessage(DeleteUserRequest)

DeleteUserMetadata = _reflection.GeneratedProtocolMessageType('DeleteUserMetadata', (_message.Message,), {
  'DESCRIPTOR' : _DELETEUSERMETADATA,
  '__module__' : 'yandex.cloud.mdb.mysql.v1.user_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mysql.v1.DeleteUserMetadata)
  })
_sym_db.RegisterMessage(DeleteUserMetadata)

GrantUserPermissionRequest = _reflection.GeneratedProtocolMessageType('GrantUserPermissionRequest', (_message.Message,), {
  'DESCRIPTOR' : _GRANTUSERPERMISSIONREQUEST,
  '__module__' : 'yandex.cloud.mdb.mysql.v1.user_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mysql.v1.GrantUserPermissionRequest)
  })
_sym_db.RegisterMessage(GrantUserPermissionRequest)

GrantUserPermissionMetadata = _reflection.GeneratedProtocolMessageType('GrantUserPermissionMetadata', (_message.Message,), {
  'DESCRIPTOR' : _GRANTUSERPERMISSIONMETADATA,
  '__module__' : 'yandex.cloud.mdb.mysql.v1.user_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mysql.v1.GrantUserPermissionMetadata)
  })
_sym_db.RegisterMessage(GrantUserPermissionMetadata)

RevokeUserPermissionRequest = _reflection.GeneratedProtocolMessageType('RevokeUserPermissionRequest', (_message.Message,), {
  'DESCRIPTOR' : _REVOKEUSERPERMISSIONREQUEST,
  '__module__' : 'yandex.cloud.mdb.mysql.v1.user_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mysql.v1.RevokeUserPermissionRequest)
  })
_sym_db.RegisterMessage(RevokeUserPermissionRequest)

RevokeUserPermissionMetadata = _reflection.GeneratedProtocolMessageType('RevokeUserPermissionMetadata', (_message.Message,), {
  'DESCRIPTOR' : _REVOKEUSERPERMISSIONMETADATA,
  '__module__' : 'yandex.cloud.mdb.mysql.v1.user_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mysql.v1.RevokeUserPermissionMetadata)
  })
_sym_db.RegisterMessage(RevokeUserPermissionMetadata)


DESCRIPTOR._options = None
_GETUSERREQUEST.fields_by_name['cluster_id']._options = None
_GETUSERREQUEST.fields_by_name['user_name']._options = None
_LISTUSERSREQUEST.fields_by_name['cluster_id']._options = None
_LISTUSERSREQUEST.fields_by_name['page_size']._options = None
_LISTUSERSREQUEST.fields_by_name['page_token']._options = None
_CREATEUSERREQUEST.fields_by_name['cluster_id']._options = None
_CREATEUSERREQUEST.fields_by_name['user_spec']._options = None
_UPDATEUSERREQUEST.fields_by_name['cluster_id']._options = None
_UPDATEUSERREQUEST.fields_by_name['user_name']._options = None
_UPDATEUSERREQUEST.fields_by_name['password']._options = None
_DELETEUSERREQUEST.fields_by_name['cluster_id']._options = None
_DELETEUSERREQUEST.fields_by_name['user_name']._options = None
_GRANTUSERPERMISSIONREQUEST.fields_by_name['cluster_id']._options = None
_GRANTUSERPERMISSIONREQUEST.fields_by_name['user_name']._options = None
_GRANTUSERPERMISSIONREQUEST.fields_by_name['permission']._options = None
_REVOKEUSERPERMISSIONREQUEST.fields_by_name['cluster_id']._options = None
_REVOKEUSERPERMISSIONREQUEST.fields_by_name['user_name']._options = None
_REVOKEUSERPERMISSIONREQUEST.fields_by_name['permission']._options = None

_USERSERVICE = _descriptor.ServiceDescriptor(
  name='UserService',
  full_name='yandex.cloud.mdb.mysql.v1.UserService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1746,
  serialized_end=3117,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='yandex.cloud.mdb.mysql.v1.UserService.Get',
    index=0,
    containing_service=None,
    input_type=_GETUSERREQUEST,
    output_type=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_user__pb2._USER,
    serialized_options=_b('\202\323\344\223\002;\0229/managed-mysql/v1/clusters/{cluster_id}/users/{user_name}'),
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='yandex.cloud.mdb.mysql.v1.UserService.List',
    index=1,
    containing_service=None,
    input_type=_LISTUSERSREQUEST,
    output_type=_LISTUSERSRESPONSE,
    serialized_options=_b('\202\323\344\223\002/\022-/managed-mysql/v1/clusters/{cluster_id}/users'),
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='yandex.cloud.mdb.mysql.v1.UserService.Create',
    index=2,
    containing_service=None,
    input_type=_CREATEUSERREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=_b('\202\323\344\223\0022\"-/managed-mysql/v1/clusters/{cluster_id}/users:\001*\262\322*\032\n\022CreateUserMetadata\022\004User'),
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='yandex.cloud.mdb.mysql.v1.UserService.Update',
    index=3,
    containing_service=None,
    input_type=_UPDATEUSERREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=_b('\202\323\344\223\002>29/managed-mysql/v1/clusters/{cluster_id}/users/{user_name}:\001*\262\322*\032\n\022UpdateUserMetadata\022\004User'),
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='yandex.cloud.mdb.mysql.v1.UserService.Delete',
    index=4,
    containing_service=None,
    input_type=_DELETEUSERREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=_b('\202\323\344\223\002;*9/managed-mysql/v1/clusters/{cluster_id}/users/{user_name}\262\322*+\n\022DeleteUserMetadata\022\025google.protobuf.Empty'),
  ),
  _descriptor.MethodDescriptor(
    name='GrantPermission',
    full_name='yandex.cloud.mdb.mysql.v1.UserService.GrantPermission',
    index=5,
    containing_service=None,
    input_type=_GRANTUSERPERMISSIONREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=_b('\202\323\344\223\002N\"I/managed-mysql/v1/clusters/{cluster_id}/users/{user_name}:grantPermission:\001*\262\322*#\n\033GrantUserPermissionMetadata\022\004User'),
  ),
  _descriptor.MethodDescriptor(
    name='RevokePermission',
    full_name='yandex.cloud.mdb.mysql.v1.UserService.RevokePermission',
    index=6,
    containing_service=None,
    input_type=_REVOKEUSERPERMISSIONREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=_b('\202\323\344\223\002O\"J/managed-mysql/v1/clusters/{cluster_id}/users/{user_name}:revokePermission:\001*\262\322*$\n\034RevokeUserPermissionMetadata\022\004User'),
  ),
])
_sym_db.RegisterServiceDescriptor(_USERSERVICE)

DESCRIPTOR.services_by_name['UserService'] = _USERSERVICE

# @@protoc_insertion_point(module_scope)
