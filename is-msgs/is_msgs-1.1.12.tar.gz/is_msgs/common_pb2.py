# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: is_msgs/common.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='is_msgs/common.proto',
  package='is.common',
  syntax='proto3',
  serialized_options=_b('\n\rcom.is.commonP\001'),
  serialized_pb=_b('\n\x14is_msgs/common.proto\x12\tis.common\x1a\x1egoogle/protobuf/wrappers.proto\"n\n\x10SamplingSettings\x12.\n\tfrequency\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12*\n\x05\x64\x65lay\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\"N\n\x0bSyncRequest\x12\x10\n\x08\x65ntities\x18\x01 \x03(\t\x12-\n\x08sampling\x18\x02 \x01(\x0b\x32\x1b.is.common.SamplingSettings\"\x1f\n\rFieldSelector\x12\x0e\n\x06\x66ields\x18\x01 \x03(\r\"Z\n\x05Shape\x12(\n\x04\x64ims\x18\x01 \x03(\x0b\x32\x1a.is.common.Shape.Dimension\x1a\'\n\tDimension\x12\x0c\n\x04size\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x9d\x01\n\x06Tensor\x12\x1f\n\x05shape\x18\x01 \x01(\x0b\x32\x10.is.common.Shape\x12!\n\x04type\x18\x02 \x01(\x0e\x32\x13.is.common.DataType\x12\x12\n\x06\x66loats\x18\x03 \x03(\x02\x42\x02\x10\x01\x12\x13\n\x07\x64oubles\x18\x04 \x03(\x01\x42\x02\x10\x01\x12\x12\n\x06ints32\x18\x05 \x03(\x05\x42\x02\x10\x01\x12\x12\n\x06ints64\x18\x06 \x03(\x03\x42\x02\x10\x01\"+\n\x08Position\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\"7\n\x0bOrientation\x12\x0b\n\x03yaw\x18\x01 \x01(\x02\x12\r\n\x05pitch\x18\x02 \x01(\x02\x12\x0c\n\x04roll\x18\x03 \x01(\x02\"Z\n\x04Pose\x12%\n\x08position\x18\x01 \x01(\x0b\x32\x13.is.common.Position\x12+\n\x0borientation\x18\x02 \x01(\x0b\x32\x16.is.common.Orientation\"(\n\x05Speed\x12\x0e\n\x06linear\x18\x01 \x01(\x02\x12\x0f\n\x07\x61ngular\x18\x02 \x01(\x02\"!\n\x0c\x43onsumerInfo\x12\x11\n\tconsumers\x18\x02 \x03(\t\"\x85\x01\n\x0c\x43onsumerList\x12/\n\x04info\x18\x01 \x03(\x0b\x32!.is.common.ConsumerList.InfoEntry\x1a\x44\n\tInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.is.common.ConsumerInfo:\x02\x38\x01*]\n\x08\x44\x61taType\x12\x10\n\x0cUNKNOWN_TYPE\x10\x00\x12\x0e\n\nFLOAT_TYPE\x10\x01\x12\x0f\n\x0b\x44OUBLE_TYPE\x10\x02\x12\x0e\n\nINT32_TYPE\x10\x03\x12\x0e\n\nINT64_TYPE\x10\x04\x42\x11\n\rcom.is.commonP\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])

_DATATYPE = _descriptor.EnumDescriptor(
  name='DataType',
  full_name='is.common.DataType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_TYPE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOAT_TYPE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOUBLE_TYPE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT32_TYPE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT64_TYPE', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=951,
  serialized_end=1044,
)
_sym_db.RegisterEnumDescriptor(_DATATYPE)

DataType = enum_type_wrapper.EnumTypeWrapper(_DATATYPE)
UNKNOWN_TYPE = 0
FLOAT_TYPE = 1
DOUBLE_TYPE = 2
INT32_TYPE = 3
INT64_TYPE = 4



_SAMPLINGSETTINGS = _descriptor.Descriptor(
  name='SamplingSettings',
  full_name='is.common.SamplingSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='frequency', full_name='is.common.SamplingSettings.frequency', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delay', full_name='is.common.SamplingSettings.delay', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=67,
  serialized_end=177,
)


_SYNCREQUEST = _descriptor.Descriptor(
  name='SyncRequest',
  full_name='is.common.SyncRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entities', full_name='is.common.SyncRequest.entities', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sampling', full_name='is.common.SyncRequest.sampling', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=179,
  serialized_end=257,
)


_FIELDSELECTOR = _descriptor.Descriptor(
  name='FieldSelector',
  full_name='is.common.FieldSelector',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fields', full_name='is.common.FieldSelector.fields', index=0,
      number=1, type=13, cpp_type=3, label=3,
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
  serialized_start=259,
  serialized_end=290,
)


_SHAPE_DIMENSION = _descriptor.Descriptor(
  name='Dimension',
  full_name='is.common.Shape.Dimension',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='size', full_name='is.common.Shape.Dimension.size', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='is.common.Shape.Dimension.name', index=1,
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
  serialized_start=343,
  serialized_end=382,
)

_SHAPE = _descriptor.Descriptor(
  name='Shape',
  full_name='is.common.Shape',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dims', full_name='is.common.Shape.dims', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SHAPE_DIMENSION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=292,
  serialized_end=382,
)


_TENSOR = _descriptor.Descriptor(
  name='Tensor',
  full_name='is.common.Tensor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shape', full_name='is.common.Tensor.shape', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='is.common.Tensor.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='floats', full_name='is.common.Tensor.floats', index=2,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='doubles', full_name='is.common.Tensor.doubles', index=3,
      number=4, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ints32', full_name='is.common.Tensor.ints32', index=4,
      number=5, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ints64', full_name='is.common.Tensor.ints64', index=5,
      number=6, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
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
  serialized_start=385,
  serialized_end=542,
)


_POSITION = _descriptor.Descriptor(
  name='Position',
  full_name='is.common.Position',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='is.common.Position.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='is.common.Position.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='is.common.Position.z', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=544,
  serialized_end=587,
)


_ORIENTATION = _descriptor.Descriptor(
  name='Orientation',
  full_name='is.common.Orientation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='yaw', full_name='is.common.Orientation.yaw', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pitch', full_name='is.common.Orientation.pitch', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roll', full_name='is.common.Orientation.roll', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=589,
  serialized_end=644,
)


_POSE = _descriptor.Descriptor(
  name='Pose',
  full_name='is.common.Pose',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='is.common.Pose.position', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orientation', full_name='is.common.Pose.orientation', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=646,
  serialized_end=736,
)


_SPEED = _descriptor.Descriptor(
  name='Speed',
  full_name='is.common.Speed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='linear', full_name='is.common.Speed.linear', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angular', full_name='is.common.Speed.angular', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=738,
  serialized_end=778,
)


_CONSUMERINFO = _descriptor.Descriptor(
  name='ConsumerInfo',
  full_name='is.common.ConsumerInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='consumers', full_name='is.common.ConsumerInfo.consumers', index=0,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=780,
  serialized_end=813,
)


_CONSUMERLIST_INFOENTRY = _descriptor.Descriptor(
  name='InfoEntry',
  full_name='is.common.ConsumerList.InfoEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='is.common.ConsumerList.InfoEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='is.common.ConsumerList.InfoEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=881,
  serialized_end=949,
)

_CONSUMERLIST = _descriptor.Descriptor(
  name='ConsumerList',
  full_name='is.common.ConsumerList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='info', full_name='is.common.ConsumerList.info', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CONSUMERLIST_INFOENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=816,
  serialized_end=949,
)

_SAMPLINGSETTINGS.fields_by_name['frequency'].message_type = google_dot_protobuf_dot_wrappers__pb2._FLOATVALUE
_SAMPLINGSETTINGS.fields_by_name['delay'].message_type = google_dot_protobuf_dot_wrappers__pb2._FLOATVALUE
_SYNCREQUEST.fields_by_name['sampling'].message_type = _SAMPLINGSETTINGS
_SHAPE_DIMENSION.containing_type = _SHAPE
_SHAPE.fields_by_name['dims'].message_type = _SHAPE_DIMENSION
_TENSOR.fields_by_name['shape'].message_type = _SHAPE
_TENSOR.fields_by_name['type'].enum_type = _DATATYPE
_POSE.fields_by_name['position'].message_type = _POSITION
_POSE.fields_by_name['orientation'].message_type = _ORIENTATION
_CONSUMERLIST_INFOENTRY.fields_by_name['value'].message_type = _CONSUMERINFO
_CONSUMERLIST_INFOENTRY.containing_type = _CONSUMERLIST
_CONSUMERLIST.fields_by_name['info'].message_type = _CONSUMERLIST_INFOENTRY
DESCRIPTOR.message_types_by_name['SamplingSettings'] = _SAMPLINGSETTINGS
DESCRIPTOR.message_types_by_name['SyncRequest'] = _SYNCREQUEST
DESCRIPTOR.message_types_by_name['FieldSelector'] = _FIELDSELECTOR
DESCRIPTOR.message_types_by_name['Shape'] = _SHAPE
DESCRIPTOR.message_types_by_name['Tensor'] = _TENSOR
DESCRIPTOR.message_types_by_name['Position'] = _POSITION
DESCRIPTOR.message_types_by_name['Orientation'] = _ORIENTATION
DESCRIPTOR.message_types_by_name['Pose'] = _POSE
DESCRIPTOR.message_types_by_name['Speed'] = _SPEED
DESCRIPTOR.message_types_by_name['ConsumerInfo'] = _CONSUMERINFO
DESCRIPTOR.message_types_by_name['ConsumerList'] = _CONSUMERLIST
DESCRIPTOR.enum_types_by_name['DataType'] = _DATATYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SamplingSettings = _reflection.GeneratedProtocolMessageType('SamplingSettings', (_message.Message,), dict(
  DESCRIPTOR = _SAMPLINGSETTINGS,
  __module__ = 'is_msgs.common_pb2'
  # @@protoc_insertion_point(class_scope:is.common.SamplingSettings)
  ))
_sym_db.RegisterMessage(SamplingSettings)

SyncRequest = _reflection.GeneratedProtocolMessageType('SyncRequest', (_message.Message,), dict(
  DESCRIPTOR = _SYNCREQUEST,
  __module__ = 'is_msgs.common_pb2'
  # @@protoc_insertion_point(class_scope:is.common.SyncRequest)
  ))
_sym_db.RegisterMessage(SyncRequest)

FieldSelector = _reflection.GeneratedProtocolMessageType('FieldSelector', (_message.Message,), dict(
  DESCRIPTOR = _FIELDSELECTOR,
  __module__ = 'is_msgs.common_pb2'
  # @@protoc_insertion_point(class_scope:is.common.FieldSelector)
  ))
_sym_db.RegisterMessage(FieldSelector)

Shape = _reflection.GeneratedProtocolMessageType('Shape', (_message.Message,), dict(

  Dimension = _reflection.GeneratedProtocolMessageType('Dimension', (_message.Message,), dict(
    DESCRIPTOR = _SHAPE_DIMENSION,
    __module__ = 'is_msgs.common_pb2'
    # @@protoc_insertion_point(class_scope:is.common.Shape.Dimension)
    ))
  ,
  DESCRIPTOR = _SHAPE,
  __module__ = 'is_msgs.common_pb2'
  # @@protoc_insertion_point(class_scope:is.common.Shape)
  ))
_sym_db.RegisterMessage(Shape)
_sym_db.RegisterMessage(Shape.Dimension)

Tensor = _reflection.GeneratedProtocolMessageType('Tensor', (_message.Message,), dict(
  DESCRIPTOR = _TENSOR,
  __module__ = 'is_msgs.common_pb2'
  # @@protoc_insertion_point(class_scope:is.common.Tensor)
  ))
_sym_db.RegisterMessage(Tensor)

Position = _reflection.GeneratedProtocolMessageType('Position', (_message.Message,), dict(
  DESCRIPTOR = _POSITION,
  __module__ = 'is_msgs.common_pb2'
  # @@protoc_insertion_point(class_scope:is.common.Position)
  ))
_sym_db.RegisterMessage(Position)

Orientation = _reflection.GeneratedProtocolMessageType('Orientation', (_message.Message,), dict(
  DESCRIPTOR = _ORIENTATION,
  __module__ = 'is_msgs.common_pb2'
  # @@protoc_insertion_point(class_scope:is.common.Orientation)
  ))
_sym_db.RegisterMessage(Orientation)

Pose = _reflection.GeneratedProtocolMessageType('Pose', (_message.Message,), dict(
  DESCRIPTOR = _POSE,
  __module__ = 'is_msgs.common_pb2'
  # @@protoc_insertion_point(class_scope:is.common.Pose)
  ))
_sym_db.RegisterMessage(Pose)

Speed = _reflection.GeneratedProtocolMessageType('Speed', (_message.Message,), dict(
  DESCRIPTOR = _SPEED,
  __module__ = 'is_msgs.common_pb2'
  # @@protoc_insertion_point(class_scope:is.common.Speed)
  ))
_sym_db.RegisterMessage(Speed)

ConsumerInfo = _reflection.GeneratedProtocolMessageType('ConsumerInfo', (_message.Message,), dict(
  DESCRIPTOR = _CONSUMERINFO,
  __module__ = 'is_msgs.common_pb2'
  # @@protoc_insertion_point(class_scope:is.common.ConsumerInfo)
  ))
_sym_db.RegisterMessage(ConsumerInfo)

ConsumerList = _reflection.GeneratedProtocolMessageType('ConsumerList', (_message.Message,), dict(

  InfoEntry = _reflection.GeneratedProtocolMessageType('InfoEntry', (_message.Message,), dict(
    DESCRIPTOR = _CONSUMERLIST_INFOENTRY,
    __module__ = 'is_msgs.common_pb2'
    # @@protoc_insertion_point(class_scope:is.common.ConsumerList.InfoEntry)
    ))
  ,
  DESCRIPTOR = _CONSUMERLIST,
  __module__ = 'is_msgs.common_pb2'
  # @@protoc_insertion_point(class_scope:is.common.ConsumerList)
  ))
_sym_db.RegisterMessage(ConsumerList)
_sym_db.RegisterMessage(ConsumerList.InfoEntry)


DESCRIPTOR._options = None
_TENSOR.fields_by_name['floats']._options = None
_TENSOR.fields_by_name['doubles']._options = None
_TENSOR.fields_by_name['ints32']._options = None
_TENSOR.fields_by_name['ints64']._options = None
_CONSUMERLIST_INFOENTRY._options = None
# @@protoc_insertion_point(module_scope)
