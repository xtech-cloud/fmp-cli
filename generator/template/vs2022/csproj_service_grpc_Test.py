import os
from typing import Dict, List, Tuple
from generator.template.utility import writer
from generator.template.vs2022.service_grpc_Test import Usings
from generator.template.vs2022.service_grpc_Test import TestServerCallContext
from generator.template.vs2022.service_grpc_Test import BaseTest
from generator.template.vs2022.service_grpc_Test import Test

template = """
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <TargetFramework>net6.0</TargetFramework>
    <RootNamespace>{{org}}.FMP.MOD.{{module}}.Test</RootNamespace>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>

    <IsPackable>false</IsPackable>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="Microsoft.NET.Test.Sdk" Version="17.1.0" />
    <PackageReference Include="xunit" Version="2.4.1" />
    <PackageReference Include="xunit.runner.visualstudio" Version="2.4.3">
      <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
      <PrivateAssets>all</PrivateAssets>
    </PackageReference>
    <PackageReference Include="coverlet.collector" Version="3.1.2">
      <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
      <PrivateAssets>all</PrivateAssets>
    </PackageReference>
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="..\\fmp-{{org_lower}}-{{module_lower}}-service-grpc\\fmp-{{org_lower}}-{{module_lower}}-service-grpc.csproj" />
  </ItemGroup>

</Project>

"""


def generate(
    _orgname: str,
    _modulename: str,
    _outputdir: str,
    _enums: List[str],
    _services: Dict[str, Dict[str, Tuple]],
    _messages: Dict[str, List[Tuple]],
):
    contents = (
        template.replace("{{org}}", _orgname)
        .replace("{{module}}", _modulename)
        .replace("{{org_lower}}", _orgname.lower())
        .replace("{{module_lower}}", _modulename.lower())
    )
    project_name = "fmp-{}-{}-service-grpc_Test".format(
        _orgname.lower(), _modulename.lower()
    )
    writer.writeVS2022Project(_outputdir, project_name, contents, False)
    # ??????Usings
    Usings.generate(_orgname, _modulename, os.path.join(_outputdir, project_name))
    # ??????TestServerCallContext
    TestServerCallContext.generate(_orgname, _modulename, os.path.join(_outputdir, project_name))
    # ??????BaseTest
    BaseTest.generate(_orgname, _modulename, os.path.join(_outputdir, project_name), _enums, _services, _messages)
    # ??????Test
    Test.generate(_orgname, _modulename, os.path.join(_outputdir, project_name), _enums, _services, _messages)
