# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/mysql/v1alpha/resource_preset.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/mdb/mysql/v1alpha/resource_preset.proto',
  package='yandex.cloud.mdb.mysql.v1alpha',
  syntax='proto3',
  serialized_options=_b('\n\"yandex.cloud.api.mdb.mysql.v1alphaZHgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mysql/v1alpha;mysql'),
  serialized_pb=_b('\n4yandex/cloud/mdb/mysql/v1alpha/resource_preset.proto\x12\x1eyandex.cloud.mdb.mysql.v1alpha\"M\n\x0eResourcePreset\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08zone_ids\x18\x02 \x03(\t\x12\r\n\x05\x63ores\x18\x03 \x01(\x03\x12\x0e\n\x06memory\x18\x04 \x01(\x03\x42n\n\"yandex.cloud.api.mdb.mysql.v1alphaZHgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mysql/v1alpha;mysqlb\x06proto3')
)




_RESOURCEPRESET = _descriptor.Descriptor(
  name='ResourcePreset',
  full_name='yandex.cloud.mdb.mysql.v1alpha.ResourcePreset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.mdb.mysql.v1alpha.ResourcePreset.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zone_ids', full_name='yandex.cloud.mdb.mysql.v1alpha.ResourcePreset.zone_ids', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cores', full_name='yandex.cloud.mdb.mysql.v1alpha.ResourcePreset.cores', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memory', full_name='yandex.cloud.mdb.mysql.v1alpha.ResourcePreset.memory', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=88,
  serialized_end=165,
)

DESCRIPTOR.message_types_by_name['ResourcePreset'] = _RESOURCEPRESET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResourcePreset = _reflection.GeneratedProtocolMessageType('ResourcePreset', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCEPRESET,
  '__module__' : 'yandex.cloud.mdb.mysql.v1alpha.resource_preset_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mysql.v1alpha.ResourcePreset)
  })
_sym_db.RegisterMessage(ResourcePreset)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
