# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Networking/Responses/UseIncenseResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Inventory import AppliedItem_pb2 as Inventory_dot_AppliedItem__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Networking/Responses/UseIncenseResponse.proto',
  package='POGOProtos.Networking.Responses',
  syntax='proto3',
  serialized_pb=_b('\n-Networking/Responses/UseIncenseResponse.proto\x12\x1fPOGOProtos.Networking.Responses\x1a\x1bInventory/AppliedItem.proto\"\x87\x02\n\x12UseIncenseResponse\x12J\n\x06result\x18\x01 \x01(\x0e\x32:.POGOProtos.Networking.Responses.UseIncenseResponse.Result\x12:\n\x0f\x61pplied_incense\x18\x02 \x01(\x0b\x32!.POGOProtos.Inventory.AppliedItem\"i\n\x06Result\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x1a\n\x16INCENSE_ALREADY_ACTIVE\x10\x02\x12\x15\n\x11NONE_IN_INVENTORY\x10\x03\x12\x12\n\x0eLOCATION_UNSET\x10\x04\x62\x06proto3')
  ,
  dependencies=[Inventory_dot_AppliedItem__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_USEINCENSERESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='POGOProtos.Networking.Responses.UseIncenseResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INCENSE_ALREADY_ACTIVE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NONE_IN_INVENTORY', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCATION_UNSET', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=270,
  serialized_end=375,
)
_sym_db.RegisterEnumDescriptor(_USEINCENSERESPONSE_RESULT)


_USEINCENSERESPONSE = _descriptor.Descriptor(
  name='UseIncenseResponse',
  full_name='POGOProtos.Networking.Responses.UseIncenseResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='POGOProtos.Networking.Responses.UseIncenseResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='applied_incense', full_name='POGOProtos.Networking.Responses.UseIncenseResponse.applied_incense', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _USEINCENSERESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=375,
)

_USEINCENSERESPONSE.fields_by_name['result'].enum_type = _USEINCENSERESPONSE_RESULT
_USEINCENSERESPONSE.fields_by_name['applied_incense'].message_type = Inventory_dot_AppliedItem__pb2._APPLIEDITEM
_USEINCENSERESPONSE_RESULT.containing_type = _USEINCENSERESPONSE
DESCRIPTOR.message_types_by_name['UseIncenseResponse'] = _USEINCENSERESPONSE

UseIncenseResponse = _reflection.GeneratedProtocolMessageType('UseIncenseResponse', (_message.Message,), dict(
  DESCRIPTOR = _USEINCENSERESPONSE,
  __module__ = 'Networking.Responses.UseIncenseResponse_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Responses.UseIncenseResponse)
  ))
_sym_db.RegisterMessage(UseIncenseResponse)


# @@protoc_insertion_point(module_scope)
