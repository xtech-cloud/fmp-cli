# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: agent.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import mygrpc.shared_pb2 as shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x61gent.proto\x12\x12xtc.fmp.repository\x1a\x0cshared.proto\"@\n\x12\x41gentCreateRequest\x12\x0b\n\x03org\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\"?\n\x12\x41gentUpdateRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\r\x12\r\n\x05pages\x18\x03 \x03(\t\"s\n\x15\x41gentRetrieveResponse\x12*\n\x06status\x18\x01 \x01(\x0b\x32\x1a.xtc.fmp.repository.Status\x12.\n\x05\x61gent\x18\x02 \x01(\x0b\x32\x1f.xtc.fmp.repository.AgentEntity\"1\n\x10\x41gentListRequest\x12\x0e\n\x06offset\x18\x01 \x01(\x03\x12\r\n\x05\x63ount\x18\x02 \x01(\x03\"\x7f\n\x11\x41gentListResponse\x12*\n\x06status\x18\x01 \x01(\x0b\x32\x1a.xtc.fmp.repository.Status\x12\r\n\x05total\x18\x02 \x01(\x03\x12/\n\x06\x61gents\x18\x03 \x03(\x0b\x32\x1f.xtc.fmp.repository.AgentEntity\"N\n\x12\x41gentSearchRequest\x12\x0e\n\x06offset\x18\x01 \x01(\x03\x12\r\n\x05\x63ount\x18\x02 \x01(\x03\x12\x0b\n\x03org\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t2\x8f\x07\n\x05\x41gent\x12T\n\x06\x43reate\x12&.xtc.fmp.repository.AgentCreateRequest\x1a .xtc.fmp.repository.UuidResponse\"\x00\x12T\n\x06Update\x12&.xtc.fmp.repository.AgentUpdateRequest\x1a .xtc.fmp.repository.UuidResponse\"\x00\x12X\n\x08Retrieve\x12\x1f.xtc.fmp.repository.UuidRequest\x1a).xtc.fmp.repository.AgentRetrieveResponse\"\x00\x12M\n\x06\x44\x65lete\x12\x1f.xtc.fmp.repository.UuidRequest\x1a .xtc.fmp.repository.UuidResponse\"\x00\x12U\n\x04List\x12$.xtc.fmp.repository.AgentListRequest\x1a%.xtc.fmp.repository.AgentListResponse\"\x00\x12Y\n\x06Search\x12&.xtc.fmp.repository.AgentSearchRequest\x1a%.xtc.fmp.repository.AgentListResponse\"\x00\x12]\n\rPrepareUpload\x12\x1f.xtc.fmp.repository.UuidRequest\x1a).xtc.fmp.repository.PrepareUploadResponse\"\x00\x12Y\n\x0b\x46lushUpload\x12\x1f.xtc.fmp.repository.UuidRequest\x1a\'.xtc.fmp.repository.FlushUploadResponse\"\x00\x12`\n\x07\x41\x64\x64\x46lag\x12(.xtc.fmp.repository.FlagOperationRequest\x1a).xtc.fmp.repository.FlagOperationResponse\"\x00\x12\x63\n\nRemoveFlag\x12(.xtc.fmp.repository.FlagOperationRequest\x1a).xtc.fmp.repository.FlagOperationResponse\"\x00\x42#\xaa\x02 XTC.FMP.MOD.Repository.LIB.Protob\x06proto3')



_AGENTCREATEREQUEST = DESCRIPTOR.message_types_by_name['AgentCreateRequest']
_AGENTUPDATEREQUEST = DESCRIPTOR.message_types_by_name['AgentUpdateRequest']
_AGENTRETRIEVERESPONSE = DESCRIPTOR.message_types_by_name['AgentRetrieveResponse']
_AGENTLISTREQUEST = DESCRIPTOR.message_types_by_name['AgentListRequest']
_AGENTLISTRESPONSE = DESCRIPTOR.message_types_by_name['AgentListResponse']
_AGENTSEARCHREQUEST = DESCRIPTOR.message_types_by_name['AgentSearchRequest']
AgentCreateRequest = _reflection.GeneratedProtocolMessageType('AgentCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _AGENTCREATEREQUEST,
  '__module__' : 'agent_pb2'
  # @@protoc_insertion_point(class_scope:xtc.fmp.repository.AgentCreateRequest)
  })
_sym_db.RegisterMessage(AgentCreateRequest)

AgentUpdateRequest = _reflection.GeneratedProtocolMessageType('AgentUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _AGENTUPDATEREQUEST,
  '__module__' : 'agent_pb2'
  # @@protoc_insertion_point(class_scope:xtc.fmp.repository.AgentUpdateRequest)
  })
_sym_db.RegisterMessage(AgentUpdateRequest)

AgentRetrieveResponse = _reflection.GeneratedProtocolMessageType('AgentRetrieveResponse', (_message.Message,), {
  'DESCRIPTOR' : _AGENTRETRIEVERESPONSE,
  '__module__' : 'agent_pb2'
  # @@protoc_insertion_point(class_scope:xtc.fmp.repository.AgentRetrieveResponse)
  })
_sym_db.RegisterMessage(AgentRetrieveResponse)

AgentListRequest = _reflection.GeneratedProtocolMessageType('AgentListRequest', (_message.Message,), {
  'DESCRIPTOR' : _AGENTLISTREQUEST,
  '__module__' : 'agent_pb2'
  # @@protoc_insertion_point(class_scope:xtc.fmp.repository.AgentListRequest)
  })
_sym_db.RegisterMessage(AgentListRequest)

AgentListResponse = _reflection.GeneratedProtocolMessageType('AgentListResponse', (_message.Message,), {
  'DESCRIPTOR' : _AGENTLISTRESPONSE,
  '__module__' : 'agent_pb2'
  # @@protoc_insertion_point(class_scope:xtc.fmp.repository.AgentListResponse)
  })
_sym_db.RegisterMessage(AgentListResponse)

AgentSearchRequest = _reflection.GeneratedProtocolMessageType('AgentSearchRequest', (_message.Message,), {
  'DESCRIPTOR' : _AGENTSEARCHREQUEST,
  '__module__' : 'agent_pb2'
  # @@protoc_insertion_point(class_scope:xtc.fmp.repository.AgentSearchRequest)
  })
_sym_db.RegisterMessage(AgentSearchRequest)

_AGENT = DESCRIPTOR.services_by_name['Agent']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002 XTC.FMP.MOD.Repository.LIB.Proto'
  _AGENTCREATEREQUEST._serialized_start=49
  _AGENTCREATEREQUEST._serialized_end=113
  _AGENTUPDATEREQUEST._serialized_start=115
  _AGENTUPDATEREQUEST._serialized_end=178
  _AGENTRETRIEVERESPONSE._serialized_start=180
  _AGENTRETRIEVERESPONSE._serialized_end=295
  _AGENTLISTREQUEST._serialized_start=297
  _AGENTLISTREQUEST._serialized_end=346
  _AGENTLISTRESPONSE._serialized_start=348
  _AGENTLISTRESPONSE._serialized_end=475
  _AGENTSEARCHREQUEST._serialized_start=477
  _AGENTSEARCHREQUEST._serialized_end=555
  _AGENT._serialized_start=558
  _AGENT._serialized_end=1469
# @@protoc_insertion_point(module_scope)
