import os
from typing import Dict, List, Tuple
from generator.template.utility import writer
from generator.template.vs2022.service_grpc import Program
from generator.template.vs2022.service_grpc import MyProgram
from generator.template.vs2022.service_grpc import ArgumentChecker
from generator.template.vs2022.service_grpc import ServiceBase
from generator.template.vs2022.service_grpc import Service
from generator.template.vs2022.service_grpc import appsettings
from generator.template.vs2022.service_grpc import DatabaseSettings
from generator.template.vs2022.service_grpc import DAO
from generator.template.vs2022.service_grpc import Entity

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
{{db_blocks}}
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="..\\fmp-{{org_lower}}-{{module_lower}}-lib-proto\\fmp-{{org_lower}}-{{module_lower}}-lib-proto.csproj" />
  </ItemGroup>

</Project>
"""

template_mongodb = """
    <PackageReference Include="MongoDB.Driver" Version="2.17.0" />
"""


def generate(
    _orgname: str,
    _modulename: str,
    _outputdir: str,
    _enums: List[str],
    _services: Dict[str, Dict[str, Tuple]],
    _messages: Dict[str, List[Tuple]],
    _databasedriver: str,
):
    contents = (
        template.replace("{{org}}", _orgname)
        .replace("{{module}}", _modulename)
        .replace("{{org_lower}}", _orgname.lower())
        .replace("{{module_lower}}", _modulename.lower())
    )
    if "mongodb" == _databasedriver:
        contents = contents.replace("{{db_blocks}}", template_mongodb)
    else:
        contents = contents.replace("{{db_blocks}}", "")
    project_name = "fmp-{}-{}-service-grpc".format(
        _orgname.lower(), _modulename.lower()
    )
    writer.writeVS2022Project(_outputdir, project_name, contents, False)
    # 生成Program
    Program.generate(
        _orgname,
        _modulename,
        os.path.join(_outputdir, project_name),
        _databasedriver,
        _enums,
        _services,
        _messages,
    )
    # 生成MyProgram
    MyProgram.generate(_orgname, _modulename, os.path.join(_outputdir, project_name))
    # 生成ServiceBase
    ServiceBase.generate(
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
    appsettings.generate(_orgname, _modulename, os.path.join(_outputdir, project_name), _databasedriver)
    # 生成ArgumentChekcer
    ArgumentChecker.generate(_orgname, _modulename, os.path.join(_outputdir, project_name))
    # 生成DatabaseSettings
    DatabaseSettings.generate(_orgname, _modulename, os.path.join(_outputdir, project_name), _databasedriver)
    # 生成DAO
    DAO.generate(_orgname, _modulename, os.path.join(_outputdir, project_name), _databasedriver)
    # 生成Entity
    Entity.generate(_orgname, _modulename, os.path.join(_outputdir, project_name), _databasedriver)
