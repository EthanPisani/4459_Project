# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: heartbeat.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'heartbeat.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fheartbeat.proto\x12\x04\x63hat\"%\n\x10HeartbeatRequest\x12\x11\n\tserver_id\x18\x01 \x01(\t\"%\n\x11HeartbeatResponse\x12\x10\n\x08received\x18\x01 \x01(\x08\"$\n\rSwitchRequest\x12\x13\n\x0bnew_primary\x18\x01 \x01(\t\"!\n\x0eSwitchResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32\x88\x01\n\tHeartbeat\x12@\n\rSendHeartbeat\x12\x16.chat.HeartbeatRequest\x1a\x17.chat.HeartbeatResponse\x12\x39\n\x0cSwitchServer\x12\x13.chat.SwitchRequest\x1a\x14.chat.SwitchResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'heartbeat_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_HEARTBEATREQUEST']._serialized_start=25
  _globals['_HEARTBEATREQUEST']._serialized_end=62
  _globals['_HEARTBEATRESPONSE']._serialized_start=64
  _globals['_HEARTBEATRESPONSE']._serialized_end=101
  _globals['_SWITCHREQUEST']._serialized_start=103
  _globals['_SWITCHREQUEST']._serialized_end=139
  _globals['_SWITCHRESPONSE']._serialized_start=141
  _globals['_SWITCHRESPONSE']._serialized_end=174
  _globals['_HEARTBEAT']._serialized_start=177
  _globals['_HEARTBEAT']._serialized_end=313
# @@protoc_insertion_point(module_scope)
