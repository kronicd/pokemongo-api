# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Networking/Requests/Messages/ClaimCodenameMessage.proto

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
  name='Networking/Requests/Messages/ClaimCodenameMessage.proto',
  package='POGOProtos.Networking.Requests.Messages',
  syntax='proto3',
  serialized_pb=_b('\n7Networking/Requests/Messages/ClaimCodenameMessage.proto\x12\'POGOProtos.Networking.Requests.Messages\"(\n\x14\x43laimCodenameMessage\x12\x10\n\x08\x63odename\x18\x01 \x01(\tb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CLAIMCODENAMEMESSAGE = _descriptor.Descriptor(
  name='ClaimCodenameMessage',
  full_name='POGOProtos.Networking.Requests.Messages.ClaimCodenameMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='codename', full_name='POGOProtos.Networking.Requests.Messages.ClaimCodenameMessage.codename', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=100,
  serialized_end=140,
)

DESCRIPTOR.message_types_by_name['ClaimCodenameMessage'] = _CLAIMCODENAMEMESSAGE

ClaimCodenameMessage = _reflection.GeneratedProtocolMessageType('ClaimCodenameMessage', (_message.Message,), dict(
  DESCRIPTOR = _CLAIMCODENAMEMESSAGE,
  __module__ = 'Networking.Requests.Messages.ClaimCodenameMessage_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Requests.Messages.ClaimCodenameMessage)
  ))
_sym_db.RegisterMessage(ClaimCodenameMessage)


# @@protoc_insertion_point(module_scope)
