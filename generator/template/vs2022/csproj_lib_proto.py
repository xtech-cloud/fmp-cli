import os
from typing import Dict, List, Tuple
from generator.template.utility import writer

template = """
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <TargetFramework>netstandard2.0</TargetFramework>
    <RootNamespace>{{org}}.FMP.MOD.{{module}}.LIB.Proto</RootNamespace>
  </PropertyGroup>

  <ItemGroup>
    <Protobuf Include="..\\..\\proto\\{{module}}\\*.proto" GrpcServices="Both" />
    <PackageReference Include="Google.Api.CommonProtos" Version="2.6.0" />
    <PackageReference Include="Grpc.Core" Version="2.46.3" />
    <PackageReference Include="Grpc.Tools" Version="2.47.0">
      <PrivateAssets>all</PrivateAssets>
      <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
    </PackageReference>
  </ItemGroup>

</Project>
"""


def generate(_orgname: str, _modulename: str, _outputdir: str):
    contents = template.replace("{{org}}", _orgname).replace("{{module}}", _modulename)
    project_name = "fmp-{}-{}-lib-proto".format(_orgname.lower(), _modulename.lower())
    writer.writeVS2022Project(_outputdir, project_name, contents, False)
