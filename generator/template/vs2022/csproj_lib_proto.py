import os
from typing import Dict, List, Tuple
from generator.template.utility import writer

template = """
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <TargetFramework>netstandard2.1</TargetFramework>
    <RootNamespace>{{org}}.FMP.MOD.{{module}}.LIB.Proto</RootNamespace>
  </PropertyGroup>

  <ItemGroup>
    <Protobuf Include="..\\..\\proto\\{{module}}\\*.proto" GrpcServices="Both" />
    <PackageReference Include="Google.Api.CommonProtos" Version="2.7.0" />
    <PackageReference Include="Grpc.Core" Version="2.46.6" />
    <PackageReference Include="Grpc.Tools" Version="2.51.0">
      <PrivateAssets>all</PrivateAssets>
      <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
    </PackageReference>
  </ItemGroup>

</Project>
"""


def generate(_options, _outputdir: str):
    org_name = _options["org_name"]
    module_name = _options["module_name"]
    contents = template.replace("{{org}}", org_name).replace("{{module}}", module_name)
    project_name = "fmp-{}-{}-lib-proto".format(org_name.lower(), module_name.lower())
    writer.writeVS2022Project(_outputdir, project_name, contents, False)
