# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Networking/Envelopes/Unknown6.proto

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
  name='Networking/Envelopes/Unknown6.proto',
  package='POGOProtos.Networking.Envelopes',
  syntax='proto3',
  serialized_pb=_b('\n#Networking/Envelopes/Unknown6.proto\x12\x1fPOGOProtos.Networking.Envelopes\"\x80\x01\n\x08Unknown6\x12\x10\n\x08unknown1\x18\x01 \x01(\x05\x12\x44\n\x08unknown2\x18\x02 \x01(\x0b\x32\x32.POGOProtos.Networking.Envelopes.Unknown6.Unknown2\x1a\x1c\n\x08Unknown2\x12\x10\n\x08unknown1\x18\x01 \x01(\x0c\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_UNKNOWN6_UNKNOWN2 = _descriptor.Descriptor(
  name='Unknown2',
  full_name='POGOProtos.Networking.Envelopes.Unknown6.Unknown2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unknown1', full_name='POGOProtos.Networking.Envelopes.Unknown6.Unknown2.unknown1', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=173,
  serialized_end=201,
)

_UNKNOWN6 = _descriptor.Descriptor(
  name='Unknown6',
  full_name='POGOProtos.Networking.Envelopes.Unknown6',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unknown1', full_name='POGOProtos.Networking.Envelopes.Unknown6.unknown1', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown2', full_name='POGOProtos.Networking.Envelopes.Unknown6.unknown2', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_UNKNOWN6_UNKNOWN2, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=73,
  serialized_end=201,
)

_UNKNOWN6_UNKNOWN2.containing_type = _UNKNOWN6
_UNKNOWN6.fields_by_name['unknown2'].message_type = _UNKNOWN6_UNKNOWN2
DESCRIPTOR.message_types_by_name['Unknown6'] = _UNKNOWN6

Unknown6 = _reflection.GeneratedProtocolMessageType('Unknown6', (_message.Message,), dict(

  Unknown2 = _reflection.GeneratedProtocolMessageType('Unknown2', (_message.Message,), dict(
    DESCRIPTOR = _UNKNOWN6_UNKNOWN2,
    __module__ = 'Networking.Envelopes.Unknown6_pb2'
    # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Envelopes.Unknown6.Unknown2)
    ))
  ,
  DESCRIPTOR = _UNKNOWN6,
  __module__ = 'Networking.Envelopes.Unknown6_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Envelopes.Unknown6)
  ))
_sym_db.RegisterMessage(Unknown6)
_sym_db.RegisterMessage(Unknown6.Unknown2)


# @@protoc_insertion_point(module_scope)
