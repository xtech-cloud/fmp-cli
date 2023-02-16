import os
import uuid
from generator.template.utility import writer
from generator.template.unity2021.assets.lib3rd.binhex import fmp_lib_mvcs
from generator.template.unity2021.assets.lib3rd.binhex import Google_Protobuf
from generator.template.unity2021.assets.lib3rd.binhex import Google_Api_CommonProtos
from generator.template.unity2021.assets.lib3rd.binhex import Grpc_Core_Api
from generator.template.unity2021.assets.lib3rd.binhex import Grpc_Net_Client
from generator.template.unity2021.assets.lib3rd.binhex import Grpc_Net_Client_Web
from generator.template.unity2021.assets.lib3rd.binhex import Grpc_Net_Common
from generator.template.unity2021.assets.lib3rd.binhex import Microsoft_Extensions_Logging_Abstractions
from generator.template.unity2021.assets.lib3rd.binhex import System_Diagnostics_DiagnosticSource
from generator.template.unity2021.assets.lib3rd.binhex import System_Runtime_CompilerServices_Unsafe
from generator.template.unity2021.assets.lib3rd.binhex import Newtonsoft_Json

def writeMVCS(_outputdir:str):
    output_dir = os.path.join(_outputdir, "fmp-lib-mvcs-1.6.1")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "fmp-lib-mvcs.dll")
    writer.writeHexToBinary(output_path, fmp_lib_mvcs.bin_hex, True)

def writeDependency(_outputdir:str):
    output_dir = os.path.join(_outputdir, "fmp-dependency")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "Google.Api.CommonProtos.dll")
    writer.writeHexToBinary(output_path, Google_Api_CommonProtos.bin_hex, True)
    output_path = os.path.join(output_dir, "Google.Protobuf.dll")
    writer.writeHexToBinary(output_path, Google_Protobuf.bin_hex, True)
    output_path = os.path.join(output_dir, "Grpc.Core.Api.dll")
    writer.writeHexToBinary(output_path, Grpc_Core_Api.bin_hex, True)
    output_path = os.path.join(output_dir, "Grpc.Net.Client.dll")
    writer.writeHexToBinary(output_path, Grpc_Net_Client.bin_hex, True)
    output_path = os.path.join(output_dir, "Grpc.Net.Client.Web.dll")
    writer.writeHexToBinary(output_path, Grpc_Net_Client_Web.bin_hex, True)
    output_path = os.path.join(output_dir, "Grpc.Net.Common.dll")
    writer.writeHexToBinary(output_path, Grpc_Net_Common.bin_hex, True)
    output_path = os.path.join(output_dir, "Microsoft.Extensions.Logging.Abstractions.dll")
    writer.writeHexToBinary(output_path, Microsoft_Extensions_Logging_Abstractions.bin_hex, True)
    output_path = os.path.join(output_dir, "System.Diagnostics.DiagnosticSource.dll")
    writer.writeHexToBinary(output_path, System_Diagnostics_DiagnosticSource.bin_hex, True)
    output_path = os.path.join(output_dir, "System.Runtime.CompilerServices.Unsafe.dll")
    writer.writeHexToBinary(output_path, System_Runtime_CompilerServices_Unsafe.bin_hex, True)
    output_path = os.path.join(output_dir, "Newtonsoft.Json.dll")
    writer.writeHexToBinary(output_path, Newtonsoft_Json.bin_hex, True)

def generate(_options, _outputdir: str):
    output_dir = os.path.join(_outputdir, "Assets")
    os.makedirs(output_dir, exist_ok=True)
    output_dir = os.path.join(output_dir, "3rd")
    os.makedirs(output_dir, exist_ok=True)

    writeMVCS(output_dir)
    writeDependency(output_dir)
