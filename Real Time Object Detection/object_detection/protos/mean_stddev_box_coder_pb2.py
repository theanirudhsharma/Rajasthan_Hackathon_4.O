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
  name='object_detection/protos/mean_stddev_box_coder.proto',
  package='object_detection.protos',
  serialized_pb=_b('\n3object_detection/protos/mean_stddev_box_coder.proto\x12\x17object_detection.protos\"\x14\n\x12MeanStddevBoxCoder')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MEANSTDDEVBOXCODER = _descriptor.Descriptor(
  name='MeanStddevBoxCoder',
  full_name='object_detection.protos.MeanStddevBoxCoder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=100,
)

DESCRIPTOR.message_types_by_name['MeanStddevBoxCoder'] = _MEANSTDDEVBOXCODER

MeanStddevBoxCoder = _reflection.GeneratedProtocolMessageType('MeanStddevBoxCoder', (_message.Message,), dict(
  DESCRIPTOR = _MEANSTDDEVBOXCODER,
  __module__ = 'object_detection.protos.mean_stddev_box_coder_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.MeanStddevBoxCoder)
  ))
_sym_db.RegisterMessage(MeanStddevBoxCoder)


# @@protoc_insertion_point(module_scope)
