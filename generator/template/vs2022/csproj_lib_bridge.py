import os
from typing import Dict, List, Tuple
from generator.template.utility import writer
from generator.template.vs2022.lib_bridge import IDTO
from generator.template.vs2022.lib_bridge import IUiBridge
from generator.template.vs2022.lib_bridge import IUiProtoBridge
from generator.template.vs2022.lib_bridge import IViewBridge
from generator.template.vs2022.lib_bridge import IViewProtoBridge

template = """
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <TargetFramework>netstandard2.0</TargetFramework>
    <RootNamespace>{{org}}.FMP.MOD.{{module}}.LIB.Bridge</RootNamespace>
    <LangVersion>8.0</LangVersion>
    <Nullable>enable</Nullable>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="fmp-lib-mvcs" Version="1.6.0" />
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
    # 生成项目文件
    contents = template.replace("{{org}}", _orgname).replace("{{module}}", _modulename)
    project_name = "fmp-{}-{}-lib-bridge".format(_orgname.lower(), _modulename.lower())
    writer.writeVS2022Project(_outputdir, project_name, contents, False)
    # 生成IDTO
    IDTO.generate(_orgname, _modulename, os.path.join(_outputdir, project_name))
    # 生成IUiBridge.cs
    IUiBridge.generate(
        _orgname,
        _modulename,
        os.path.join(_outputdir, project_name),
        _enums,
        _services,
        _messages,
    )
    # 生成IUiProtoBridge.cs
    IUiProtoBridge.generate(
        _orgname,
        _modulename,
        os.path.join(_outputdir, project_name),
        _enums,
        _services,
        _messages,
    )
    # 生成IViewBridge.cs
    IViewBridge.generate(
        _orgname,
        _modulename,
        os.path.join(_outputdir, project_name),
        _enums,
        _services,
        _messages,
    )
    # 生成IViewProtoBridge.cs
    IViewProtoBridge.generate(
        _orgname,
        _modulename,
        os.path.join(_outputdir, project_name),
        _enums,
        _services,
        _messages,
    )
