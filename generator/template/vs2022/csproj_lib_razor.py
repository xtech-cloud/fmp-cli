import os
from typing import Dict, List, Tuple
from generator.template.utility import writer
from generator.template.vs2022.lib_razor import _Imports
from generator.template.vs2022.lib_razor import Component

template = """
<Project Sdk="Microsoft.NET.Sdk.Razor">

  <PropertyGroup>
    <TargetFramework>net6.0</TargetFramework>
    <Nullable>enable</Nullable>
    <ImplicitUsings>enable</ImplicitUsings>
    <RootNamespace>{{org}}.FMP.MOD.{{module}}.LIB.Razor</RootNamespace>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="AntDesign.ProLayout" Version="0.10.6" />
  </ItemGroup>


  <ItemGroup>
    <SupportedPlatform Include="browser" />
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="..\\fmp-{{org_lower}}-{{module_lower}}-lib-mvcs\\fmp-{{org_lower}}-{{module_lower}}-lib-mvcs.csproj" />
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
    project_name = "fmp-{}-{}-lib-razor".format(_orgname.lower(), _modulename.lower())
    writer.writeVS2022Project(_outputdir, project_name, contents, False)
    # 生成_Imports
    _Imports.generate(_orgname, _modulename, os.path.join(_outputdir, project_name))
    # 生成Component
    Component.generate(
        _orgname,
        _modulename,
        os.path.join(_outputdir, project_name),
        _enums,
        _services,
        _messages,
    )
