# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: module.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import mygrpc.shared_pb2 as shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cmodule.proto\x12\x12xtc.fmp.repository\x1a\x0cshared.proto\"A\n\x13ModuleCreateRequest\x12\x0b\n\x03org\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\"0\n\x13ModuleUpdateRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0b\n\x03\x63li\x18\x02 \x01(\t\"v\n\x16ModuleRetrieveResponse\x12*\n\x06status\x18\x01 \x01(\x0b\x32\x1a.xtc.fmp.repository.Status\x12\x30\n\x06module\x18\x02 \x01(\x0b\x32 .xtc.fmp.repository.ModuleEntity\"2\n\x11ModuleListRequest\x12\x0e\n\x06offset\x18\x01 \x01(\x03\x12\r\n\x05\x63ount\x18\x02 \x01(\x03\"\x82\x01\n\x12ModuleListResponse\x12*\n\x06status\x18\x01 \x01(\x0b\x32\x1a.xtc.fmp.repository.Status\x12\r\n\x05total\x18\x02 \x01(\x03\x12\x31\n\x07modules\x18\x03 \x03(\x0b\x32 .xtc.fmp.repository.ModuleEntity\"O\n\x13ModuleSearchRequest\x12\x0e\n\x06offset\x18\x01 \x01(\x03\x12\r\n\x05\x63ount\x18\x02 \x01(\x03\x12\x0b\n\x03org\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t2\x97\x07\n\x06Module\x12U\n\x06\x43reate\x12\'.xtc.fmp.repository.ModuleCreateRequest\x1a .xtc.fmp.repository.UuidResponse\"\x00\x12U\n\x06Update\x12\'.xtc.fmp.repository.ModuleUpdateRequest\x1a .xtc.fmp.repository.UuidResponse\"\x00\x12Y\n\x08Retrieve\x12\x1f.xtc.fmp.repository.UuidRequest\x1a*.xtc.fmp.repository.ModuleRetrieveResponse\"\x00\x12M\n\x06\x44\x65lete\x12\x1f.xtc.fmp.repository.UuidRequest\x1a .xtc.fmp.repository.UuidResponse\"\x00\x12W\n\x04List\x12%.xtc.fmp.repository.ModuleListRequest\x1a&.xtc.fmp.repository.ModuleListResponse\"\x00\x12[\n\x06Search\x12\'.xtc.fmp.repository.ModuleSearchRequest\x1a&.xtc.fmp.repository.ModuleListResponse\"\x00\x12]\n\rPrepareUpload\x12\x1f.xtc.fmp.repository.UuidRequest\x1a).xtc.fmp.repository.PrepareUploadResponse\"\x00\x12Y\n\x0b\x46lushUpload\x12\x1f.xtc.fmp.repository.UuidRequest\x1a\'.xtc.fmp.repository.FlushUploadResponse\"\x00\x12`\n\x07\x41\x64\x64\x46lag\x12(.xtc.fmp.repository.FlagOperationRequest\x1a).xtc.fmp.repository.FlagOperationResponse\"\x00\x12\x63\n\nRemoveFlag\x12(.xtc.fmp.repository.FlagOperationRequest\x1a).xtc.fmp.repository.FlagOperationResponse\"\x00\x42#\xaa\x02 XTC.FMP.MOD.Repository.LIB.Protob\x06proto3')



_MODULECREATEREQUEST = DESCRIPTOR.message_types_by_name['ModuleCreateRequest']
_MODULEUPDATEREQUEST = DESCRIPTOR.message_types_by_name['ModuleUpdateRequest']
_MODULERETRIEVERESPONSE = DESCRIPTOR.message_types_by_name['ModuleRetrieveResponse']
_MODULELISTREQUEST = DESCRIPTOR.message_types_by_name['ModuleListRequest']
_MODULELISTRESPONSE = DESCRIPTOR.message_types_by_name['ModuleListResponse']
_MODULESEARCHREQUEST = DESCRIPTOR.message_types_by_name['ModuleSearchRequest']
ModuleCreateRequest = _reflection.GeneratedProtocolMessageType('ModuleCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _MODULECREATEREQUEST,
  '__module__' : 'module_pb2'
  # @@protoc_insertion_point(class_scope:xtc.fmp.repository.ModuleCreateRequest)
  })
_sym_db.RegisterMessage(ModuleCreateRequest)

ModuleUpdateRequest = _reflection.GeneratedProtocolMessageType('ModuleUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _MODULEUPDATEREQUEST,
  '__module__' : 'module_pb2'
  # @@protoc_insertion_point(class_scope:xtc.fmp.repository.ModuleUpdateRequest)
  })
_sym_db.RegisterMessage(ModuleUpdateRequest)

ModuleRetrieveResponse = _reflection.GeneratedProtocolMessageType('ModuleRetrieveResponse', (_message.Message,), {
  'DESCRIPTOR' : _MODULERETRIEVERESPONSE,
  '__module__' : 'module_pb2'
  # @@protoc_insertion_point(class_scope:xtc.fmp.repository.ModuleRetrieveResponse)
  })
_sym_db.RegisterMessage(ModuleRetrieveResponse)

ModuleListRequest = _reflection.GeneratedProtocolMessageType('ModuleListRequest', (_message.Message,), {
  'DESCRIPTOR' : _MODULELISTREQUEST,
  '__module__' : 'module_pb2'
  # @@protoc_insertion_point(class_scope:xtc.fmp.repository.ModuleListRequest)
  })
_sym_db.RegisterMessage(ModuleListRequest)

ModuleListResponse = _reflection.GeneratedProtocolMessageType('ModuleListResponse', (_message.Message,), {
  'DESCRIPTOR' : _MODULELISTRESPONSE,
  '__module__' : 'module_pb2'
  # @@protoc_insertion_point(class_scope:xtc.fmp.repository.ModuleListResponse)
  })
_sym_db.RegisterMessage(ModuleListResponse)

ModuleSearchRequest = _reflection.GeneratedProtocolMessageType('ModuleSearchRequest', (_message.Message,), {
  'DESCRIPTOR' : _MODULESEARCHREQUEST,
  '__module__' : 'module_pb2'
  # @@protoc_insertion_point(class_scope:xtc.fmp.repository.ModuleSearchRequest)
  })
_sym_db.RegisterMessage(ModuleSearchRequest)

_MODULE = DESCRIPTOR.services_by_name['Module']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002 XTC.FMP.MOD.Repository.LIB.Proto'
  _MODULECREATEREQUEST._serialized_start=50
  _MODULECREATEREQUEST._serialized_end=115
  _MODULEUPDATEREQUEST._serialized_start=117
  _MODULEUPDATEREQUEST._serialized_end=165
  _MODULERETRIEVERESPONSE._serialized_start=167
  _MODULERETRIEVERESPONSE._serialized_end=285
  _MODULELISTREQUEST._serialized_start=287
  _MODULELISTREQUEST._serialized_end=337
  _MODULELISTRESPONSE._serialized_start=340
  _MODULELISTRESPONSE._serialized_end=470
  _MODULESEARCHREQUEST._serialized_start=472
  _MODULESEARCHREQUEST._serialized_end=551
  _MODULE._serialized_start=554
  _MODULE._serialized_end=1473
# @@protoc_insertion_point(module_scope)
