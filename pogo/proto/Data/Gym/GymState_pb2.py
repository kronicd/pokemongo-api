# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Data/Gym/GymState.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Map.Fort import FortData_pb2 as Map_dot_Fort_dot_FortData__pb2
from Data.Gym import GymMembership_pb2 as Data_dot_Gym_dot_GymMembership__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Data/Gym/GymState.proto',
  package='POGOProtos.Data.Gym',
  syntax='proto3',
  serialized_pb=_b('\n\x17\x44\x61ta/Gym/GymState.proto\x12\x13POGOProtos.Data.Gym\x1a\x17Map/Fort/FortData.proto\x1a\x1c\x44\x61ta/Gym/GymMembership.proto\"u\n\x08GymState\x12\x30\n\tfort_data\x18\x01 \x01(\x0b\x32\x1d.POGOProtos.Map.Fort.FortData\x12\x37\n\x0bmemberships\x18\x02 \x03(\x0b\x32\".POGOProtos.Data.Gym.GymMembershipb\x06proto3')
  ,
  dependencies=[Map_dot_Fort_dot_FortData__pb2.DESCRIPTOR,Data_dot_Gym_dot_GymMembership__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GYMSTATE = _descriptor.Descriptor(
  name='GymState',
  full_name='POGOProtos.Data.Gym.GymState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fort_data', full_name='POGOProtos.Data.Gym.GymState.fort_data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='memberships', full_name='POGOProtos.Data.Gym.GymState.memberships', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=103,
  serialized_end=220,
)

_GYMSTATE.fields_by_name['fort_data'].message_type = Map_dot_Fort_dot_FortData__pb2._FORTDATA
_GYMSTATE.fields_by_name['memberships'].message_type = Data_dot_Gym_dot_GymMembership__pb2._GYMMEMBERSHIP
DESCRIPTOR.message_types_by_name['GymState'] = _GYMSTATE

GymState = _reflection.GeneratedProtocolMessageType('GymState', (_message.Message,), dict(
  DESCRIPTOR = _GYMSTATE,
  __module__ = 'Data.Gym.GymState_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Data.Gym.GymState)
  ))
_sym_db.RegisterMessage(GymState)


# @@protoc_insertion_point(module_scope)
