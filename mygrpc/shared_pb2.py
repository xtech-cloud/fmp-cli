# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: shared.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cshared.proto\x12\x12xtc.fmp.repository\"\'\n\x06Status\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x0e\n\x0c\x42lankRequest\";\n\rBlankResponse\x12*\n\x06status\x18\x01 \x01(\x0b\x32\x1a.xtc.fmp.repository.Status\"\x1d\n\x0cScopeRequest\x12\r\n\x05scope\x18\x01 \x01(\t\"J\n\rScopeResponse\x12*\n\x06status\x18\x01 \x01(\x0b\x32\x1a.xtc.fmp.repository.Status\x12\r\n\x05scope\x18\x02 \x01(\t\"\x1b\n\x0bUuidRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t\"H\n\x0cUuidResponse\x12*\n\x06status\x18\x01 \x01(\x0b\x32\x1a.xtc.fmp.repository.Status\x12\x0c\n\x04uuid\x18\x02 \x01(\t\"\xc1\x01\n\x15PrepareUploadResponse\x12*\n\x06status\x18\x01 \x01(\x0b\x32\x1a.xtc.fmp.repository.Status\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\x41\n\x04urls\x18\x03 \x03(\x0b\x32\x33.xtc.fmp.repository.PrepareUploadResponse.UrlsEntry\x1a+\n\tUrlsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xc0\x02\n\x13\x46lushUploadResponse\x12*\n\x06status\x18\x01 \x01(\x0b\x32\x1a.xtc.fmp.repository.Status\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\x41\n\x05hashs\x18\x03 \x03(\x0b\x32\x32.xtc.fmp.repository.FlushUploadResponse.HashsEntry\x12\x41\n\x05sizes\x18\x04 \x03(\x0b\x32\x32.xtc.fmp.repository.FlushUploadResponse.SizesEntry\x12\r\n\x05\x66lags\x18\x05 \x01(\x04\x1a,\n\nHashsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a,\n\nSizesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x04:\x02\x38\x01\"2\n\x14\x46lagOperationRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0c\n\x04\x66lag\x18\x02 \x01(\x04\"`\n\x15\x46lagOperationResponse\x12*\n\x06status\x18\x01 \x01(\x0b\x32\x1a.xtc.fmp.repository.Status\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\r\n\x05\x66lags\x18\x03 \x01(\x04\"6\n\nFileEntity\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04size\x18\x02 \x01(\x04\x12\x0c\n\x04hash\x18\x03 \x01(\t\"\x8b\x01\n\x0cPluginEntity\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\r\n\x05\x66lags\x18\n \x01(\x04\x12\x11\n\tupdatedAt\x18\x0b \x01(\x03\x12,\n\x04\x66ile\x18\x14 \x01(\x0b\x32\x1e.xtc.fmp.repository.FileEntity\"\xa6\x01\n\x0cModuleEntity\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0b\n\x03org\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\t\x12\x0b\n\x03\x63li\x18\x05 \x01(\t\x12\r\n\x05\x66lags\x18\n \x01(\x04\x12\x11\n\tupdatedAt\x18\x0b \x01(\x03\x12-\n\x05\x66iles\x18\x14 \x03(\x0b\x32\x1e.xtc.fmp.repository.FileEntity\"\xb4\x01\n\x0b\x41gentEntity\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0b\n\x03org\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\t\x12\x0c\n\x04port\x18\x05 \x01(\r\x12\r\n\x05pages\x18\x06 \x03(\t\x12\r\n\x05\x66lags\x18\n \x01(\x04\x12\x11\n\tupdatedAt\x18\x0b \x01(\x03\x12,\n\x04\x66ile\x18\x14 \x01(\x0b\x32\x1e.xtc.fmp.repository.FileEntity\"\xaf\x01\n\x11\x41pplicationEntity\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0b\n\x03org\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\t\x12\x10\n\x08platform\x18\x05 \x01(\t\x12\r\n\x05\x66lags\x18\n \x01(\x04\x12\x11\n\tupdatedAt\x18\x0b \x01(\x03\x12,\n\x04\x66ile\x18\x14 \x01(\x0b\x32\x1e.xtc.fmp.repository.FileEntityB#\xaa\x02 XTC.FMP.MOD.Repository.LIB.Protob\x06proto3')



_STATUS = DESCRIPTOR.message_types_by_name['Status']
_BLANKREQUEST = DESCRIPTOR.message_types_by_name['BlankRequest']
_BLANKRESPONSE = DESCRIPTOR.message_types_by_name['BlankResponse']
_SCOPEREQUEST = DESCRIPTOR.message_types_by_name['ScopeRequest']
_SCOPERESPONSE = DESCRIPTOR.message_types_by_name['ScopeResponse']
_UUIDREQUEST = DESCRIPTOR.message_types_by_name['UuidRequest']
_UUIDRESPONSE = DESCRIPTOR.message_types_by_name['UuidResponse']
_PREPAREUPLOADRESPONSE = DESCRIPTOR.message_types_by_name['PrepareUploadResponse']
_PREPAREUPLOADRESPONSE_URLSENTRY = _PREPAREUPLOADRESPONSE.nested_types_by_name['UrlsEntry']
_FLUSHUPLOADRESPONSE = DESCRIPTOR.message_types_by_name['FlushUploadResponse']
_FLUSHUPLOADRESPONSE_HASHSENTRY = _FLUSHUPLOADRESPONSE.nested_types_by_name['HashsEntry']
_FLUSHUPLOADRESPONSE_SIZESENTRY = _FLUSHUPLOADRESPONSE.nested_types_by_name['SizesEntry']
_FLAGOPERATIONREQUEST = DESCRIPTOR.message_types_by_name['FlagOperationRequest']
_FLAGOPERATIONRESPONSE = DESCRIPTOR.message_types_by_name['FlagOperationResponse']
_FILEENTITY = DESCRIPTOR.message_types_by_name['FileEntity']
_PLUGINENTITY = DESCRIPTOR.message_types_by_name['PluginEntity']
_MODULEENTITY = DESCRIPTOR.message_types_by_name['ModuleEntity']
_AGENTENTITY = DESCRIPTOR.message_types_by_name['AgentEntity']
_APPLICATIONENTITY = DESCRIPTOR.message_types_by_name['ApplicationEntity']
Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'shared_pb2'
  # @@protoc_insertion_point(class_scope:xtc.fmp.repository.Status)
  })
_sym_db.RegisterMessage(Status)

BlankRequest = _reflection.GeneratedProtocolMessageType('BlankRequest', (_message.Message,), {
  'DESCRIPTOR' : _BLANKREQUEST,
  '__module__' : 'shared_pb2'
  # @@protoc_insertion_point(class_scope:xtc.fmp.repository.BlankRequest)
  })
_sym_db.RegisterMessage(BlankRequest)

BlankResponse = _reflection.GeneratedProtocolMessageType('BlankResponse', (_message.Message,), {
  'DESCRIPTOR' : _BLANKRESPONSE,
  '__module__' : 'shared_pb2'
  # @@protoc_insertion_point(class_scope:xtc.fmp.repository.BlankResponse)
  })
_sym_db.RegisterMessage(BlankResponse)

ScopeRequest = _reflection.GeneratedProtocolMessageType('ScopeRequest', (_message.Message,), {
  'DESCRIPTOR' : _SCOPEREQUEST,
  '__module__' : 'shared_pb2'
  # @@protoc_insertion_point(class_scope:xtc.fmp.repository.ScopeRequest)
  })
_sym_db.RegisterMessage(ScopeRequest)

ScopeResponse = _reflection.GeneratedProtocolMessageType('ScopeResponse', (_message.Message,), {
  'DESCRIPTOR' : _SCOPERESPONSE,
  '__module__' : 'shared_pb2'
  # @@protoc_insertion_point(class_scope:xtc.fmp.repository.ScopeResponse)
  })
_sym_db.RegisterMessage(ScopeResponse)

UuidRequest = _reflection.GeneratedProtocolMessageType('UuidRequest', (_message.Message,), {
  'DESCRIPTOR' : _UUIDREQUEST,
  '__module__' : 'shared_pb2'
  # @@protoc_insertion_point(class_scope:xtc.fmp.repository.UuidRequest)
  })
_sym_db.RegisterMessage(UuidRequest)

UuidResponse = _reflection.GeneratedProtocolMessageType('UuidResponse', (_message.Message,), {
  'DESCRIPTOR' : _UUIDRESPONSE,
  '__module__' : 'shared_pb2'
  # @@protoc_insertion_point(class_scope:xtc.fmp.repository.UuidResponse)
  })
_sym_db.RegisterMessage(UuidResponse)

PrepareUploadResponse = _reflection.GeneratedProtocolMessageType('PrepareUploadResponse', (_message.Message,), {

  'UrlsEntry' : _reflection.GeneratedProtocolMessageType('UrlsEntry', (_message.Message,), {
    'DESCRIPTOR' : _PREPAREUPLOADRESPONSE_URLSENTRY,
    '__module__' : 'shared_pb2'
    # @@protoc_insertion_point(class_scope:xtc.fmp.repository.PrepareUploadResponse.UrlsEntry)
    })
  ,
  'DESCRIPTOR' : _PREPAREUPLOADRESPONSE,
  '__module__' : 'shared_pb2'
  # @@protoc_insertion_point(class_scope:xtc.fmp.repository.PrepareUploadResponse)
  })
_sym_db.RegisterMessage(PrepareUploadResponse)
_sym_db.RegisterMessage(PrepareUploadResponse.UrlsEntry)

FlushUploadResponse = _reflection.GeneratedProtocolMessageType('FlushUploadResponse', (_message.Message,), {

  'HashsEntry' : _reflection.GeneratedProtocolMessageType('HashsEntry', (_message.Message,), {
    'DESCRIPTOR' : _FLUSHUPLOADRESPONSE_HASHSENTRY,
    '__module__' : 'shared_pb2'
    # @@protoc_insertion_point(class_scope:xtc.fmp.repository.FlushUploadResponse.HashsEntry)
    })
  ,

  'SizesEntry' : _reflection.GeneratedProtocolMessageType('SizesEntry', (_message.Message,), {
    'DESCRIPTOR' : _FLUSHUPLOADRESPONSE_SIZESENTRY,
    '__module__' : 'shared_pb2'
    # @@protoc_insertion_point(class_scope:xtc.fmp.repository.FlushUploadResponse.SizesEntry)
    })
  ,
  'DESCRIPTOR' : _FLUSHUPLOADRESPONSE,
  '__module__' : 'shared_pb2'
  # @@protoc_insertion_point(class_scope:xtc.fmp.repository.FlushUploadResponse)
  })
_sym_db.RegisterMessage(FlushUploadResponse)
_sym_db.RegisterMessage(FlushUploadResponse.HashsEntry)
_sym_db.RegisterMessage(FlushUploadResponse.SizesEntry)

FlagOperationRequest = _reflection.GeneratedProtocolMessageType('FlagOperationRequest', (_message.Message,), {
  'DESCRIPTOR' : _FLAGOPERATIONREQUEST,
  '__module__' : 'shared_pb2'
  # @@protoc_insertion_point(class_scope:xtc.fmp.repository.FlagOperationRequest)
  })
_sym_db.RegisterMessage(FlagOperationRequest)

FlagOperationResponse = _reflection.GeneratedProtocolMessageType('FlagOperationResponse', (_message.Message,), {
  'DESCRIPTOR' : _FLAGOPERATIONRESPONSE,
  '__module__' : 'shared_pb2'
  # @@protoc_insertion_point(class_scope:xtc.fmp.repository.FlagOperationResponse)
  })
_sym_db.RegisterMessage(FlagOperationResponse)

FileEntity = _reflection.GeneratedProtocolMessageType('FileEntity', (_message.Message,), {
  'DESCRIPTOR' : _FILEENTITY,
  '__module__' : 'shared_pb2'
  # @@protoc_insertion_point(class_scope:xtc.fmp.repository.FileEntity)
  })
_sym_db.RegisterMessage(FileEntity)

PluginEntity = _reflection.GeneratedProtocolMessageType('PluginEntity', (_message.Message,), {
  'DESCRIPTOR' : _PLUGINENTITY,
  '__module__' : 'shared_pb2'
  # @@protoc_insertion_point(class_scope:xtc.fmp.repository.PluginEntity)
  })
_sym_db.RegisterMessage(PluginEntity)

ModuleEntity = _reflection.GeneratedProtocolMessageType('ModuleEntity', (_message.Message,), {
  'DESCRIPTOR' : _MODULEENTITY,
  '__module__' : 'shared_pb2'
  # @@protoc_insertion_point(class_scope:xtc.fmp.repository.ModuleEntity)
  })
_sym_db.RegisterMessage(ModuleEntity)

AgentEntity = _reflection.GeneratedProtocolMessageType('AgentEntity', (_message.Message,), {
  'DESCRIPTOR' : _AGENTENTITY,
  '__module__' : 'shared_pb2'
  # @@protoc_insertion_point(class_scope:xtc.fmp.repository.AgentEntity)
  })
_sym_db.RegisterMessage(AgentEntity)

ApplicationEntity = _reflection.GeneratedProtocolMessageType('ApplicationEntity', (_message.Message,), {
  'DESCRIPTOR' : _APPLICATIONENTITY,
  '__module__' : 'shared_pb2'
  # @@protoc_insertion_point(class_scope:xtc.fmp.repository.ApplicationEntity)
  })
_sym_db.RegisterMessage(ApplicationEntity)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002 XTC.FMP.MOD.Repository.LIB.Proto'
  _PREPAREUPLOADRESPONSE_URLSENTRY._options = None
  _PREPAREUPLOADRESPONSE_URLSENTRY._serialized_options = b'8\001'
  _FLUSHUPLOADRESPONSE_HASHSENTRY._options = None
  _FLUSHUPLOADRESPONSE_HASHSENTRY._serialized_options = b'8\001'
  _FLUSHUPLOADRESPONSE_SIZESENTRY._options = None
  _FLUSHUPLOADRESPONSE_SIZESENTRY._serialized_options = b'8\001'
  _STATUS._serialized_start=36
  _STATUS._serialized_end=75
  _BLANKREQUEST._serialized_start=77
  _BLANKREQUEST._serialized_end=91
  _BLANKRESPONSE._serialized_start=93
  _BLANKRESPONSE._serialized_end=152
  _SCOPEREQUEST._serialized_start=154
  _SCOPEREQUEST._serialized_end=183
  _SCOPERESPONSE._serialized_start=185
  _SCOPERESPONSE._serialized_end=259
  _UUIDREQUEST._serialized_start=261
  _UUIDREQUEST._serialized_end=288
  _UUIDRESPONSE._serialized_start=290
  _UUIDRESPONSE._serialized_end=362
  _PREPAREUPLOADRESPONSE._serialized_start=365
  _PREPAREUPLOADRESPONSE._serialized_end=558
  _PREPAREUPLOADRESPONSE_URLSENTRY._serialized_start=515
  _PREPAREUPLOADRESPONSE_URLSENTRY._serialized_end=558
  _FLUSHUPLOADRESPONSE._serialized_start=561
  _FLUSHUPLOADRESPONSE._serialized_end=881
  _FLUSHUPLOADRESPONSE_HASHSENTRY._serialized_start=791
  _FLUSHUPLOADRESPONSE_HASHSENTRY._serialized_end=835
  _FLUSHUPLOADRESPONSE_SIZESENTRY._serialized_start=837
  _FLUSHUPLOADRESPONSE_SIZESENTRY._serialized_end=881
  _FLAGOPERATIONREQUEST._serialized_start=883
  _FLAGOPERATIONREQUEST._serialized_end=933
  _FLAGOPERATIONRESPONSE._serialized_start=935
  _FLAGOPERATIONRESPONSE._serialized_end=1031
  _FILEENTITY._serialized_start=1033
  _FILEENTITY._serialized_end=1087
  _PLUGINENTITY._serialized_start=1090
  _PLUGINENTITY._serialized_end=1229
  _MODULEENTITY._serialized_start=1232
  _MODULEENTITY._serialized_end=1398
  _AGENTENTITY._serialized_start=1401
  _AGENTENTITY._serialized_end=1581
  _APPLICATIONENTITY._serialized_start=1584
  _APPLICATIONENTITY._serialized_end=1759
# @@protoc_insertion_point(module_scope)
