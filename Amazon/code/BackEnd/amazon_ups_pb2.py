# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: amazon_ups.proto

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
  name='amazon_ups.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x10\x61mazon_ups.proto\"/\n\x0cUAWorldBuilt\x12\x0f\n\x07worldid\x18\x01 \x02(\x05\x12\x0e\n\x06seqnum\x18\x02 \x02(\x03\"V\n\x07\x41UOrder\x12\x13\n\x0b\x64\x65scription\x18\x01 \x02(\t\x12\x11\n\tlocationx\x18\x02 \x02(\x05\x12\x11\n\tlocationy\x18\x03 \x02(\x05\x12\x10\n\x08username\x18\x04 \x02(\t\"[\n\nAUReqTruck\x12\x13\n\x0bwarehouseid\x18\x01 \x02(\x05\x12\x0e\n\x06shipid\x18\x02 \x02(\x05\x12\x18\n\x06orders\x18\x03 \x02(\x0b\x32\x08.AUOrder\x12\x0e\n\x06seqnum\x18\x04 \x02(\x03\"A\n\x0eUATruckArrived\x12\x0f\n\x07truckid\x18\x01 \x02(\x05\x12\x0e\n\x06shipid\x18\x02 \x02(\x05\x12\x0e\n\x06seqnum\x18\x03 \x02(\x03\"@\n\rAUTruckLoaded\x12\x0f\n\x07truckid\x18\x01 \x02(\x05\x12\x0e\n\x06shipid\x18\x02 \x02(\x05\x12\x0e\n\x06seqnum\x18\x03 \x02(\x03\"2\n\x10UAPackageArrived\x12\x0e\n\x06shipid\x18\x01 \x02(\x03\x12\x0e\n\x06seqnum\x18\x02 \x02(\x03\":\n\x05UAErr\x12\x0b\n\x03\x65rr\x18\x01 \x02(\t\x12\x14\n\x0coriginseqnum\x18\x02 \x02(\x03\x12\x0e\n\x06seqnum\x18\x03 \x02(\x03\"w\n\nAUCommands\x12\x1d\n\x08requests\x18\x01 \x03(\x0b\x32\x0b.AUReqTruck\x12#\n\x0btruckloaded\x18\x02 \x03(\x0b\x32\x0e.AUTruckLoaded\x12\x17\n\x07uaerror\x18\x03 \x03(\x0b\x32\x06.UAErr\x12\x0c\n\x04\x61\x63ks\x18\x04 \x03(\x03\"\x85\x01\n\nUACommands\x12%\n\x0ctruckarrived\x18\x01 \x03(\x0b\x32\x0f.UATruckArrived\x12)\n\x0epackagearrived\x18\x02 \x03(\x0b\x32\x11.UAPackageArrived\x12\x17\n\x07uaerror\x18\x03 \x03(\x0b\x32\x06.UAErr\x12\x0c\n\x04\x61\x63ks\x18\x04 \x03(\x03')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_UAWORLDBUILT = _descriptor.Descriptor(
  name='UAWorldBuilt',
  full_name='UAWorldBuilt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='worldid', full_name='UAWorldBuilt.worldid', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seqnum', full_name='UAWorldBuilt.seqnum', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=67,
)


_AUORDER = _descriptor.Descriptor(
  name='AUOrder',
  full_name='AUOrder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='description', full_name='AUOrder.description', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='locationx', full_name='AUOrder.locationx', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='locationy', full_name='AUOrder.locationy', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='username', full_name='AUOrder.username', index=3,
      number=4, type=9, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=155,
)


_AUREQTRUCK = _descriptor.Descriptor(
  name='AUReqTruck',
  full_name='AUReqTruck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='warehouseid', full_name='AUReqTruck.warehouseid', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shipid', full_name='AUReqTruck.shipid', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orders', full_name='AUReqTruck.orders', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seqnum', full_name='AUReqTruck.seqnum', index=3,
      number=4, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=157,
  serialized_end=248,
)


_UATRUCKARRIVED = _descriptor.Descriptor(
  name='UATruckArrived',
  full_name='UATruckArrived',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='truckid', full_name='UATruckArrived.truckid', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shipid', full_name='UATruckArrived.shipid', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seqnum', full_name='UATruckArrived.seqnum', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=250,
  serialized_end=315,
)


_AUTRUCKLOADED = _descriptor.Descriptor(
  name='AUTruckLoaded',
  full_name='AUTruckLoaded',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='truckid', full_name='AUTruckLoaded.truckid', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shipid', full_name='AUTruckLoaded.shipid', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seqnum', full_name='AUTruckLoaded.seqnum', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=317,
  serialized_end=381,
)


_UAPACKAGEARRIVED = _descriptor.Descriptor(
  name='UAPackageArrived',
  full_name='UAPackageArrived',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shipid', full_name='UAPackageArrived.shipid', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seqnum', full_name='UAPackageArrived.seqnum', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=383,
  serialized_end=433,
)


_UAERR = _descriptor.Descriptor(
  name='UAErr',
  full_name='UAErr',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err', full_name='UAErr.err', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='originseqnum', full_name='UAErr.originseqnum', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seqnum', full_name='UAErr.seqnum', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=435,
  serialized_end=493,
)


_AUCOMMANDS = _descriptor.Descriptor(
  name='AUCommands',
  full_name='AUCommands',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='requests', full_name='AUCommands.requests', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='truckloaded', full_name='AUCommands.truckloaded', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uaerror', full_name='AUCommands.uaerror', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='acks', full_name='AUCommands.acks', index=3,
      number=4, type=3, cpp_type=2, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=495,
  serialized_end=614,
)


_UACOMMANDS = _descriptor.Descriptor(
  name='UACommands',
  full_name='UACommands',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='truckarrived', full_name='UACommands.truckarrived', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='packagearrived', full_name='UACommands.packagearrived', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uaerror', full_name='UACommands.uaerror', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='acks', full_name='UACommands.acks', index=3,
      number=4, type=3, cpp_type=2, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=617,
  serialized_end=750,
)

_AUREQTRUCK.fields_by_name['orders'].message_type = _AUORDER
_AUCOMMANDS.fields_by_name['requests'].message_type = _AUREQTRUCK
_AUCOMMANDS.fields_by_name['truckloaded'].message_type = _AUTRUCKLOADED
_AUCOMMANDS.fields_by_name['uaerror'].message_type = _UAERR
_UACOMMANDS.fields_by_name['truckarrived'].message_type = _UATRUCKARRIVED
_UACOMMANDS.fields_by_name['packagearrived'].message_type = _UAPACKAGEARRIVED
_UACOMMANDS.fields_by_name['uaerror'].message_type = _UAERR
DESCRIPTOR.message_types_by_name['UAWorldBuilt'] = _UAWORLDBUILT
DESCRIPTOR.message_types_by_name['AUOrder'] = _AUORDER
DESCRIPTOR.message_types_by_name['AUReqTruck'] = _AUREQTRUCK
DESCRIPTOR.message_types_by_name['UATruckArrived'] = _UATRUCKARRIVED
DESCRIPTOR.message_types_by_name['AUTruckLoaded'] = _AUTRUCKLOADED
DESCRIPTOR.message_types_by_name['UAPackageArrived'] = _UAPACKAGEARRIVED
DESCRIPTOR.message_types_by_name['UAErr'] = _UAERR
DESCRIPTOR.message_types_by_name['AUCommands'] = _AUCOMMANDS
DESCRIPTOR.message_types_by_name['UACommands'] = _UACOMMANDS

UAWorldBuilt = _reflection.GeneratedProtocolMessageType('UAWorldBuilt', (_message.Message,), dict(
  DESCRIPTOR = _UAWORLDBUILT,
  __module__ = 'amazon_ups_pb2'
  # @@protoc_insertion_point(class_scope:UAWorldBuilt)
  ))
_sym_db.RegisterMessage(UAWorldBuilt)

AUOrder = _reflection.GeneratedProtocolMessageType('AUOrder', (_message.Message,), dict(
  DESCRIPTOR = _AUORDER,
  __module__ = 'amazon_ups_pb2'
  # @@protoc_insertion_point(class_scope:AUOrder)
  ))
_sym_db.RegisterMessage(AUOrder)

AUReqTruck = _reflection.GeneratedProtocolMessageType('AUReqTruck', (_message.Message,), dict(
  DESCRIPTOR = _AUREQTRUCK,
  __module__ = 'amazon_ups_pb2'
  # @@protoc_insertion_point(class_scope:AUReqTruck)
  ))
_sym_db.RegisterMessage(AUReqTruck)

UATruckArrived = _reflection.GeneratedProtocolMessageType('UATruckArrived', (_message.Message,), dict(
  DESCRIPTOR = _UATRUCKARRIVED,
  __module__ = 'amazon_ups_pb2'
  # @@protoc_insertion_point(class_scope:UATruckArrived)
  ))
_sym_db.RegisterMessage(UATruckArrived)

AUTruckLoaded = _reflection.GeneratedProtocolMessageType('AUTruckLoaded', (_message.Message,), dict(
  DESCRIPTOR = _AUTRUCKLOADED,
  __module__ = 'amazon_ups_pb2'
  # @@protoc_insertion_point(class_scope:AUTruckLoaded)
  ))
_sym_db.RegisterMessage(AUTruckLoaded)

UAPackageArrived = _reflection.GeneratedProtocolMessageType('UAPackageArrived', (_message.Message,), dict(
  DESCRIPTOR = _UAPACKAGEARRIVED,
  __module__ = 'amazon_ups_pb2'
  # @@protoc_insertion_point(class_scope:UAPackageArrived)
  ))
_sym_db.RegisterMessage(UAPackageArrived)

UAErr = _reflection.GeneratedProtocolMessageType('UAErr', (_message.Message,), dict(
  DESCRIPTOR = _UAERR,
  __module__ = 'amazon_ups_pb2'
  # @@protoc_insertion_point(class_scope:UAErr)
  ))
_sym_db.RegisterMessage(UAErr)

AUCommands = _reflection.GeneratedProtocolMessageType('AUCommands', (_message.Message,), dict(
  DESCRIPTOR = _AUCOMMANDS,
  __module__ = 'amazon_ups_pb2'
  # @@protoc_insertion_point(class_scope:AUCommands)
  ))
_sym_db.RegisterMessage(AUCommands)

UACommands = _reflection.GeneratedProtocolMessageType('UACommands', (_message.Message,), dict(
  DESCRIPTOR = _UACOMMANDS,
  __module__ = 'amazon_ups_pb2'
  # @@protoc_insertion_point(class_scope:UACommands)
  ))
_sym_db.RegisterMessage(UACommands)


# @@protoc_insertion_point(module_scope)
