# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/compute/v1/snapshot_service.proto

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
from yandex.cloud.compute.v1 import snapshot_pb2 as yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/compute/v1/snapshot_service.proto',
  package='yandex.cloud.compute.v1',
  syntax='proto3',
  serialized_options=_b('\n\033yandex.cloud.api.compute.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;compute'),
  serialized_pb=_b('\n.yandex/cloud/compute/v1/snapshot_service.proto\x12\x17yandex.cloud.compute.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/compute/v1/snapshot.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"7\n\x12GetSnapshotRequest\x12!\n\x0bsnapshot_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\x91\x01\n\x14ListSnapshotsRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"f\n\x15ListSnapshotsResponse\x12\x34\n\tsnapshots\x18\x01 \x03(\x0b\x32!.yandex.cloud.compute.v1.Snapshot\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xf0\x02\n\x15\x43reateSnapshotRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\x07\x64isk_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x32\n\x04name\x18\x03 \x01(\tB$\xf2\xc7\x31 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x93\x01\n\x06labels\x18\x06 \x03(\x0b\x32:.yandex.cloud.compute.v1.CreateSnapshotRequest.LabelsEntryBG\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xf2\xc7\x31\x0f[-_./\\@0-9a-z]*\xb2\xc8\x31\x06\x1a\x04\x31-63\xb2\xc8\x31\x16\x12\x14[a-z][-_./\\@0-9a-z]*\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\">\n\x16\x43reateSnapshotMetadata\x12\x13\n\x0bsnapshot_id\x18\x01 \x01(\t\x12\x0f\n\x07\x64isk_id\x18\x02 \x01(\t\"\x84\x03\n\x15UpdateSnapshotRequest\x12!\n\x0bsnapshot_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x32\n\x04name\x18\x03 \x01(\tB$\xf2\xc7\x31 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x93\x01\n\x06labels\x18\x05 \x03(\x0b\x32:.yandex.cloud.compute.v1.UpdateSnapshotRequest.LabelsEntryBG\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xf2\xc7\x31\x0f[-_./\\@0-9a-z]*\xb2\xc8\x31\x06\x1a\x04\x31-63\xb2\xc8\x31\x16\x12\x14[a-z][-_./\\@0-9a-z]*\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"-\n\x16UpdateSnapshotMetadata\x12\x13\n\x0bsnapshot_id\x18\x01 \x01(\t\":\n\x15\x44\x65leteSnapshotRequest\x12!\n\x0bsnapshot_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"-\n\x16\x44\x65leteSnapshotMetadata\x12\x13\n\x0bsnapshot_id\x18\x01 \x01(\t\"\x80\x01\n\x1dListSnapshotOperationsRequest\x12!\n\x0bsnapshot_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"p\n\x1eListSnapshotOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xf1\x07\n\x0fSnapshotService\x12\x82\x01\n\x03Get\x12+.yandex.cloud.compute.v1.GetSnapshotRequest\x1a!.yandex.cloud.compute.v1.Snapshot\"+\x82\xd3\xe4\x93\x02%\x12#/compute/v1/snapshots/{snapshot_id}\x12\x84\x01\n\x04List\x12-.yandex.cloud.compute.v1.ListSnapshotsRequest\x1a..yandex.cloud.compute.v1.ListSnapshotsResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/compute/v1/snapshots\x12\xa3\x01\n\x06\x43reate\x12..yandex.cloud.compute.v1.CreateSnapshotRequest\x1a!.yandex.cloud.operation.Operation\"F\x82\xd3\xe4\x93\x02\x1a\"\x15/compute/v1/snapshots:\x01*\xb2\xd2*\"\n\x16\x43reateSnapshotMetadata\x12\x08Snapshot\x12\xb1\x01\n\x06Update\x12..yandex.cloud.compute.v1.UpdateSnapshotRequest\x1a!.yandex.cloud.operation.Operation\"T\x82\xd3\xe4\x93\x02(2#/compute/v1/snapshots/{snapshot_id}:\x01*\xb2\xd2*\"\n\x16UpdateSnapshotMetadata\x12\x08Snapshot\x12\xbb\x01\n\x06\x44\x65lete\x12..yandex.cloud.compute.v1.DeleteSnapshotRequest\x1a!.yandex.cloud.operation.Operation\"^\x82\xd3\xe4\x93\x02%*#/compute/v1/snapshots/{snapshot_id}\xb2\xd2*/\n\x16\x44\x65leteSnapshotMetadata\x12\x15google.protobuf.Empty\x12\xb9\x01\n\x0eListOperations\x12\x36.yandex.cloud.compute.v1.ListSnapshotOperationsRequest\x1a\x37.yandex.cloud.compute.v1.ListSnapshotOperationsResponse\"6\x82\xd3\xe4\x93\x02\x30\x12./compute/v1/snapshots/{snapshot_id}/operationsBb\n\x1byandex.cloud.api.compute.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;computeb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,yandex_dot_cloud_dot_api_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__pb2.DESCRIPTOR,yandex_dot_cloud_dot_operation_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])




_GETSNAPSHOTREQUEST = _descriptor.Descriptor(
  name='GetSnapshotRequest',
  full_name='yandex.cloud.compute.v1.GetSnapshotRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='snapshot_id', full_name='yandex.cloud.compute.v1.GetSnapshotRequest.snapshot_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001\212\3101\004<=50'), file=DESCRIPTOR),
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
  serialized_start=284,
  serialized_end=339,
)


_LISTSNAPSHOTSREQUEST = _descriptor.Descriptor(
  name='ListSnapshotsRequest',
  full_name='yandex.cloud.compute.v1.ListSnapshotsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.compute.v1.ListSnapshotsRequest.folder_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001\212\3101\004<=50'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='yandex.cloud.compute.v1.ListSnapshotsRequest.page_size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\372\3071\006<=1000'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='yandex.cloud.compute.v1.ListSnapshotsRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3101\005<=100'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter', full_name='yandex.cloud.compute.v1.ListSnapshotsRequest.filter', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3101\006<=1000'), file=DESCRIPTOR),
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
  serialized_start=342,
  serialized_end=487,
)


_LISTSNAPSHOTSRESPONSE = _descriptor.Descriptor(
  name='ListSnapshotsResponse',
  full_name='yandex.cloud.compute.v1.ListSnapshotsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='snapshots', full_name='yandex.cloud.compute.v1.ListSnapshotsResponse.snapshots', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='yandex.cloud.compute.v1.ListSnapshotsResponse.next_page_token', index=1,
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
  serialized_start=489,
  serialized_end=591,
)


_CREATESNAPSHOTREQUEST_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='yandex.cloud.compute.v1.CreateSnapshotRequest.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.compute.v1.CreateSnapshotRequest.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.compute.v1.CreateSnapshotRequest.LabelsEntry.value', index=1,
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
  serialized_start=917,
  serialized_end=962,
)

_CREATESNAPSHOTREQUEST = _descriptor.Descriptor(
  name='CreateSnapshotRequest',
  full_name='yandex.cloud.compute.v1.CreateSnapshotRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.compute.v1.CreateSnapshotRequest.folder_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001\212\3101\004<=50'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disk_id', full_name='yandex.cloud.compute.v1.CreateSnapshotRequest.disk_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001\212\3101\004<=50'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.compute.v1.CreateSnapshotRequest.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\3071 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.compute.v1.CreateSnapshotRequest.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3101\005<=256'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='yandex.cloud.compute.v1.CreateSnapshotRequest.labels', index=4,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\202\3101\004<=64\212\3101\004<=63\362\3071\017[-_./\\@0-9a-z]*\262\3101\006\032\0041-63\262\3101\026\022\024[a-z][-_./\\@0-9a-z]*'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CREATESNAPSHOTREQUEST_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=594,
  serialized_end=962,
)


_CREATESNAPSHOTMETADATA = _descriptor.Descriptor(
  name='CreateSnapshotMetadata',
  full_name='yandex.cloud.compute.v1.CreateSnapshotMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='snapshot_id', full_name='yandex.cloud.compute.v1.CreateSnapshotMetadata.snapshot_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disk_id', full_name='yandex.cloud.compute.v1.CreateSnapshotMetadata.disk_id', index=1,
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
  serialized_start=964,
  serialized_end=1026,
)


_UPDATESNAPSHOTREQUEST_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='yandex.cloud.compute.v1.UpdateSnapshotRequest.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.compute.v1.UpdateSnapshotRequest.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.compute.v1.UpdateSnapshotRequest.LabelsEntry.value', index=1,
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
  serialized_start=917,
  serialized_end=962,
)

_UPDATESNAPSHOTREQUEST = _descriptor.Descriptor(
  name='UpdateSnapshotRequest',
  full_name='yandex.cloud.compute.v1.UpdateSnapshotRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='snapshot_id', full_name='yandex.cloud.compute.v1.UpdateSnapshotRequest.snapshot_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001\212\3101\004<=50'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='yandex.cloud.compute.v1.UpdateSnapshotRequest.update_mask', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.compute.v1.UpdateSnapshotRequest.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\3071 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.compute.v1.UpdateSnapshotRequest.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3101\005<=256'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='yandex.cloud.compute.v1.UpdateSnapshotRequest.labels', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\202\3101\004<=64\212\3101\004<=63\362\3071\017[-_./\\@0-9a-z]*\262\3101\006\032\0041-63\262\3101\026\022\024[a-z][-_./\\@0-9a-z]*'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_UPDATESNAPSHOTREQUEST_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1029,
  serialized_end=1417,
)


_UPDATESNAPSHOTMETADATA = _descriptor.Descriptor(
  name='UpdateSnapshotMetadata',
  full_name='yandex.cloud.compute.v1.UpdateSnapshotMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='snapshot_id', full_name='yandex.cloud.compute.v1.UpdateSnapshotMetadata.snapshot_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=1419,
  serialized_end=1464,
)


_DELETESNAPSHOTREQUEST = _descriptor.Descriptor(
  name='DeleteSnapshotRequest',
  full_name='yandex.cloud.compute.v1.DeleteSnapshotRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='snapshot_id', full_name='yandex.cloud.compute.v1.DeleteSnapshotRequest.snapshot_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001\212\3101\004<=50'), file=DESCRIPTOR),
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
  serialized_start=1466,
  serialized_end=1524,
)


_DELETESNAPSHOTMETADATA = _descriptor.Descriptor(
  name='DeleteSnapshotMetadata',
  full_name='yandex.cloud.compute.v1.DeleteSnapshotMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='snapshot_id', full_name='yandex.cloud.compute.v1.DeleteSnapshotMetadata.snapshot_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=1526,
  serialized_end=1571,
)


_LISTSNAPSHOTOPERATIONSREQUEST = _descriptor.Descriptor(
  name='ListSnapshotOperationsRequest',
  full_name='yandex.cloud.compute.v1.ListSnapshotOperationsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='snapshot_id', full_name='yandex.cloud.compute.v1.ListSnapshotOperationsRequest.snapshot_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001\212\3101\004<=50'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='yandex.cloud.compute.v1.ListSnapshotOperationsRequest.page_size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\372\3071\006<=1000'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='yandex.cloud.compute.v1.ListSnapshotOperationsRequest.page_token', index=2,
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
  serialized_start=1574,
  serialized_end=1702,
)


_LISTSNAPSHOTOPERATIONSRESPONSE = _descriptor.Descriptor(
  name='ListSnapshotOperationsResponse',
  full_name='yandex.cloud.compute.v1.ListSnapshotOperationsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operations', full_name='yandex.cloud.compute.v1.ListSnapshotOperationsResponse.operations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='yandex.cloud.compute.v1.ListSnapshotOperationsResponse.next_page_token', index=1,
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
  serialized_start=1704,
  serialized_end=1816,
)

_LISTSNAPSHOTSRESPONSE.fields_by_name['snapshots'].message_type = yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__pb2._SNAPSHOT
_CREATESNAPSHOTREQUEST_LABELSENTRY.containing_type = _CREATESNAPSHOTREQUEST
_CREATESNAPSHOTREQUEST.fields_by_name['labels'].message_type = _CREATESNAPSHOTREQUEST_LABELSENTRY
_UPDATESNAPSHOTREQUEST_LABELSENTRY.containing_type = _UPDATESNAPSHOTREQUEST
_UPDATESNAPSHOTREQUEST.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_UPDATESNAPSHOTREQUEST.fields_by_name['labels'].message_type = _UPDATESNAPSHOTREQUEST_LABELSENTRY
_LISTSNAPSHOTOPERATIONSRESPONSE.fields_by_name['operations'].message_type = yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION
DESCRIPTOR.message_types_by_name['GetSnapshotRequest'] = _GETSNAPSHOTREQUEST
DESCRIPTOR.message_types_by_name['ListSnapshotsRequest'] = _LISTSNAPSHOTSREQUEST
DESCRIPTOR.message_types_by_name['ListSnapshotsResponse'] = _LISTSNAPSHOTSRESPONSE
DESCRIPTOR.message_types_by_name['CreateSnapshotRequest'] = _CREATESNAPSHOTREQUEST
DESCRIPTOR.message_types_by_name['CreateSnapshotMetadata'] = _CREATESNAPSHOTMETADATA
DESCRIPTOR.message_types_by_name['UpdateSnapshotRequest'] = _UPDATESNAPSHOTREQUEST
DESCRIPTOR.message_types_by_name['UpdateSnapshotMetadata'] = _UPDATESNAPSHOTMETADATA
DESCRIPTOR.message_types_by_name['DeleteSnapshotRequest'] = _DELETESNAPSHOTREQUEST
DESCRIPTOR.message_types_by_name['DeleteSnapshotMetadata'] = _DELETESNAPSHOTMETADATA
DESCRIPTOR.message_types_by_name['ListSnapshotOperationsRequest'] = _LISTSNAPSHOTOPERATIONSREQUEST
DESCRIPTOR.message_types_by_name['ListSnapshotOperationsResponse'] = _LISTSNAPSHOTOPERATIONSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetSnapshotRequest = _reflection.GeneratedProtocolMessageType('GetSnapshotRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSNAPSHOTREQUEST,
  '__module__' : 'yandex.cloud.compute.v1.snapshot_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.GetSnapshotRequest)
  })
_sym_db.RegisterMessage(GetSnapshotRequest)

ListSnapshotsRequest = _reflection.GeneratedProtocolMessageType('ListSnapshotsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTSNAPSHOTSREQUEST,
  '__module__' : 'yandex.cloud.compute.v1.snapshot_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.ListSnapshotsRequest)
  })
_sym_db.RegisterMessage(ListSnapshotsRequest)

ListSnapshotsResponse = _reflection.GeneratedProtocolMessageType('ListSnapshotsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTSNAPSHOTSRESPONSE,
  '__module__' : 'yandex.cloud.compute.v1.snapshot_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.ListSnapshotsResponse)
  })
_sym_db.RegisterMessage(ListSnapshotsResponse)

CreateSnapshotRequest = _reflection.GeneratedProtocolMessageType('CreateSnapshotRequest', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CREATESNAPSHOTREQUEST_LABELSENTRY,
    '__module__' : 'yandex.cloud.compute.v1.snapshot_service_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.CreateSnapshotRequest.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _CREATESNAPSHOTREQUEST,
  '__module__' : 'yandex.cloud.compute.v1.snapshot_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.CreateSnapshotRequest)
  })
_sym_db.RegisterMessage(CreateSnapshotRequest)
_sym_db.RegisterMessage(CreateSnapshotRequest.LabelsEntry)

CreateSnapshotMetadata = _reflection.GeneratedProtocolMessageType('CreateSnapshotMetadata', (_message.Message,), {
  'DESCRIPTOR' : _CREATESNAPSHOTMETADATA,
  '__module__' : 'yandex.cloud.compute.v1.snapshot_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.CreateSnapshotMetadata)
  })
_sym_db.RegisterMessage(CreateSnapshotMetadata)

UpdateSnapshotRequest = _reflection.GeneratedProtocolMessageType('UpdateSnapshotRequest', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _UPDATESNAPSHOTREQUEST_LABELSENTRY,
    '__module__' : 'yandex.cloud.compute.v1.snapshot_service_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.UpdateSnapshotRequest.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _UPDATESNAPSHOTREQUEST,
  '__module__' : 'yandex.cloud.compute.v1.snapshot_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.UpdateSnapshotRequest)
  })
_sym_db.RegisterMessage(UpdateSnapshotRequest)
_sym_db.RegisterMessage(UpdateSnapshotRequest.LabelsEntry)

UpdateSnapshotMetadata = _reflection.GeneratedProtocolMessageType('UpdateSnapshotMetadata', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESNAPSHOTMETADATA,
  '__module__' : 'yandex.cloud.compute.v1.snapshot_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.UpdateSnapshotMetadata)
  })
_sym_db.RegisterMessage(UpdateSnapshotMetadata)

DeleteSnapshotRequest = _reflection.GeneratedProtocolMessageType('DeleteSnapshotRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETESNAPSHOTREQUEST,
  '__module__' : 'yandex.cloud.compute.v1.snapshot_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.DeleteSnapshotRequest)
  })
_sym_db.RegisterMessage(DeleteSnapshotRequest)

DeleteSnapshotMetadata = _reflection.GeneratedProtocolMessageType('DeleteSnapshotMetadata', (_message.Message,), {
  'DESCRIPTOR' : _DELETESNAPSHOTMETADATA,
  '__module__' : 'yandex.cloud.compute.v1.snapshot_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.DeleteSnapshotMetadata)
  })
_sym_db.RegisterMessage(DeleteSnapshotMetadata)

ListSnapshotOperationsRequest = _reflection.GeneratedProtocolMessageType('ListSnapshotOperationsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTSNAPSHOTOPERATIONSREQUEST,
  '__module__' : 'yandex.cloud.compute.v1.snapshot_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.ListSnapshotOperationsRequest)
  })
_sym_db.RegisterMessage(ListSnapshotOperationsRequest)

ListSnapshotOperationsResponse = _reflection.GeneratedProtocolMessageType('ListSnapshotOperationsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTSNAPSHOTOPERATIONSRESPONSE,
  '__module__' : 'yandex.cloud.compute.v1.snapshot_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.ListSnapshotOperationsResponse)
  })
_sym_db.RegisterMessage(ListSnapshotOperationsResponse)


DESCRIPTOR._options = None
_GETSNAPSHOTREQUEST.fields_by_name['snapshot_id']._options = None
_LISTSNAPSHOTSREQUEST.fields_by_name['folder_id']._options = None
_LISTSNAPSHOTSREQUEST.fields_by_name['page_size']._options = None
_LISTSNAPSHOTSREQUEST.fields_by_name['page_token']._options = None
_LISTSNAPSHOTSREQUEST.fields_by_name['filter']._options = None
_CREATESNAPSHOTREQUEST_LABELSENTRY._options = None
_CREATESNAPSHOTREQUEST.fields_by_name['folder_id']._options = None
_CREATESNAPSHOTREQUEST.fields_by_name['disk_id']._options = None
_CREATESNAPSHOTREQUEST.fields_by_name['name']._options = None
_CREATESNAPSHOTREQUEST.fields_by_name['description']._options = None
_CREATESNAPSHOTREQUEST.fields_by_name['labels']._options = None
_UPDATESNAPSHOTREQUEST_LABELSENTRY._options = None
_UPDATESNAPSHOTREQUEST.fields_by_name['snapshot_id']._options = None
_UPDATESNAPSHOTREQUEST.fields_by_name['name']._options = None
_UPDATESNAPSHOTREQUEST.fields_by_name['description']._options = None
_UPDATESNAPSHOTREQUEST.fields_by_name['labels']._options = None
_DELETESNAPSHOTREQUEST.fields_by_name['snapshot_id']._options = None
_LISTSNAPSHOTOPERATIONSREQUEST.fields_by_name['snapshot_id']._options = None
_LISTSNAPSHOTOPERATIONSREQUEST.fields_by_name['page_size']._options = None
_LISTSNAPSHOTOPERATIONSREQUEST.fields_by_name['page_token']._options = None

_SNAPSHOTSERVICE = _descriptor.ServiceDescriptor(
  name='SnapshotService',
  full_name='yandex.cloud.compute.v1.SnapshotService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1819,
  serialized_end=2828,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='yandex.cloud.compute.v1.SnapshotService.Get',
    index=0,
    containing_service=None,
    input_type=_GETSNAPSHOTREQUEST,
    output_type=yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__pb2._SNAPSHOT,
    serialized_options=_b('\202\323\344\223\002%\022#/compute/v1/snapshots/{snapshot_id}'),
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='yandex.cloud.compute.v1.SnapshotService.List',
    index=1,
    containing_service=None,
    input_type=_LISTSNAPSHOTSREQUEST,
    output_type=_LISTSNAPSHOTSRESPONSE,
    serialized_options=_b('\202\323\344\223\002\027\022\025/compute/v1/snapshots'),
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='yandex.cloud.compute.v1.SnapshotService.Create',
    index=2,
    containing_service=None,
    input_type=_CREATESNAPSHOTREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=_b('\202\323\344\223\002\032\"\025/compute/v1/snapshots:\001*\262\322*\"\n\026CreateSnapshotMetadata\022\010Snapshot'),
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='yandex.cloud.compute.v1.SnapshotService.Update',
    index=3,
    containing_service=None,
    input_type=_UPDATESNAPSHOTREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=_b('\202\323\344\223\002(2#/compute/v1/snapshots/{snapshot_id}:\001*\262\322*\"\n\026UpdateSnapshotMetadata\022\010Snapshot'),
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='yandex.cloud.compute.v1.SnapshotService.Delete',
    index=4,
    containing_service=None,
    input_type=_DELETESNAPSHOTREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=_b('\202\323\344\223\002%*#/compute/v1/snapshots/{snapshot_id}\262\322*/\n\026DeleteSnapshotMetadata\022\025google.protobuf.Empty'),
  ),
  _descriptor.MethodDescriptor(
    name='ListOperations',
    full_name='yandex.cloud.compute.v1.SnapshotService.ListOperations',
    index=5,
    containing_service=None,
    input_type=_LISTSNAPSHOTOPERATIONSREQUEST,
    output_type=_LISTSNAPSHOTOPERATIONSRESPONSE,
    serialized_options=_b('\202\323\344\223\0020\022./compute/v1/snapshots/{snapshot_id}/operations'),
  ),
])
_sym_db.RegisterServiceDescriptor(_SNAPSHOTSERVICE)

DESCRIPTOR.services_by_name['SnapshotService'] = _SNAPSHOTSERVICE

# @@protoc_insertion_point(module_scope)
