import os
from typing import Dict, List, Tuple
from generator.template.utility import writer
from generator.template.vs2022.lib_mvcs import ProtoDTO
from generator.template.vs2022.lib_mvcs import Entry
from generator.template.vs2022.lib_mvcs import BaseEntry
from generator.template.vs2022.lib_mvcs import BaseModel
from generator.template.vs2022.lib_mvcs import Model
from generator.template.vs2022.lib_mvcs import BaseView
from generator.template.vs2022.lib_mvcs import View
from generator.template.vs2022.lib_mvcs import BaseController
from generator.template.vs2022.lib_mvcs import Controller
from generator.template.vs2022.lib_mvcs import BaseService
from generator.template.vs2022.lib_mvcs import Service
from generator.template.vs2022.lib_mvcs import Facade
from generator.template.vs2022.lib_mvcs import ViewBridge
from generator.template.vs2022.lib_mvcs import BaseViewBridge

template = """
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <TargetFramework>netstandard2.0</TargetFramework>
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
    project_name = "fmp-{}-{}-lib-mvcs".format(_orgname.lower(), _modulename.lower())
    writer.writeVS2022Project(_outputdir, project_name, contents, False)
    # ??????ProtoDTO
    ProtoDTO.generate(
        _orgname,
        _modulename,
        os.path.join(_outputdir, project_name),
        _enums,
        _services,
        _messages,
    )
    # ??????Entry
    Entry.generate(_orgname, _modulename, os.path.join(_outputdir, project_name))
    # ??????BaseEntry
    BaseEntry.generate(
        _orgname,
        _modulename,
        os.path.join(_outputdir, project_name),
        _enums,
        _services,
        _messages,
    )
    # ??????BaseModel
    BaseModel.generate(
        _orgname,
        _modulename,
        os.path.join(_outputdir, project_name),
        _enums,
        _services,
        _messages,
    )
    # ??????Model
    Model.generate(
        _orgname,
        _modulename,
        os.path.join(_outputdir, project_name),
        _enums,
        _services,
        _messages,
    )
    # ??????BaseView
    BaseView.generate(
        _orgname,
        _modulename,
        os.path.join(_outputdir, project_name),
        _enums,
        _services,
        _messages,
    )
    # ??????View
    View.generate(
        _orgname,
        _modulename,
        os.path.join(_outputdir, project_name),
        _enums,
        _services,
        _messages,
    )
    # ??????BaseController
    BaseController.generate(
        _orgname,
        _modulename,
        os.path.join(_outputdir, project_name),
        _enums,
        _services,
        _messages,
    )
    # ??????Controller
    Controller.generate(
        _orgname,
        _modulename,
        os.path.join(_outputdir, project_name),
        _enums,
        _services,
        _messages,
    )
    # ??????BaseService
    BaseService.generate(
        _orgname,
        _modulename,
        os.path.join(_outputdir, project_name),
        _enums,
        _services,
        _messages,
    )
    # ??????Service
    Service.generate(
        _orgname,
        _modulename,
        os.path.join(_outputdir, project_name),
        _enums,
        _services,
        _messages,
    )
    # ??????Facade
    Facade.generate(
        _orgname,
        _modulename,
        os.path.join(_outputdir, project_name),
        _enums,
        _services,
        _messages,
    )
    # ??????BaseViewBridge
    BaseViewBridge.generate(
        _orgname,
        _modulename,
        os.path.join(_outputdir, project_name),
        _enums,
        _services,
        _messages,
    )
    # ??????ViewBridge
    ViewBridge.generate(
        _orgname,
        _modulename,
        os.path.join(_outputdir, project_name),
        _enums,
        _services,
        _messages,
    )
