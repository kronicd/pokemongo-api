# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Networking/Responses/CheckAwardedBadgesResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Enums import BadgeType_pb2 as Enums_dot_BadgeType__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Networking/Responses/CheckAwardedBadgesResponse.proto',
  package='POGOProtos.Networking.Responses',
  syntax='proto3',
  serialized_pb=_b('\n5Networking/Responses/CheckAwardedBadgesResponse.proto\x12\x1fPOGOProtos.Networking.Responses\x1a\x15\x45nums/BadgeType.proto\"\x80\x01\n\x1a\x43heckAwardedBadgesResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x33\n\x0e\x61warded_badges\x18\x02 \x03(\x0e\x32\x1b.POGOProtos.Enums.BadgeType\x12\x1c\n\x14\x61warded_badge_levels\x18\x03 \x03(\x05\x62\x06proto3')
  ,
  dependencies=[Enums_dot_BadgeType__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CHECKAWARDEDBADGESRESPONSE = _descriptor.Descriptor(
  name='CheckAwardedBadgesResponse',
  full_name='POGOProtos.Networking.Responses.CheckAwardedBadgesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='POGOProtos.Networking.Responses.CheckAwardedBadgesResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='awarded_badges', full_name='POGOProtos.Networking.Responses.CheckAwardedBadgesResponse.awarded_badges', index=1,
      number=2, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='awarded_badge_levels', full_name='POGOProtos.Networking.Responses.CheckAwardedBadgesResponse.awarded_badge_levels', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=114,
  serialized_end=242,
)

_CHECKAWARDEDBADGESRESPONSE.fields_by_name['awarded_badges'].enum_type = Enums_dot_BadgeType__pb2._BADGETYPE
DESCRIPTOR.message_types_by_name['CheckAwardedBadgesResponse'] = _CHECKAWARDEDBADGESRESPONSE

CheckAwardedBadgesResponse = _reflection.GeneratedProtocolMessageType('CheckAwardedBadgesResponse', (_message.Message,), dict(
  DESCRIPTOR = _CHECKAWARDEDBADGESRESPONSE,
  __module__ = 'Networking.Responses.CheckAwardedBadgesResponse_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Responses.CheckAwardedBadgesResponse)
  ))
_sym_db.RegisterMessage(CheckAwardedBadgesResponse)


# @@protoc_insertion_point(module_scope)
