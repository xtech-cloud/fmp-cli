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
from generator.template.vs2022.service_grpc import MongoDAO
from generator.template.vs2022.service_grpc import Entity
from generator.template.vs2022.service_grpc import SingletonServices

template = """
<Project Sdk="Microsoft.NET.Sdk.Web">

  <PropertyGroup>
    <TargetFramework>net7.0</TargetFramework>
    <Nullable>enable</Nullable>
    <ImplicitUsings>enable</ImplicitUsings>
    <RootNamespace>{{org}}.FMP.MOD.{{module}}.App.Service</RootNamespace>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="Grpc.AspNetCore" Version="2.51.0" />
    <PackageReference Include="Grpc.AspNetCore.HealthChecks" Version="2.51.0" />
    <PackageReference Include="Grpc.AspNetCore.Server.Reflection" Version="2.51.0" />
    <PackageReference Include="Grpc.AspNetCore.Web" Version="2.51.0" />
    <PackageReference Include="Microsoft.AspNetCore.Grpc.JsonTranscoding" Version="7.0.3" />
{{db_blocks}}
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="..\\fmp-{{org_lower}}-{{module_lower}}-lib-proto\\fmp-{{org_lower}}-{{module_lower}}-lib-proto.csproj" />
  </ItemGroup>

</Project>
"""

template_mongodb = """
    <PackageReference Include="MongoDB.Driver" Version="2.19.0" />
"""


def generate(_options, _outputdir: str):
    org_name = _options["org_name"]
    module_name = _options["module_name"]
    database_driver = _options["database_driver"]
    contents = (
        template.replace("{{org}}", org_name)
        .replace("{{module}}", module_name)
        .replace("{{org_lower}}", org_name.lower())
        .replace("{{module_lower}}", module_name.lower())
    )
    if "mongodb" == database_driver:
        contents = contents.replace("{{db_blocks}}", template_mongodb)
    else:
        contents = contents.replace("{{db_blocks}}", "")
    project_name = "fmp-{}-{}-service-grpc".format(
        org_name.lower(), module_name.lower()
    )
    writer.writeVS2022Project(_outputdir, project_name, contents, False)

    # 生成Program
    Program.generate(_options, os.path.join(_outputdir, project_name))
    # 生成MyProgram
    MyProgram.generate(_options, os.path.join(_outputdir, project_name))
    # 生成ServiceBase
    ServiceBase.generate(_options, os.path.join(_outputdir, project_name))
    # 生成Service
    Service.generate(_options, os.path.join(_outputdir, project_name))
    # 生成appsettings
    appsettings.generate(_options, os.path.join(_outputdir, project_name))
    # 生成ArgumentChekcer
    ArgumentChecker.generate(_options, os.path.join(_outputdir, project_name))
    # 生成DatabaseSettings
    DatabaseSettings.generate(_options, os.path.join(_outputdir, project_name))
    # 生成DAO
    MongoDAO.generate(_options, os.path.join(_outputdir, project_name))
    # 生成Entity
    Entity.generate(_options, os.path.join(_outputdir, project_name))
    # 生成SingletonServices
    SingletonServices.generate(_options, os.path.join(_outputdir, project_name))
