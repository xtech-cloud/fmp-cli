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
    <PackageReference Include="AntDesign" Version="0.12.0" />
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


def generate(_options, _outputdir: str):
    org_name = _options["org_name"]
    module_name = _options["module_name"]
    contents = (
        template.replace("{{org}}", org_name)
        .replace("{{module}}", module_name)
        .replace("{{org_lower}}", org_name.lower())
        .replace("{{module_lower}}", module_name.lower())
    )
    project_name = "fmp-{}-{}-lib-razor".format(org_name.lower(), module_name.lower())
    writer.writeVS2022Project(_outputdir, project_name, contents, False)
    # 生成_Imports
    _Imports.generate(_options, os.path.join(_outputdir, project_name))
    # 生成Component
    Component.generate(_options, os.path.join(_outputdir, project_name))
