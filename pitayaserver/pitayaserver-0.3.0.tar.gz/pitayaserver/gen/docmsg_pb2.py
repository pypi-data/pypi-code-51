# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: docmsg.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='docmsg.proto',
  package='protos',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0c\x64ocmsg.proto\x12\x06protos\"\x1b\n\x06\x44ocMsg\x12\x11\n\tgetProtos\x18\x01 \x01(\x08\x62\x06proto3')
)




_DOCMSG = _descriptor.Descriptor(
  name='DocMsg',
  full_name='protos.DocMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='getProtos', full_name='protos.DocMsg.getProtos', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=24,
  serialized_end=51,
)

DESCRIPTOR.message_types_by_name['DocMsg'] = _DOCMSG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DocMsg = _reflection.GeneratedProtocolMessageType('DocMsg', (_message.Message,), dict(
  DESCRIPTOR = _DOCMSG,
  __module__ = 'docmsg_pb2'
  # @@protoc_insertion_point(class_scope:protos.DocMsg)
  ))
_sym_db.RegisterMessage(DocMsg)


# @@protoc_insertion_point(module_scope)
