import os
from typing import Dict, List, Tuple
from generator.template.utility import writer
from generator.template.vs2022.lib_mvcs import ProtoDTO
from generator.template.vs2022.lib_mvcs import Subjects
from generator.template.vs2022.lib_mvcs import Entry
from generator.template.vs2022.lib_mvcs import EntryBase
from generator.template.vs2022.lib_mvcs import ModelBase
from generator.template.vs2022.lib_mvcs import Model
from generator.template.vs2022.lib_mvcs import ViewBase
from generator.template.vs2022.lib_mvcs import View
from generator.template.vs2022.lib_mvcs import ControllerBase
from generator.template.vs2022.lib_mvcs import Controller
from generator.template.vs2022.lib_mvcs import ServiceMock
from generator.template.vs2022.lib_mvcs import ServiceBase
from generator.template.vs2022.lib_mvcs import Service
from generator.template.vs2022.lib_mvcs import Facade
from generator.template.vs2022.lib_mvcs import ViewBridge
from generator.template.vs2022.lib_mvcs import ViewBridgeBase

template = """
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <TargetFramework>netstandard2.1</TargetFramework>
    <RootNamespace>{{org}}.FMP.MOD.{{module}}.LIB.MVCS</RootNamespace>
    <LangVersion>8.0</LangVersion>
    <Nullable>enable</Nullable>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="fmp-lib-mvcs" Version="1.6.0" />
    <PackageReference Include="Grpc.Net.Client" Version="2.47.0" />
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="..\\fmp-{{org_lower}}-{{module_lower}}-lib-bridge\\fmp-{{org_lower}}-{{module_lower}}-lib-bridge.csproj" />
    <ProjectReference Include="..\\fmp-{{org_lower}}-{{module_lower}}-lib-proto\\fmp-{{org_lower}}-{{module_lower}}-lib-proto.csproj" />
  </ItemGroup>

</Project>

"""


def generate(_options, _outputdir: str):
    org_name = _options["org_name"]
    module_name = _options["module_name"]

    contents = (
        template.replace("{{org}}", org_name)
        .replace("{{module}}", module_name)
        .replace("{{org_lower}}", org_name.lower())
        .replace("{{module_lower}}", module_name.lower())
    )
    project_name = "fmp-{}-{}-lib-mvcs".format(org_name.lower(), module_name.lower())
    writer.writeVS2022Project(_outputdir, project_name, contents, False)
    # 生成ProtoDTO
    ProtoDTO.generate(_options, os.path.join(_outputdir, project_name))
    # 生成Subjects
    Subjects.generate(_options, os.path.join(_outputdir, project_name))
    # 生成Entry
    Entry.generate(_options, os.path.join(_outputdir, project_name))
    # 生成BaseEntry
    EntryBase.generate(_options, os.path.join(_outputdir, project_name))
    # 生成BaseModel
    ModelBase.generate(_options, os.path.join(_outputdir, project_name))
    # 生成Model
    Model.generate(_options, os.path.join(_outputdir, project_name))
    # 生成BaseView
    ViewBase.generate(_options, os.path.join(_outputdir, project_name))
    # 生成View
    View.generate(_options, os.path.join(_outputdir, project_name))
    # 生成BaseController
    ControllerBase.generate(_options, os.path.join(_outputdir, project_name))
    # 生成Controller
    Controller.generate(_options, os.path.join(_outputdir, project_name))
    # 生成ServiceMock
    ServiceMock.generate(_options, os.path.join(_outputdir, project_name))
    # 生成BaseService
    ServiceBase.generate(_options, os.path.join(_outputdir, project_name))
    # 生成Service
    Service.generate(_options, os.path.join(_outputdir, project_name))
    # 生成Facade
    Facade.generate(_options, os.path.join(_outputdir, project_name))
    # 生成BaseViewBridge
    ViewBridgeBase.generate(_options, os.path.join(_outputdir, project_name))
    # 生成ViewBridge
    ViewBridge.generate(_options, os.path.join(_outputdir, project_name))
