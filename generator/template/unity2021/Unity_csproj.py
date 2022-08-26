import os
from generator.template.utility import writer

template = r"""
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <TargetFramework>netstandard2.1</TargetFramework>
    <AssemblyName>{{org_name}}.FMP.MOD.{{module_name}}.LIB.Unity</AssemblyName>
    <Version>1.0.0</Version>
    <RootNamespace />
  </PropertyGroup>

  <ItemGroup>
    <Reference Include="fmp-lib-mvcs">
      <HintPath>{{WORK_DIR}}\{{module_name}}\Assets\3rd\fmp-lib-mvcs-1.6.1\fmp-lib-mvcs.dll</HintPath>
    </Reference>
    <Reference Include="Newtonsoft.Json">
      <HintPath>{{WORK_DIR}}\{{module_name}}\Assets\3rd\fmp-dependency\Newtonsoft.Json.dll</HintPath>
    </Reference>
    <Reference Include="Google.Protobuf">
      <HintPath>{{WORK_DIR}}\{{module_name}}\Assets\3rd\fmp-dependency\Google.Protobuf.dll</HintPath>
    </Reference>
    <Reference Include="Grpc.Core.Api">
      <HintPath>{{WORK_DIR}}\{{module_name}}\Assets\3rd\fmp-dependency\Grpc.Core.Api.dll</HintPath>
    </Reference>
    <Reference Include="Grpc.Net.Client">
      <HintPath>{{WORK_DIR}}\{{module_name}}\Assets\3rd\fmp-dependency\Grpc.Net.Client.dll</HintPath>
    </Reference>
    <Reference Include="Grpc.Net.Client.Web">
      <HintPath>{{WORK_DIR}}\{{module_name}}\Assets\3rd\fmp-dependency\Grpc.Net.Client.Web.dll</HintPath>
    </Reference>
    <Reference Include="Grpc.Net.Common">
      <HintPath>{{WORK_DIR}}\{{module_name}}\Assets\3rd\fmp-dependency\Grpc.Net.Common.dll</HintPath>
    </Reference>
    <Reference Include="Microsoft.Extensions.Logging.Abstractions">
      <HintPath>{{WORK_DIR}}\{{module_name}}\Assets\3rd\fmp-dependency\Microsoft.Extensions.Logging.Abstractions.dll</HintPath>
    </Reference>
    <Reference Include="System.Diagnostics.DiagnosticSource">
      <HintPath>{{WORK_DIR}}\{{module_name}}\Assets\3rd\fmp-dependency\System.Diagnostics.DiagnosticSource.dll</HintPath>
    </Reference>
    <Reference Include="System.Runtime.CompilerServices.Unsafe">
      <HintPath>{{WORK_DIR}}\{{module_name}}\Assets\3rd\fmp-dependency\System.Runtime.CompilerServices.Unsafe.dll</HintPath>
    </Reference>
    <Reference Include="fmp-{{org_name_lower}}-{{module_name_lower}}-lib-bridge">
      <HintPath>{{WORK_DIR}}\{{module_name}}\Assets\3rd\fmp-{{org_name_lower}}-{{module_name_lower}}\fmp-{{org_name_lower}}-{{module_name_lower}}-lib-bridge.dll</HintPath>
    </Reference>
    <Reference Include="fmp-{{org_name_lower}}-{{module_name_lower}}-lib-mvcs">
      <HintPath>{{WORK_DIR}}\{{module_name}}\Assets\3rd\fmp-{{org_name_lower}}-{{module_name_lower}}\fmp-{{org_name_lower}}-{{module_name_lower}}-lib-mvcs.dll</HintPath>
    </Reference>
    <Reference Include="fmp-{{org_name_lower}}-{{module_name}}-lib-proto">
      <HintPath>{{WORK_DIR}}\{{module_name}}\Assets\3rd\fmp-{{org_name_lower}}-{{module_name_lower}}\fmp-{{org_name_lower}}-{{module_name_lower}}-lib-proto.dll</HintPath>
    </Reference>
    <Reference Include="UnityEngine.UI">
      <HintPath>{{WORK_DIR}}\{{module_name}}\Library\ScriptAssemblies\UnityEngine.UI.dll</HintPath>
    </Reference>
    <Reference Include="UnityEngine">
      <HintPath>{{UNITY_HOME}}\Editor\Data\Managed\UnityEngine\UnityEngine.dll</HintPath>
    </Reference>
    <Reference Include="UnityEngine.CoreModule">
      <HintPath>{{UNITY_HOME}}\Editor\Data\Managed\UnityEngine\UnityEngine.CoreModule.dll</HintPath>
    </Reference>
    <Reference Include="UnityEngine.AudioModule">
      <HintPath>{{UNITY_HOME}}\Editor\Data\Managed\UnityEngine\UnityEngine.AudioModule.dll</HintPath>
    </Reference>
    <Reference Include="UnityEngine.UnityWebRequestModule">
      <HintPath>{{UNITY_HOME}}\Editor\Data\Managed\UnityEngine\UnityEngine.UnityWebRequestModule.dll</HintPath>
    </Reference>
    <Reference Include="UnityEngine.AssetBundleModule">
      <HintPath>{{UNITY_HOME}}\Editor\Data\Managed\UnityEngine\UnityEngine.AssetBundleModule.dll</HintPath>
    </Reference>
    <Reference Include="UnityEngine.UnityWebRequestAssetBundleModule">
      <HintPath>{{UNITY_HOME}}\Editor\Data\Managed\UnityEngine\UnityEngine.UnityWebRequestAssetBundleModule.dll</HintPath>
    </Reference>
    <Reference Include="UnityEngine.UnityWebRequestAudioModule">
      <HintPath>{{UNITY_HOME}}\Editor\Data\Managed\UnityEngine\UnityEngine.UnityWebRequestAudioModule.dll</HintPath>
    </Reference>
    <Reference Include="UnityEngine.UnityWebRequestTextureModule">
      <HintPath>{{UNITY_HOME}}\Editor\Data\Managed\UnityEngine\UnityEngine.UnityWebRequestTextureModule.dll</HintPath>
    </Reference>
    <Reference Include="UnityEngine.ImageConversionModule">
      <HintPath>{{UNITY_HOME}}\Editor\Data\Managed\UnityEngine\UnityEngine.ImageConversionModule.dll</HintPath>
    </Reference>
  </ItemGroup>

</Project>
"""

def generate(_options, _outputdir: str):
    output_dir = _outputdir

    contents = template
    contents = contents.replace("{{version}}", _options["version"])
    contents = contents.replace("{{org_name}}", _options["org_name"])
    contents = contents.replace("{{module_name}}", _options["module_name"])
    contents = contents.replace("{{org_name_lower}}", _options["org_name"].lower())
    contents = contents.replace("{{module_name_lower}}", _options["module_name"].lower())
    output_path = os.path.join(output_dir, "Unity.csproj.keep")
    writer.write(output_path, contents, False)
