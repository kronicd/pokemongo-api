# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Networking/Responses/GetSuggestedCodenamesResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Networking/Responses/GetSuggestedCodenamesResponse.proto',
  package='POGOProtos.Networking.Responses',
  syntax='proto3',
  serialized_pb=_b('\n8Networking/Responses/GetSuggestedCodenamesResponse.proto\x12\x1fPOGOProtos.Networking.Responses\"C\n\x1dGetSuggestedCodenamesResponse\x12\x11\n\tcodenames\x18\x01 \x03(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GETSUGGESTEDCODENAMESRESPONSE = _descriptor.Descriptor(
  name='GetSuggestedCodenamesResponse',
  full_name='POGOProtos.Networking.Responses.GetSuggestedCodenamesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='codenames', full_name='POGOProtos.Networking.Responses.GetSuggestedCodenamesResponse.codenames', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='success', full_name='POGOProtos.Networking.Responses.GetSuggestedCodenamesResponse.success', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=93,
  serialized_end=160,
)

DESCRIPTOR.message_types_by_name['GetSuggestedCodenamesResponse'] = _GETSUGGESTEDCODENAMESRESPONSE

GetSuggestedCodenamesResponse = _reflection.GeneratedProtocolMessageType('GetSuggestedCodenamesResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETSUGGESTEDCODENAMESRESPONSE,
  __module__ = 'Networking.Responses.GetSuggestedCodenamesResponse_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Responses.GetSuggestedCodenamesResponse)
  ))
_sym_db.RegisterMessage(GetSuggestedCodenamesResponse)


# @@protoc_insertion_point(module_scope)
