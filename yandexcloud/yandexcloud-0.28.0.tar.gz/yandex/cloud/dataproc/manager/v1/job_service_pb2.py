# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/dataproc/manager/v1/job_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.dataproc.manager.v1 import job_pb2 as yandex_dot_cloud_dot_dataproc_dot_manager_dot_v1_dot_job__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/dataproc/manager/v1/job_service.proto',
  package='yandex.cloud.dataproc.manager.v1',
  syntax='proto3',
  serialized_options=_b('\n$yandex.cloud.api.dataproc.manager.v1ZUgithub.com/yandex-cloud/go-genproto/yandex/cloud/dataproc/manager/v1;dataproc_manager'),
  serialized_pb=_b('\n2yandex/cloud/dataproc/manager/v1/job_service.proto\x12 yandex.cloud.dataproc.manager.v1\x1a\x1dyandex/cloud/validation.proto\x1a*yandex/cloud/dataproc/manager/v1/job.proto\"\x89\x01\n\x0fListJobsRequest\x12\x1c\n\ncluster_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"`\n\x10ListJobsResponse\x12\x33\n\x04jobs\x18\x01 \x03(\x0b\x32%.yandex.cloud.dataproc.manager.v1.Job\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x8e\x01\n\x16UpdateJobStatusRequest\x12\x1c\n\ncluster_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x18\n\x06job_id\x18\x02 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12<\n\x06status\x18\x03 \x01(\x0e\x32,.yandex.cloud.dataproc.manager.v1.Job.Status\"\x19\n\x17UpdateJobStatusResponse2\x8b\x02\n\nJobService\x12u\n\nListActive\x12\x31.yandex.cloud.dataproc.manager.v1.ListJobsRequest\x1a\x32.yandex.cloud.dataproc.manager.v1.ListJobsResponse\"\x00\x12\x85\x01\n\x0cUpdateStatus\x12\x38.yandex.cloud.dataproc.manager.v1.UpdateJobStatusRequest\x1a\x39.yandex.cloud.dataproc.manager.v1.UpdateJobStatusResponse\"\x00\x42}\n$yandex.cloud.api.dataproc.manager.v1ZUgithub.com/yandex-cloud/go-genproto/yandex/cloud/dataproc/manager/v1;dataproc_managerb\x06proto3')
  ,
  dependencies=[yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_dataproc_dot_manager_dot_v1_dot_job__pb2.DESCRIPTOR,])




_LISTJOBSREQUEST = _descriptor.Descriptor(
  name='ListJobsRequest',
  full_name='yandex.cloud.dataproc.manager.v1.ListJobsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.dataproc.manager.v1.ListJobsRequest.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3101\004<=50'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='yandex.cloud.dataproc.manager.v1.ListJobsRequest.page_size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\372\3071\006<=1000'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='yandex.cloud.dataproc.manager.v1.ListJobsRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3101\005<=100'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter', full_name='yandex.cloud.dataproc.manager.v1.ListJobsRequest.filter', index=3,
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
  serialized_start=164,
  serialized_end=301,
)


_LISTJOBSRESPONSE = _descriptor.Descriptor(
  name='ListJobsResponse',
  full_name='yandex.cloud.dataproc.manager.v1.ListJobsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='jobs', full_name='yandex.cloud.dataproc.manager.v1.ListJobsResponse.jobs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='yandex.cloud.dataproc.manager.v1.ListJobsResponse.next_page_token', index=1,
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
  serialized_start=303,
  serialized_end=399,
)


_UPDATEJOBSTATUSREQUEST = _descriptor.Descriptor(
  name='UpdateJobStatusRequest',
  full_name='yandex.cloud.dataproc.manager.v1.UpdateJobStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.dataproc.manager.v1.UpdateJobStatusRequest.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3101\004<=50'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='job_id', full_name='yandex.cloud.dataproc.manager.v1.UpdateJobStatusRequest.job_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3101\004<=50'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='yandex.cloud.dataproc.manager.v1.UpdateJobStatusRequest.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
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
  serialized_start=402,
  serialized_end=544,
)


_UPDATEJOBSTATUSRESPONSE = _descriptor.Descriptor(
  name='UpdateJobStatusResponse',
  full_name='yandex.cloud.dataproc.manager.v1.UpdateJobStatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=546,
  serialized_end=571,
)

_LISTJOBSRESPONSE.fields_by_name['jobs'].message_type = yandex_dot_cloud_dot_dataproc_dot_manager_dot_v1_dot_job__pb2._JOB
_UPDATEJOBSTATUSREQUEST.fields_by_name['status'].enum_type = yandex_dot_cloud_dot_dataproc_dot_manager_dot_v1_dot_job__pb2._JOB_STATUS
DESCRIPTOR.message_types_by_name['ListJobsRequest'] = _LISTJOBSREQUEST
DESCRIPTOR.message_types_by_name['ListJobsResponse'] = _LISTJOBSRESPONSE
DESCRIPTOR.message_types_by_name['UpdateJobStatusRequest'] = _UPDATEJOBSTATUSREQUEST
DESCRIPTOR.message_types_by_name['UpdateJobStatusResponse'] = _UPDATEJOBSTATUSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListJobsRequest = _reflection.GeneratedProtocolMessageType('ListJobsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTJOBSREQUEST,
  '__module__' : 'yandex.cloud.dataproc.manager.v1.job_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.dataproc.manager.v1.ListJobsRequest)
  })
_sym_db.RegisterMessage(ListJobsRequest)

ListJobsResponse = _reflection.GeneratedProtocolMessageType('ListJobsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTJOBSRESPONSE,
  '__module__' : 'yandex.cloud.dataproc.manager.v1.job_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.dataproc.manager.v1.ListJobsResponse)
  })
_sym_db.RegisterMessage(ListJobsResponse)

UpdateJobStatusRequest = _reflection.GeneratedProtocolMessageType('UpdateJobStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEJOBSTATUSREQUEST,
  '__module__' : 'yandex.cloud.dataproc.manager.v1.job_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.dataproc.manager.v1.UpdateJobStatusRequest)
  })
_sym_db.RegisterMessage(UpdateJobStatusRequest)

UpdateJobStatusResponse = _reflection.GeneratedProtocolMessageType('UpdateJobStatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEJOBSTATUSRESPONSE,
  '__module__' : 'yandex.cloud.dataproc.manager.v1.job_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.dataproc.manager.v1.UpdateJobStatusResponse)
  })
_sym_db.RegisterMessage(UpdateJobStatusResponse)


DESCRIPTOR._options = None
_LISTJOBSREQUEST.fields_by_name['cluster_id']._options = None
_LISTJOBSREQUEST.fields_by_name['page_size']._options = None
_LISTJOBSREQUEST.fields_by_name['page_token']._options = None
_LISTJOBSREQUEST.fields_by_name['filter']._options = None
_UPDATEJOBSTATUSREQUEST.fields_by_name['cluster_id']._options = None
_UPDATEJOBSTATUSREQUEST.fields_by_name['job_id']._options = None

_JOBSERVICE = _descriptor.ServiceDescriptor(
  name='JobService',
  full_name='yandex.cloud.dataproc.manager.v1.JobService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=574,
  serialized_end=841,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListActive',
    full_name='yandex.cloud.dataproc.manager.v1.JobService.ListActive',
    index=0,
    containing_service=None,
    input_type=_LISTJOBSREQUEST,
    output_type=_LISTJOBSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateStatus',
    full_name='yandex.cloud.dataproc.manager.v1.JobService.UpdateStatus',
    index=1,
    containing_service=None,
    input_type=_UPDATEJOBSTATUSREQUEST,
    output_type=_UPDATEJOBSTATUSRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_JOBSERVICE)

DESCRIPTOR.services_by_name['JobService'] = _JOBSERVICE

# @@protoc_insertion_point(module_scope)
