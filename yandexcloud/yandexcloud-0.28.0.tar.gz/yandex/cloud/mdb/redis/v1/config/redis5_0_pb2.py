# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/redis/v1/config/redis5_0.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/mdb/redis/v1/config/redis5_0.proto',
  package='yandex.cloud.mdb.redis.v1.config',
  syntax='proto3',
  serialized_options=_b('\n$yandex.cloud.api.mdb.redis.v1.configZJgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/redis/v1/config;redis'),
  serialized_pb=_b('\n/yandex/cloud/mdb/redis/v1/config/redis5_0.proto\x12 yandex.cloud.mdb.redis.v1.config\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dyandex/cloud/validation.proto\"\x9b\x03\n\x0eRedisConfig5_0\x12Z\n\x10maxmemory_policy\x18\x01 \x01(\x0e\x32@.yandex.cloud.mdb.redis.v1.config.RedisConfig5_0.MaxmemoryPolicy\x12,\n\x07timeout\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x38\n\x08password\x18\x03 \x01(\tB&\xf2\xc7\x31\"[a-zA-Z0-9@=+?*.,!&#$^<>_-]{8,128}\"\xc4\x01\n\x0fMaxmemoryPolicy\x12 \n\x1cMAXMEMORY_POLICY_UNSPECIFIED\x10\x00\x12\x10\n\x0cVOLATILE_LRU\x10\x01\x12\x0f\n\x0b\x41LLKEYS_LRU\x10\x02\x12\x10\n\x0cVOLATILE_LFU\x10\x03\x12\x0f\n\x0b\x41LLKEYS_LFU\x10\x04\x12\x13\n\x0fVOLATILE_RANDOM\x10\x05\x12\x12\n\x0e\x41LLKEYS_RANDOM\x10\x06\x12\x10\n\x0cVOLATILE_TTL\x10\x07\x12\x0e\n\nNOEVICTION\x10\x08\"\xf0\x01\n\x11RedisConfigSet5_0\x12J\n\x10\x65\x66\x66\x65\x63tive_config\x18\x01 \x01(\x0b\x32\x30.yandex.cloud.mdb.redis.v1.config.RedisConfig5_0\x12\x45\n\x0buser_config\x18\x02 \x01(\x0b\x32\x30.yandex.cloud.mdb.redis.v1.config.RedisConfig5_0\x12H\n\x0e\x64\x65\x66\x61ult_config\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.mdb.redis.v1.config.RedisConfig5_0Br\n$yandex.cloud.api.mdb.redis.v1.configZJgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/redis/v1/config;redisb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])



_REDISCONFIG5_0_MAXMEMORYPOLICY = _descriptor.EnumDescriptor(
  name='MaxmemoryPolicy',
  full_name='yandex.cloud.mdb.redis.v1.config.RedisConfig5_0.MaxmemoryPolicy',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MAXMEMORY_POLICY_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VOLATILE_LRU', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALLKEYS_LRU', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VOLATILE_LFU', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALLKEYS_LFU', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VOLATILE_RANDOM', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALLKEYS_RANDOM', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VOLATILE_TTL', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOEVICTION', index=8, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=364,
  serialized_end=560,
)
_sym_db.RegisterEnumDescriptor(_REDISCONFIG5_0_MAXMEMORYPOLICY)


_REDISCONFIG5_0 = _descriptor.Descriptor(
  name='RedisConfig5_0',
  full_name='yandex.cloud.mdb.redis.v1.config.RedisConfig5_0',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='maxmemory_policy', full_name='yandex.cloud.mdb.redis.v1.config.RedisConfig5_0.maxmemory_policy', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='yandex.cloud.mdb.redis.v1.config.RedisConfig5_0.timeout', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='yandex.cloud.mdb.redis.v1.config.RedisConfig5_0.password', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\3071\"[a-zA-Z0-9@=+?*.,!&#$^<>_-]{8,128}'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REDISCONFIG5_0_MAXMEMORYPOLICY,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=149,
  serialized_end=560,
)


_REDISCONFIGSET5_0 = _descriptor.Descriptor(
  name='RedisConfigSet5_0',
  full_name='yandex.cloud.mdb.redis.v1.config.RedisConfigSet5_0',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='effective_config', full_name='yandex.cloud.mdb.redis.v1.config.RedisConfigSet5_0.effective_config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_config', full_name='yandex.cloud.mdb.redis.v1.config.RedisConfigSet5_0.user_config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default_config', full_name='yandex.cloud.mdb.redis.v1.config.RedisConfigSet5_0.default_config', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=563,
  serialized_end=803,
)

_REDISCONFIG5_0.fields_by_name['maxmemory_policy'].enum_type = _REDISCONFIG5_0_MAXMEMORYPOLICY
_REDISCONFIG5_0.fields_by_name['timeout'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_REDISCONFIG5_0_MAXMEMORYPOLICY.containing_type = _REDISCONFIG5_0
_REDISCONFIGSET5_0.fields_by_name['effective_config'].message_type = _REDISCONFIG5_0
_REDISCONFIGSET5_0.fields_by_name['user_config'].message_type = _REDISCONFIG5_0
_REDISCONFIGSET5_0.fields_by_name['default_config'].message_type = _REDISCONFIG5_0
DESCRIPTOR.message_types_by_name['RedisConfig5_0'] = _REDISCONFIG5_0
DESCRIPTOR.message_types_by_name['RedisConfigSet5_0'] = _REDISCONFIGSET5_0
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RedisConfig5_0 = _reflection.GeneratedProtocolMessageType('RedisConfig5_0', (_message.Message,), {
  'DESCRIPTOR' : _REDISCONFIG5_0,
  '__module__' : 'yandex.cloud.mdb.redis.v1.config.redis5_0_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.redis.v1.config.RedisConfig5_0)
  })
_sym_db.RegisterMessage(RedisConfig5_0)

RedisConfigSet5_0 = _reflection.GeneratedProtocolMessageType('RedisConfigSet5_0', (_message.Message,), {
  'DESCRIPTOR' : _REDISCONFIGSET5_0,
  '__module__' : 'yandex.cloud.mdb.redis.v1.config.redis5_0_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.redis.v1.config.RedisConfigSet5_0)
  })
_sym_db.RegisterMessage(RedisConfigSet5_0)


DESCRIPTOR._options = None
_REDISCONFIG5_0.fields_by_name['password']._options = None
# @@protoc_insertion_point(module_scope)
