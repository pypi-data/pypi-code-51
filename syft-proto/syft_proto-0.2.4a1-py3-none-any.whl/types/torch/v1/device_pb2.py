# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: syft_proto/types/torch/v1/device.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='syft_proto/types/torch/v1/device.proto',
  package='syft_proto.types.torch.v1',
  syntax='proto3',
  serialized_options=_b('\n&org.openmined.syftproto.types.torch.v1'),
  serialized_pb=_b('\n&syft_proto/types/torch/v1/device.proto\x12\x19syft_proto.types.torch.v1\"\x1c\n\x06\x44\x65vice\x12\x12\n\x04type\x18\x01 \x01(\tR\x04typeB(\n&org.openmined.syftproto.types.torch.v1b\x06proto3')
)




_DEVICE = _descriptor.Descriptor(
  name='Device',
  full_name='syft_proto.types.torch.v1.Device',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='syft_proto.types.torch.v1.Device.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='type', file=DESCRIPTOR),
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
  serialized_start=69,
  serialized_end=97,
)

DESCRIPTOR.message_types_by_name['Device'] = _DEVICE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Device = _reflection.GeneratedProtocolMessageType('Device', (_message.Message,), {
  'DESCRIPTOR' : _DEVICE,
  '__module__' : 'syft_proto.types.torch.v1.device_pb2'
  # @@protoc_insertion_point(class_scope:syft_proto.types.torch.v1.Device)
  })
_sym_db.RegisterMessage(Device)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
