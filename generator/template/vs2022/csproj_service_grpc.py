import os
from typing import Dict, List, Tuple
from generator.template.utility import writer
from generator.template.vs2022.service_grpc import Program
from generator.template.vs2022.service_grpc import MyProgram
from generator.template.vs2022.service_grpc import BaseService
from generator.template.vs2022.service_grpc import Service
from generator.template.vs2022.service_grpc import appsettings

template = """
<Project Sdk="Microsoft.NET.Sdk.Web">

  <PropertyGroup>
    <TargetFramework>net6.0</TargetFramework>
    <Nullable>enable</Nullable>
    <ImplicitUsings>enable</ImplicitUsings>
    <RootNamespace>{{org}}.FMP.MOD.{{module}}.App.Service</RootNamespace>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="Grpc.AspNetCore" Version="2.40.0" />
    <PackageReference Include="Grpc.AspNetCore.HealthChecks" Version="2.46.0" />
    <PackageReference Include="Grpc.AspNetCore.Server.Reflection" Version="2.47.0-pre1" />
    <PackageReference Include="Grpc.AspNetCore.Web" Version="2.46.0" />
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="..\\fmp-{{org_lower}}-{{module_lower}}-lib-proto\\fmp-{{org_lower}}-{{module_lower}}-lib-proto.csproj" />
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
    project_name = "fmp-{}-{}-service-grpc".format(
        _orgname.lower(), _modulename.lower()
    )
    writer.writeVS2022Project(_outputdir, project_name, contents, False)
    # 生成Program
    Program.generate(
        _orgname,
        _modulename,
        os.path.join(_outputdir, project_name),
        _enums,
        _services,
        _messages,
    )
    # 生成MyProgram
    MyProgram.generate(_orgname, _modulename, os.path.join(_outputdir, project_name))
    # 生成BaseService
    BaseService.generate(
        _orgname,
        _modulename,
        os.path.join(_outputdir, project_name),
        _enums,
        _services,
        _messages,
    )
    # 生成Service
    Service.generate(
        _orgname,
        _modulename,
        os.path.join(_outputdir, project_name),
        _enums,
        _services,
        _messages,
    )
    # 生成appsettings
    appsettings.generate(_orgname, _modulename, os.path.join(_outputdir, project_name))
