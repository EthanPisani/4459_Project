# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: chat.proto
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
    'chat.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nchat.proto\x12\x04\x63hat\"\x1b\n\x0bJoinRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\'\n\x0cJoinResponse\x12\x17\n\x0fwelcome_message\x18\x01 \x01(\t\"*\n\x07Message\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\"\x07\n\x05\x45mpty2\x98\x01\n\x0b\x43hatService\x12-\n\x04Join\x12\x11.chat.JoinRequest\x1a\x12.chat.JoinResponse\x12)\n\x0bSendMessage\x12\r.chat.Message\x1a\x0b.chat.Empty\x12/\n\x0fReceiveMessages\x12\x0b.chat.Empty\x1a\r.chat.Message0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chat_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_JOINREQUEST']._serialized_start=20
  _globals['_JOINREQUEST']._serialized_end=47
  _globals['_JOINRESPONSE']._serialized_start=49
  _globals['_JOINRESPONSE']._serialized_end=88
  _globals['_MESSAGE']._serialized_start=90
  _globals['_MESSAGE']._serialized_end=132
  _globals['_EMPTY']._serialized_start=134
  _globals['_EMPTY']._serialized_end=141
  _globals['_CHATSERVICE']._serialized_start=144
  _globals['_CHATSERVICE']._serialized_end=296
# @@protoc_insertion_point(module_scope)
