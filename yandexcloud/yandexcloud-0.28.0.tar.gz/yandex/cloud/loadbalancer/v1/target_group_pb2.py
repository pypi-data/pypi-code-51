# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/loadbalancer/v1/target_group.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/loadbalancer/v1/target_group.proto',
  package='yandex.cloud.loadbalancer.v1',
  syntax='proto3',
  serialized_options=_b('\n yandex.cloud.api.loadbalancer.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/loadbalancer/v1;loadbalancer'),
  serialized_pb=_b('\n/yandex/cloud/loadbalancer/v1/target_group.proto\x12\x1cyandex.cloud.loadbalancer.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dyandex/cloud/validation.proto\"\xbf\x02\n\x0bTargetGroup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x45\n\x06labels\x18\x06 \x03(\x0b\x32\x35.yandex.cloud.loadbalancer.v1.TargetGroup.LabelsEntry\x12\x11\n\tregion_id\x18\x07 \x01(\t\x12\x35\n\x07targets\x18\t \x03(\x0b\x32$.yandex.cloud.loadbalancer.v1.Target\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"6\n\x06Target\x12\x1b\n\tsubnet_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\tBq\n yandex.cloud.api.loadbalancer.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/loadbalancer/v1;loadbalancerb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])




_TARGETGROUP_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='yandex.cloud.loadbalancer.v1.TargetGroup.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.loadbalancer.v1.TargetGroup.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.loadbalancer.v1.TargetGroup.LabelsEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=420,
  serialized_end=465,
)

_TARGETGROUP = _descriptor.Descriptor(
  name='TargetGroup',
  full_name='yandex.cloud.loadbalancer.v1.TargetGroup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.loadbalancer.v1.TargetGroup.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.loadbalancer.v1.TargetGroup.folder_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.loadbalancer.v1.TargetGroup.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.loadbalancer.v1.TargetGroup.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.loadbalancer.v1.TargetGroup.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='yandex.cloud.loadbalancer.v1.TargetGroup.labels', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='region_id', full_name='yandex.cloud.loadbalancer.v1.TargetGroup.region_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targets', full_name='yandex.cloud.loadbalancer.v1.TargetGroup.targets', index=7,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TARGETGROUP_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=146,
  serialized_end=465,
)


_TARGET = _descriptor.Descriptor(
  name='Target',
  full_name='yandex.cloud.loadbalancer.v1.Target',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='subnet_id', full_name='yandex.cloud.loadbalancer.v1.Target.subnet_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3101\004<=50'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='yandex.cloud.loadbalancer.v1.Target.address', index=1,
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
  serialized_start=467,
  serialized_end=521,
)

_TARGETGROUP_LABELSENTRY.containing_type = _TARGETGROUP
_TARGETGROUP.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TARGETGROUP.fields_by_name['labels'].message_type = _TARGETGROUP_LABELSENTRY
_TARGETGROUP.fields_by_name['targets'].message_type = _TARGET
DESCRIPTOR.message_types_by_name['TargetGroup'] = _TARGETGROUP
DESCRIPTOR.message_types_by_name['Target'] = _TARGET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TargetGroup = _reflection.GeneratedProtocolMessageType('TargetGroup', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _TARGETGROUP_LABELSENTRY,
    '__module__' : 'yandex.cloud.loadbalancer.v1.target_group_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.loadbalancer.v1.TargetGroup.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _TARGETGROUP,
  '__module__' : 'yandex.cloud.loadbalancer.v1.target_group_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.loadbalancer.v1.TargetGroup)
  })
_sym_db.RegisterMessage(TargetGroup)
_sym_db.RegisterMessage(TargetGroup.LabelsEntry)

Target = _reflection.GeneratedProtocolMessageType('Target', (_message.Message,), {
  'DESCRIPTOR' : _TARGET,
  '__module__' : 'yandex.cloud.loadbalancer.v1.target_group_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.loadbalancer.v1.Target)
  })
_sym_db.RegisterMessage(Target)


DESCRIPTOR._options = None
_TARGETGROUP_LABELSENTRY._options = None
_TARGET.fields_by_name['subnet_id']._options = None
# @@protoc_insertion_point(module_scope)
