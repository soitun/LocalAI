# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: backend.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rbackend.proto\x12\x07\x62\x61\x63kend\"\x0f\n\rHealthMessage\"\xa6\x06\n\x0ePredictOptions\x12\x0e\n\x06Prompt\x18\x01 \x01(\t\x12\x0c\n\x04Seed\x18\x02 \x01(\x05\x12\x0f\n\x07Threads\x18\x03 \x01(\x05\x12\x0e\n\x06Tokens\x18\x04 \x01(\x05\x12\x0c\n\x04TopK\x18\x05 \x01(\x05\x12\x0e\n\x06Repeat\x18\x06 \x01(\x05\x12\r\n\x05\x42\x61tch\x18\x07 \x01(\x05\x12\r\n\x05NKeep\x18\x08 \x01(\x05\x12\x13\n\x0bTemperature\x18\t \x01(\x02\x12\x0f\n\x07Penalty\x18\n \x01(\x02\x12\r\n\x05\x46\x31\x36KV\x18\x0b \x01(\x08\x12\x11\n\tDebugMode\x18\x0c \x01(\x08\x12\x13\n\x0bStopPrompts\x18\r \x03(\t\x12\x11\n\tIgnoreEOS\x18\x0e \x01(\x08\x12\x19\n\x11TailFreeSamplingZ\x18\x0f \x01(\x02\x12\x10\n\x08TypicalP\x18\x10 \x01(\x02\x12\x18\n\x10\x46requencyPenalty\x18\x11 \x01(\x02\x12\x17\n\x0fPresencePenalty\x18\x12 \x01(\x02\x12\x10\n\x08Mirostat\x18\x13 \x01(\x05\x12\x13\n\x0bMirostatETA\x18\x14 \x01(\x02\x12\x13\n\x0bMirostatTAU\x18\x15 \x01(\x02\x12\x12\n\nPenalizeNL\x18\x16 \x01(\x08\x12\x11\n\tLogitBias\x18\x17 \x01(\t\x12\r\n\x05MLock\x18\x19 \x01(\x08\x12\x0c\n\x04MMap\x18\x1a \x01(\x08\x12\x16\n\x0ePromptCacheAll\x18\x1b \x01(\x08\x12\x15\n\rPromptCacheRO\x18\x1c \x01(\x08\x12\x0f\n\x07Grammar\x18\x1d \x01(\t\x12\x0f\n\x07MainGPU\x18\x1e \x01(\t\x12\x13\n\x0bTensorSplit\x18\x1f \x01(\t\x12\x0c\n\x04TopP\x18  \x01(\x02\x12\x17\n\x0fPromptCachePath\x18! \x01(\t\x12\r\n\x05\x44\x65\x62ug\x18\" \x01(\x08\x12\x17\n\x0f\x45mbeddingTokens\x18# \x03(\x05\x12\x12\n\nEmbeddings\x18$ \x01(\t\x12\x14\n\x0cRopeFreqBase\x18% \x01(\x02\x12\x15\n\rRopeFreqScale\x18& \x01(\x02\x12\x1b\n\x13NegativePromptScale\x18\' \x01(\x02\x12\x16\n\x0eNegativePrompt\x18( \x01(\t\x12\x0e\n\x06NDraft\x18) \x01(\x05\x12\x0e\n\x06Images\x18* \x03(\t\"\x18\n\x05Reply\x12\x0f\n\x07message\x18\x01 \x01(\x0c\"\xad\x07\n\x0cModelOptions\x12\r\n\x05Model\x18\x01 \x01(\t\x12\x13\n\x0b\x43ontextSize\x18\x02 \x01(\x05\x12\x0c\n\x04Seed\x18\x03 \x01(\x05\x12\x0e\n\x06NBatch\x18\x04 \x01(\x05\x12\x11\n\tF16Memory\x18\x05 \x01(\x08\x12\r\n\x05MLock\x18\x06 \x01(\x08\x12\x0c\n\x04MMap\x18\x07 \x01(\x08\x12\x11\n\tVocabOnly\x18\x08 \x01(\x08\x12\x0f\n\x07LowVRAM\x18\t \x01(\x08\x12\x12\n\nEmbeddings\x18\n \x01(\x08\x12\x0c\n\x04NUMA\x18\x0b \x01(\x08\x12\x12\n\nNGPULayers\x18\x0c \x01(\x05\x12\x0f\n\x07MainGPU\x18\r \x01(\t\x12\x13\n\x0bTensorSplit\x18\x0e \x01(\t\x12\x0f\n\x07Threads\x18\x0f \x01(\x05\x12\x19\n\x11LibrarySearchPath\x18\x10 \x01(\t\x12\x14\n\x0cRopeFreqBase\x18\x11 \x01(\x02\x12\x15\n\rRopeFreqScale\x18\x12 \x01(\x02\x12\x12\n\nRMSNormEps\x18\x13 \x01(\x02\x12\x0c\n\x04NGQA\x18\x14 \x01(\x05\x12\x11\n\tModelFile\x18\x15 \x01(\t\x12\x0e\n\x06\x44\x65vice\x18\x16 \x01(\t\x12\x11\n\tUseTriton\x18\x17 \x01(\x08\x12\x15\n\rModelBaseName\x18\x18 \x01(\t\x12\x18\n\x10UseFastTokenizer\x18\x19 \x01(\x08\x12\x14\n\x0cPipelineType\x18\x1a \x01(\t\x12\x15\n\rSchedulerType\x18\x1b \x01(\t\x12\x0c\n\x04\x43UDA\x18\x1c \x01(\x08\x12\x10\n\x08\x43\x46GScale\x18\x1d \x01(\x02\x12\x0f\n\x07IMG2IMG\x18\x1e \x01(\x08\x12\x11\n\tCLIPModel\x18\x1f \x01(\t\x12\x15\n\rCLIPSubfolder\x18  \x01(\t\x12\x10\n\x08\x43LIPSkip\x18! \x01(\x05\x12\x12\n\nControlNet\x18\x30 \x01(\t\x12\x11\n\tTokenizer\x18\" \x01(\t\x12\x10\n\x08LoraBase\x18# \x01(\t\x12\x13\n\x0bLoraAdapter\x18$ \x01(\t\x12\x11\n\tLoraScale\x18* \x01(\x02\x12\x11\n\tNoMulMatQ\x18% \x01(\x08\x12\x12\n\nDraftModel\x18\' \x01(\t\x12\x11\n\tAudioPath\x18& \x01(\t\x12\x14\n\x0cQuantization\x18( \x01(\t\x12\x0e\n\x06MMProj\x18) \x01(\t\x12\x13\n\x0bRopeScaling\x18+ \x01(\t\x12\x15\n\rYarnExtFactor\x18, \x01(\x02\x12\x16\n\x0eYarnAttnFactor\x18- \x01(\x02\x12\x14\n\x0cYarnBetaFast\x18. \x01(\x02\x12\x14\n\x0cYarnBetaSlow\x18/ \x01(\x02\"*\n\x06Result\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\"%\n\x0f\x45mbeddingResult\x12\x12\n\nembeddings\x18\x01 \x03(\x02\"C\n\x11TranscriptRequest\x12\x0b\n\x03\x64st\x18\x02 \x01(\t\x12\x10\n\x08language\x18\x03 \x01(\t\x12\x0f\n\x07threads\x18\x04 \x01(\r\"N\n\x10TranscriptResult\x12,\n\x08segments\x18\x01 \x03(\x0b\x32\x1a.backend.TranscriptSegment\x12\x0c\n\x04text\x18\x02 \x01(\t\"Y\n\x11TranscriptSegment\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05start\x18\x02 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x03 \x01(\x03\x12\x0c\n\x04text\x18\x04 \x01(\t\x12\x0e\n\x06tokens\x18\x05 \x03(\x05\"\xd7\x01\n\x14GenerateImageRequest\x12\x0e\n\x06height\x18\x01 \x01(\x05\x12\r\n\x05width\x18\x02 \x01(\x05\x12\x0c\n\x04mode\x18\x03 \x01(\x05\x12\x0c\n\x04step\x18\x04 \x01(\x05\x12\x0c\n\x04seed\x18\x05 \x01(\x05\x12\x17\n\x0fpositive_prompt\x18\x06 \x01(\t\x12\x17\n\x0fnegative_prompt\x18\x07 \x01(\t\x12\x0b\n\x03\x64st\x18\x08 \x01(\t\x12\x0b\n\x03src\x18\t \x01(\t\x12\x18\n\x10\x45nableParameters\x18\n \x01(\t\x12\x10\n\x08\x43LIPSkip\x18\x0b \x01(\x05\"6\n\nTTSRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\r\n\x05model\x18\x02 \x01(\t\x12\x0b\n\x03\x64st\x18\x03 \x01(\t\"6\n\x14TokenizationResponse\x12\x0e\n\x06length\x18\x01 \x01(\x05\x12\x0e\n\x06tokens\x18\x02 \x03(\x05\"\x8e\x01\n\x0fMemoryUsageData\x12\r\n\x05total\x18\x01 \x01(\x04\x12:\n\tbreakdown\x18\x02 \x03(\x0b\x32\'.backend.MemoryUsageData.BreakdownEntry\x1a\x30\n\x0e\x42reakdownEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x04:\x02\x38\x01\"\xad\x01\n\x0eStatusResponse\x12,\n\x05state\x18\x01 \x01(\x0e\x32\x1d.backend.StatusResponse.State\x12(\n\x06memory\x18\x02 \x01(\x0b\x32\x18.backend.MemoryUsageData\"C\n\x05State\x12\x11\n\rUNINITIALIZED\x10\x00\x12\x08\n\x04\x42USY\x10\x01\x12\t\n\x05READY\x10\x02\x12\x12\n\x05\x45RROR\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x32\xf4\x04\n\x07\x42\x61\x63kend\x12\x32\n\x06Health\x12\x16.backend.HealthMessage\x1a\x0e.backend.Reply\"\x00\x12\x34\n\x07Predict\x12\x17.backend.PredictOptions\x1a\x0e.backend.Reply\"\x00\x12\x35\n\tLoadModel\x12\x15.backend.ModelOptions\x1a\x0f.backend.Result\"\x00\x12<\n\rPredictStream\x12\x17.backend.PredictOptions\x1a\x0e.backend.Reply\"\x00\x30\x01\x12@\n\tEmbedding\x12\x17.backend.PredictOptions\x1a\x18.backend.EmbeddingResult\"\x00\x12\x41\n\rGenerateImage\x12\x1d.backend.GenerateImageRequest\x1a\x0f.backend.Result\"\x00\x12M\n\x12\x41udioTranscription\x12\x1a.backend.TranscriptRequest\x1a\x19.backend.TranscriptResult\"\x00\x12-\n\x03TTS\x12\x13.backend.TTSRequest\x1a\x0f.backend.Result\"\x00\x12J\n\x0eTokenizeString\x12\x17.backend.PredictOptions\x1a\x1d.backend.TokenizationResponse\"\x00\x12;\n\x06Status\x12\x16.backend.HealthMessage\x1a\x17.backend.StatusResponse\"\x00\x42Z\n\x19io.skynet.localai.backendB\x0eLocalAIBackendP\x01Z+github.com/go-skynet/LocalAI/pkg/grpc/protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'backend_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031io.skynet.localai.backendB\016LocalAIBackendP\001Z+github.com/go-skynet/LocalAI/pkg/grpc/proto'
  _globals['_MEMORYUSAGEDATA_BREAKDOWNENTRY']._options = None
  _globals['_MEMORYUSAGEDATA_BREAKDOWNENTRY']._serialized_options = b'8\001'
  _globals['_HEALTHMESSAGE']._serialized_start=26
  _globals['_HEALTHMESSAGE']._serialized_end=41
  _globals['_PREDICTOPTIONS']._serialized_start=44
  _globals['_PREDICTOPTIONS']._serialized_end=850
  _globals['_REPLY']._serialized_start=852
  _globals['_REPLY']._serialized_end=876
  _globals['_MODELOPTIONS']._serialized_start=879
  _globals['_MODELOPTIONS']._serialized_end=1820
  _globals['_RESULT']._serialized_start=1822
  _globals['_RESULT']._serialized_end=1864
  _globals['_EMBEDDINGRESULT']._serialized_start=1866
  _globals['_EMBEDDINGRESULT']._serialized_end=1903
  _globals['_TRANSCRIPTREQUEST']._serialized_start=1905
  _globals['_TRANSCRIPTREQUEST']._serialized_end=1972
  _globals['_TRANSCRIPTRESULT']._serialized_start=1974
  _globals['_TRANSCRIPTRESULT']._serialized_end=2052
  _globals['_TRANSCRIPTSEGMENT']._serialized_start=2054
  _globals['_TRANSCRIPTSEGMENT']._serialized_end=2143
  _globals['_GENERATEIMAGEREQUEST']._serialized_start=2146
  _globals['_GENERATEIMAGEREQUEST']._serialized_end=2361
  _globals['_TTSREQUEST']._serialized_start=2363
  _globals['_TTSREQUEST']._serialized_end=2417
  _globals['_TOKENIZATIONRESPONSE']._serialized_start=2419
  _globals['_TOKENIZATIONRESPONSE']._serialized_end=2473
  _globals['_MEMORYUSAGEDATA']._serialized_start=2476
  _globals['_MEMORYUSAGEDATA']._serialized_end=2618
  _globals['_MEMORYUSAGEDATA_BREAKDOWNENTRY']._serialized_start=2570
  _globals['_MEMORYUSAGEDATA_BREAKDOWNENTRY']._serialized_end=2618
  _globals['_STATUSRESPONSE']._serialized_start=2621
  _globals['_STATUSRESPONSE']._serialized_end=2794
  _globals['_STATUSRESPONSE_STATE']._serialized_start=2727
  _globals['_STATUSRESPONSE_STATE']._serialized_end=2794
  _globals['_BACKEND']._serialized_start=2797
  _globals['_BACKEND']._serialized_end=3425
# @@protoc_insertion_point(module_scope)
