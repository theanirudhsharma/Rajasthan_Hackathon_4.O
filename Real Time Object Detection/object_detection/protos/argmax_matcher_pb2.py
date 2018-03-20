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
  name='object_detection/protos/argmax_matcher.proto',
  package='object_detection.protos',
  serialized_pb=_b('\n,object_detection/protos/argmax_matcher.proto\x12\x17object_detection.protos\"\xca\x01\n\rArgMaxMatcher\x12\x1e\n\x11matched_threshold\x18\x01 \x01(\x02:\x03\x30.5\x12 \n\x13unmatched_threshold\x18\x02 \x01(\x02:\x03\x30.5\x12 \n\x11ignore_thresholds\x18\x03 \x01(\x08:\x05\x66\x61lse\x12,\n\x1enegatives_lower_than_unmatched\x18\x04 \x01(\x08:\x04true\x12\'\n\x18\x66orce_match_for_each_row\x18\x05 \x01(\x08:\x05\x66\x61lse')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ARGMAXMATCHER = _descriptor.Descriptor(
  name='ArgMaxMatcher',
  full_name='object_detection.protos.ArgMaxMatcher',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='matched_threshold', full_name='object_detection.protos.ArgMaxMatcher.matched_threshold', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0.5,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unmatched_threshold', full_name='object_detection.protos.ArgMaxMatcher.unmatched_threshold', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0.5,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ignore_thresholds', full_name='object_detection.protos.ArgMaxMatcher.ignore_thresholds', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='negatives_lower_than_unmatched', full_name='object_detection.protos.ArgMaxMatcher.negatives_lower_than_unmatched', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='force_match_for_each_row', full_name='object_detection.protos.ArgMaxMatcher.force_match_for_each_row', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=276,
)

DESCRIPTOR.message_types_by_name['ArgMaxMatcher'] = _ARGMAXMATCHER

ArgMaxMatcher = _reflection.GeneratedProtocolMessageType('ArgMaxMatcher', (_message.Message,), dict(
  DESCRIPTOR = _ARGMAXMATCHER,
  __module__ = 'object_detection.protos.argmax_matcher_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.ArgMaxMatcher)
  ))
_sym_db.RegisterMessage(ArgMaxMatcher)


# @@protoc_insertion_point(module_scope)
