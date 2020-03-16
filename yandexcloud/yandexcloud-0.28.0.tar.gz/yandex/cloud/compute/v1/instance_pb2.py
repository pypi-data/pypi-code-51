# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/compute/v1/instance.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/compute/v1/instance.proto',
  package='yandex.cloud.compute.v1',
  syntax='proto3',
  serialized_options=_b('\n\033yandex.cloud.api.compute.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;compute'),
  serialized_pb=_b('\n&yandex/cloud/compute/v1/instance.proto\x12\x17yandex.cloud.compute.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\xdd\x08\n\x08Instance\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12=\n\x06labels\x18\x06 \x03(\x0b\x32-.yandex.cloud.compute.v1.Instance.LabelsEntry\x12\x0f\n\x07zone_id\x18\x07 \x01(\t\x12\x13\n\x0bplatform_id\x18\x08 \x01(\t\x12\x35\n\tresources\x18\t \x01(\x0b\x32\".yandex.cloud.compute.v1.Resources\x12\x38\n\x06status\x18\n \x01(\x0e\x32(.yandex.cloud.compute.v1.Instance.Status\x12\x41\n\x08metadata\x18\x0b \x03(\x0b\x32/.yandex.cloud.compute.v1.Instance.MetadataEntry\x12\x38\n\tboot_disk\x18\x0c \x01(\x0b\x32%.yandex.cloud.compute.v1.AttachedDisk\x12>\n\x0fsecondary_disks\x18\r \x03(\x0b\x32%.yandex.cloud.compute.v1.AttachedDisk\x12\x45\n\x12network_interfaces\x18\x0e \x03(\x0b\x32).yandex.cloud.compute.v1.NetworkInterface\x12\x0c\n\x04\x66qdn\x18\x10 \x01(\t\x12\x44\n\x11scheduling_policy\x18\x11 \x01(\x0b\x32).yandex.cloud.compute.v1.SchedulingPolicy\x12\x1a\n\x12service_account_id\x18\x12 \x01(\t\x12\x42\n\x10network_settings\x18\x13 \x01(\x0b\x32(.yandex.cloud.compute.v1.NetworkSettings\x12\x42\n\x10placement_policy\x18\x14 \x01(\x0b\x32(.yandex.cloud.compute.v1.PlacementPolicy\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xac\x01\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x10\n\x0cPROVISIONING\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\x0c\n\x08STOPPING\x10\x03\x12\x0b\n\x07STOPPED\x10\x04\x12\x0c\n\x08STARTING\x10\x05\x12\x0e\n\nRESTARTING\x10\x06\x12\x0c\n\x08UPDATING\x10\x07\x12\t\n\x05\x45RROR\x10\x08\x12\x0b\n\x07\x43RASHED\x10\t\x12\x0c\n\x08\x44\x45LETING\x10\n\"O\n\tResources\x12\x0e\n\x06memory\x18\x01 \x01(\x03\x12\r\n\x05\x63ores\x18\x02 \x01(\x03\x12\x15\n\rcore_fraction\x18\x03 \x01(\x03\x12\x0c\n\x04gpus\x18\x04 \x01(\x03\"\xc0\x01\n\x0c\x41ttachedDisk\x12\x38\n\x04mode\x18\x01 \x01(\x0e\x32*.yandex.cloud.compute.v1.AttachedDisk.Mode\x12\x13\n\x0b\x64\x65vice_name\x18\x02 \x01(\t\x12\x13\n\x0b\x61uto_delete\x18\x03 \x01(\x08\x12\x0f\n\x07\x64isk_id\x18\x04 \x01(\t\";\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\r\n\tREAD_ONLY\x10\x01\x12\x0e\n\nREAD_WRITE\x10\x02\"\xef\x01\n\x10NetworkInterface\x12\r\n\x05index\x18\x01 \x01(\t\x12\x13\n\x0bmac_address\x18\x02 \x01(\t\x12\x11\n\tsubnet_id\x18\x03 \x01(\t\x12\x43\n\x12primary_v4_address\x18\x04 \x01(\x0b\x32\'.yandex.cloud.compute.v1.PrimaryAddress\x12\x43\n\x12primary_v6_address\x18\x05 \x01(\x0b\x32\'.yandex.cloud.compute.v1.PrimaryAddress\x12\x1a\n\x12security_group_ids\x18\x06 \x03(\t\"_\n\x0ePrimaryAddress\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12<\n\x0eone_to_one_nat\x18\x02 \x01(\x0b\x32$.yandex.cloud.compute.v1.OneToOneNat\"V\n\x0bOneToOneNat\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x36\n\nip_version\x18\x02 \x01(\x0e\x32\".yandex.cloud.compute.v1.IpVersion\"\'\n\x10SchedulingPolicy\x12\x13\n\x0bpreemptible\x18\x01 \x01(\x08\"\xae\x01\n\x0fNetworkSettings\x12;\n\x04type\x18\x01 \x01(\x0e\x32-.yandex.cloud.compute.v1.NetworkSettings.Type\"^\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0c\n\x08STANDARD\x10\x01\x12\x18\n\x14SOFTWARE_ACCELERATED\x10\x02\x12\x18\n\x14HARDWARE_ACCELERATED\x10\x03\"-\n\x0fPlacementPolicy\x12\x1a\n\x12placement_group_id\x18\x01 \x01(\t*;\n\tIpVersion\x12\x1a\n\x16IP_VERSION_UNSPECIFIED\x10\x00\x12\x08\n\x04IPV4\x10\x01\x12\x08\n\x04IPV6\x10\x02\x42\x62\n\x1byandex.cloud.api.compute.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;computeb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_IPVERSION = _descriptor.EnumDescriptor(
  name='IpVersion',
  full_name='yandex.cloud.compute.v1.IpVersion',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IP_VERSION_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IPV4', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IPV6', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2188,
  serialized_end=2247,
)
_sym_db.RegisterEnumDescriptor(_IPVERSION)

IpVersion = enum_type_wrapper.EnumTypeWrapper(_IPVERSION)
IP_VERSION_UNSPECIFIED = 0
IPV4 = 1
IPV6 = 2


_INSTANCE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='yandex.cloud.compute.v1.Instance.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROVISIONING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOPPING', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOPPED', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STARTING', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESTARTING', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATING', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CRASHED', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETING', index=10, number=10,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1046,
  serialized_end=1218,
)
_sym_db.RegisterEnumDescriptor(_INSTANCE_STATUS)

_ATTACHEDDISK_MODE = _descriptor.EnumDescriptor(
  name='Mode',
  full_name='yandex.cloud.compute.v1.AttachedDisk.Mode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MODE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READ_ONLY', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READ_WRITE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1435,
  serialized_end=1494,
)
_sym_db.RegisterEnumDescriptor(_ATTACHEDDISK_MODE)

_NETWORKSETTINGS_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='yandex.cloud.compute.v1.NetworkSettings.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STANDARD', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOFTWARE_ACCELERATED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HARDWARE_ACCELERATED', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2045,
  serialized_end=2139,
)
_sym_db.RegisterEnumDescriptor(_NETWORKSETTINGS_TYPE)


_INSTANCE_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='yandex.cloud.compute.v1.Instance.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.compute.v1.Instance.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.compute.v1.Instance.LabelsEntry.value', index=1,
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
  serialized_start=949,
  serialized_end=994,
)

_INSTANCE_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='yandex.cloud.compute.v1.Instance.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.compute.v1.Instance.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.compute.v1.Instance.MetadataEntry.value', index=1,
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
  serialized_start=996,
  serialized_end=1043,
)

_INSTANCE = _descriptor.Descriptor(
  name='Instance',
  full_name='yandex.cloud.compute.v1.Instance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.compute.v1.Instance.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.compute.v1.Instance.folder_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.compute.v1.Instance.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.compute.v1.Instance.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.compute.v1.Instance.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='yandex.cloud.compute.v1.Instance.labels', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zone_id', full_name='yandex.cloud.compute.v1.Instance.zone_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='platform_id', full_name='yandex.cloud.compute.v1.Instance.platform_id', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resources', full_name='yandex.cloud.compute.v1.Instance.resources', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='yandex.cloud.compute.v1.Instance.status', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='yandex.cloud.compute.v1.Instance.metadata', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='boot_disk', full_name='yandex.cloud.compute.v1.Instance.boot_disk', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secondary_disks', full_name='yandex.cloud.compute.v1.Instance.secondary_disks', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='network_interfaces', full_name='yandex.cloud.compute.v1.Instance.network_interfaces', index=13,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fqdn', full_name='yandex.cloud.compute.v1.Instance.fqdn', index=14,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scheduling_policy', full_name='yandex.cloud.compute.v1.Instance.scheduling_policy', index=15,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service_account_id', full_name='yandex.cloud.compute.v1.Instance.service_account_id', index=16,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='network_settings', full_name='yandex.cloud.compute.v1.Instance.network_settings', index=17,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='placement_policy', full_name='yandex.cloud.compute.v1.Instance.placement_policy', index=18,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_INSTANCE_LABELSENTRY, _INSTANCE_METADATAENTRY, ],
  enum_types=[
    _INSTANCE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=1218,
)


_RESOURCES = _descriptor.Descriptor(
  name='Resources',
  full_name='yandex.cloud.compute.v1.Resources',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='memory', full_name='yandex.cloud.compute.v1.Resources.memory', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cores', full_name='yandex.cloud.compute.v1.Resources.cores', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='core_fraction', full_name='yandex.cloud.compute.v1.Resources.core_fraction', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gpus', full_name='yandex.cloud.compute.v1.Resources.gpus', index=3,
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
  serialized_start=1220,
  serialized_end=1299,
)


_ATTACHEDDISK = _descriptor.Descriptor(
  name='AttachedDisk',
  full_name='yandex.cloud.compute.v1.AttachedDisk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mode', full_name='yandex.cloud.compute.v1.AttachedDisk.mode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_name', full_name='yandex.cloud.compute.v1.AttachedDisk.device_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auto_delete', full_name='yandex.cloud.compute.v1.AttachedDisk.auto_delete', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disk_id', full_name='yandex.cloud.compute.v1.AttachedDisk.disk_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ATTACHEDDISK_MODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1302,
  serialized_end=1494,
)


_NETWORKINTERFACE = _descriptor.Descriptor(
  name='NetworkInterface',
  full_name='yandex.cloud.compute.v1.NetworkInterface',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='yandex.cloud.compute.v1.NetworkInterface.index', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mac_address', full_name='yandex.cloud.compute.v1.NetworkInterface.mac_address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subnet_id', full_name='yandex.cloud.compute.v1.NetworkInterface.subnet_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='primary_v4_address', full_name='yandex.cloud.compute.v1.NetworkInterface.primary_v4_address', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='primary_v6_address', full_name='yandex.cloud.compute.v1.NetworkInterface.primary_v6_address', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='security_group_ids', full_name='yandex.cloud.compute.v1.NetworkInterface.security_group_ids', index=5,
      number=6, type=9, cpp_type=9, label=3,
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
  serialized_start=1497,
  serialized_end=1736,
)


_PRIMARYADDRESS = _descriptor.Descriptor(
  name='PrimaryAddress',
  full_name='yandex.cloud.compute.v1.PrimaryAddress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='yandex.cloud.compute.v1.PrimaryAddress.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='one_to_one_nat', full_name='yandex.cloud.compute.v1.PrimaryAddress.one_to_one_nat', index=1,
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
  serialized_start=1738,
  serialized_end=1833,
)


_ONETOONENAT = _descriptor.Descriptor(
  name='OneToOneNat',
  full_name='yandex.cloud.compute.v1.OneToOneNat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='yandex.cloud.compute.v1.OneToOneNat.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip_version', full_name='yandex.cloud.compute.v1.OneToOneNat.ip_version', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=1835,
  serialized_end=1921,
)


_SCHEDULINGPOLICY = _descriptor.Descriptor(
  name='SchedulingPolicy',
  full_name='yandex.cloud.compute.v1.SchedulingPolicy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='preemptible', full_name='yandex.cloud.compute.v1.SchedulingPolicy.preemptible', index=0,
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
  serialized_start=1923,
  serialized_end=1962,
)


_NETWORKSETTINGS = _descriptor.Descriptor(
  name='NetworkSettings',
  full_name='yandex.cloud.compute.v1.NetworkSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='yandex.cloud.compute.v1.NetworkSettings.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _NETWORKSETTINGS_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1965,
  serialized_end=2139,
)


_PLACEMENTPOLICY = _descriptor.Descriptor(
  name='PlacementPolicy',
  full_name='yandex.cloud.compute.v1.PlacementPolicy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='placement_group_id', full_name='yandex.cloud.compute.v1.PlacementPolicy.placement_group_id', index=0,
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
  serialized_start=2141,
  serialized_end=2186,
)

_INSTANCE_LABELSENTRY.containing_type = _INSTANCE
_INSTANCE_METADATAENTRY.containing_type = _INSTANCE
_INSTANCE.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_INSTANCE.fields_by_name['labels'].message_type = _INSTANCE_LABELSENTRY
_INSTANCE.fields_by_name['resources'].message_type = _RESOURCES
_INSTANCE.fields_by_name['status'].enum_type = _INSTANCE_STATUS
_INSTANCE.fields_by_name['metadata'].message_type = _INSTANCE_METADATAENTRY
_INSTANCE.fields_by_name['boot_disk'].message_type = _ATTACHEDDISK
_INSTANCE.fields_by_name['secondary_disks'].message_type = _ATTACHEDDISK
_INSTANCE.fields_by_name['network_interfaces'].message_type = _NETWORKINTERFACE
_INSTANCE.fields_by_name['scheduling_policy'].message_type = _SCHEDULINGPOLICY
_INSTANCE.fields_by_name['network_settings'].message_type = _NETWORKSETTINGS
_INSTANCE.fields_by_name['placement_policy'].message_type = _PLACEMENTPOLICY
_INSTANCE_STATUS.containing_type = _INSTANCE
_ATTACHEDDISK.fields_by_name['mode'].enum_type = _ATTACHEDDISK_MODE
_ATTACHEDDISK_MODE.containing_type = _ATTACHEDDISK
_NETWORKINTERFACE.fields_by_name['primary_v4_address'].message_type = _PRIMARYADDRESS
_NETWORKINTERFACE.fields_by_name['primary_v6_address'].message_type = _PRIMARYADDRESS
_PRIMARYADDRESS.fields_by_name['one_to_one_nat'].message_type = _ONETOONENAT
_ONETOONENAT.fields_by_name['ip_version'].enum_type = _IPVERSION
_NETWORKSETTINGS.fields_by_name['type'].enum_type = _NETWORKSETTINGS_TYPE
_NETWORKSETTINGS_TYPE.containing_type = _NETWORKSETTINGS
DESCRIPTOR.message_types_by_name['Instance'] = _INSTANCE
DESCRIPTOR.message_types_by_name['Resources'] = _RESOURCES
DESCRIPTOR.message_types_by_name['AttachedDisk'] = _ATTACHEDDISK
DESCRIPTOR.message_types_by_name['NetworkInterface'] = _NETWORKINTERFACE
DESCRIPTOR.message_types_by_name['PrimaryAddress'] = _PRIMARYADDRESS
DESCRIPTOR.message_types_by_name['OneToOneNat'] = _ONETOONENAT
DESCRIPTOR.message_types_by_name['SchedulingPolicy'] = _SCHEDULINGPOLICY
DESCRIPTOR.message_types_by_name['NetworkSettings'] = _NETWORKSETTINGS
DESCRIPTOR.message_types_by_name['PlacementPolicy'] = _PLACEMENTPOLICY
DESCRIPTOR.enum_types_by_name['IpVersion'] = _IPVERSION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Instance = _reflection.GeneratedProtocolMessageType('Instance', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _INSTANCE_LABELSENTRY,
    '__module__' : 'yandex.cloud.compute.v1.instance_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.Instance.LabelsEntry)
    })
  ,

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _INSTANCE_METADATAENTRY,
    '__module__' : 'yandex.cloud.compute.v1.instance_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.Instance.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _INSTANCE,
  '__module__' : 'yandex.cloud.compute.v1.instance_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.Instance)
  })
_sym_db.RegisterMessage(Instance)
_sym_db.RegisterMessage(Instance.LabelsEntry)
_sym_db.RegisterMessage(Instance.MetadataEntry)

Resources = _reflection.GeneratedProtocolMessageType('Resources', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCES,
  '__module__' : 'yandex.cloud.compute.v1.instance_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.Resources)
  })
_sym_db.RegisterMessage(Resources)

AttachedDisk = _reflection.GeneratedProtocolMessageType('AttachedDisk', (_message.Message,), {
  'DESCRIPTOR' : _ATTACHEDDISK,
  '__module__' : 'yandex.cloud.compute.v1.instance_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.AttachedDisk)
  })
_sym_db.RegisterMessage(AttachedDisk)

NetworkInterface = _reflection.GeneratedProtocolMessageType('NetworkInterface', (_message.Message,), {
  'DESCRIPTOR' : _NETWORKINTERFACE,
  '__module__' : 'yandex.cloud.compute.v1.instance_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.NetworkInterface)
  })
_sym_db.RegisterMessage(NetworkInterface)

PrimaryAddress = _reflection.GeneratedProtocolMessageType('PrimaryAddress', (_message.Message,), {
  'DESCRIPTOR' : _PRIMARYADDRESS,
  '__module__' : 'yandex.cloud.compute.v1.instance_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.PrimaryAddress)
  })
_sym_db.RegisterMessage(PrimaryAddress)

OneToOneNat = _reflection.GeneratedProtocolMessageType('OneToOneNat', (_message.Message,), {
  'DESCRIPTOR' : _ONETOONENAT,
  '__module__' : 'yandex.cloud.compute.v1.instance_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.OneToOneNat)
  })
_sym_db.RegisterMessage(OneToOneNat)

SchedulingPolicy = _reflection.GeneratedProtocolMessageType('SchedulingPolicy', (_message.Message,), {
  'DESCRIPTOR' : _SCHEDULINGPOLICY,
  '__module__' : 'yandex.cloud.compute.v1.instance_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.SchedulingPolicy)
  })
_sym_db.RegisterMessage(SchedulingPolicy)

NetworkSettings = _reflection.GeneratedProtocolMessageType('NetworkSettings', (_message.Message,), {
  'DESCRIPTOR' : _NETWORKSETTINGS,
  '__module__' : 'yandex.cloud.compute.v1.instance_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.NetworkSettings)
  })
_sym_db.RegisterMessage(NetworkSettings)

PlacementPolicy = _reflection.GeneratedProtocolMessageType('PlacementPolicy', (_message.Message,), {
  'DESCRIPTOR' : _PLACEMENTPOLICY,
  '__module__' : 'yandex.cloud.compute.v1.instance_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.PlacementPolicy)
  })
_sym_db.RegisterMessage(PlacementPolicy)


DESCRIPTOR._options = None
_INSTANCE_LABELSENTRY._options = None
_INSTANCE_METADATAENTRY._options = None
# @@protoc_insertion_point(module_scope)
