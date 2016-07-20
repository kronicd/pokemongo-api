# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Networking/Responses/FortDetailsResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Data import PokemonData_pb2 as Data_dot_PokemonData__pb2
from Enums import TeamColor_pb2 as Enums_dot_TeamColor__pb2
from Map.Fort import FortType_pb2 as Map_dot_Fort_dot_FortType__pb2
from Map.Fort import FortModifier_pb2 as Map_dot_Fort_dot_FortModifier__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Networking/Responses/FortDetailsResponse.proto',
  package='POGOProtos.Networking.Responses',
  syntax='proto3',
  serialized_pb=_b('\n.Networking/Responses/FortDetailsResponse.proto\x12\x1fPOGOProtos.Networking.Responses\x1a\x16\x44\x61ta/PokemonData.proto\x1a\x15\x45nums/TeamColor.proto\x1a\x17Map/Fort/FortType.proto\x1a\x1bMap/Fort/FortModifier.proto\"\xfc\x02\n\x13\x46ortDetailsResponse\x12\x0f\n\x07\x66ort_id\x18\x01 \x01(\t\x12/\n\nteam_color\x18\x02 \x01(\x0e\x32\x1b.POGOProtos.Enums.TeamColor\x12\x32\n\x0cpokemon_data\x18\x03 \x01(\x0b\x32\x1c.POGOProtos.Data.PokemonData\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x12\n\nimage_urls\x18\x05 \x03(\t\x12\n\n\x02\x66p\x18\x06 \x01(\x05\x12\x0f\n\x07stamina\x18\x07 \x01(\x05\x12\x13\n\x0bmax_stamina\x18\x08 \x01(\x05\x12+\n\x04type\x18\t \x01(\x0e\x32\x1d.POGOProtos.Map.Fort.FortType\x12\x10\n\x08latitude\x18\n \x01(\x01\x12\x11\n\tlongitude\x18\x0b \x01(\x01\x12\x13\n\x0b\x64\x65scription\x18\x0c \x01(\t\x12\x34\n\tmodifiers\x18\r \x03(\x0b\x32!.POGOProtos.Map.Fort.FortModifierb\x06proto3')
  ,
  dependencies=[Data_dot_PokemonData__pb2.DESCRIPTOR,Enums_dot_TeamColor__pb2.DESCRIPTOR,Map_dot_Fort_dot_FortType__pb2.DESCRIPTOR,Map_dot_Fort_dot_FortModifier__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_FORTDETAILSRESPONSE = _descriptor.Descriptor(
  name='FortDetailsResponse',
  full_name='POGOProtos.Networking.Responses.FortDetailsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fort_id', full_name='POGOProtos.Networking.Responses.FortDetailsResponse.fort_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='team_color', full_name='POGOProtos.Networking.Responses.FortDetailsResponse.team_color', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_data', full_name='POGOProtos.Networking.Responses.FortDetailsResponse.pokemon_data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='POGOProtos.Networking.Responses.FortDetailsResponse.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='image_urls', full_name='POGOProtos.Networking.Responses.FortDetailsResponse.image_urls', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fp', full_name='POGOProtos.Networking.Responses.FortDetailsResponse.fp', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stamina', full_name='POGOProtos.Networking.Responses.FortDetailsResponse.stamina', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_stamina', full_name='POGOProtos.Networking.Responses.FortDetailsResponse.max_stamina', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='POGOProtos.Networking.Responses.FortDetailsResponse.type', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='POGOProtos.Networking.Responses.FortDetailsResponse.latitude', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='POGOProtos.Networking.Responses.FortDetailsResponse.longitude', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='POGOProtos.Networking.Responses.FortDetailsResponse.description', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='modifiers', full_name='POGOProtos.Networking.Responses.FortDetailsResponse.modifiers', index=12,
      number=13, type=11, cpp_type=10, label=3,
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
  serialized_start=185,
  serialized_end=565,
)

_FORTDETAILSRESPONSE.fields_by_name['team_color'].enum_type = Enums_dot_TeamColor__pb2._TEAMCOLOR
_FORTDETAILSRESPONSE.fields_by_name['pokemon_data'].message_type = Data_dot_PokemonData__pb2._POKEMONDATA
_FORTDETAILSRESPONSE.fields_by_name['type'].enum_type = Map_dot_Fort_dot_FortType__pb2._FORTTYPE
_FORTDETAILSRESPONSE.fields_by_name['modifiers'].message_type = Map_dot_Fort_dot_FortModifier__pb2._FORTMODIFIER
DESCRIPTOR.message_types_by_name['FortDetailsResponse'] = _FORTDETAILSRESPONSE

FortDetailsResponse = _reflection.GeneratedProtocolMessageType('FortDetailsResponse', (_message.Message,), dict(
  DESCRIPTOR = _FORTDETAILSRESPONSE,
  __module__ = 'Networking.Responses.FortDetailsResponse_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Responses.FortDetailsResponse)
  ))
_sym_db.RegisterMessage(FortDetailsResponse)


# @@protoc_insertion_point(module_scope)
