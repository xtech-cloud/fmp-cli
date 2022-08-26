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
    <TargetFramework>netstandard2.1</TargetFramework>
    <RootNamespace>{{org}}.FMP.MOD.{{module}}.LIB.Bridge</RootNamespace>
    <LangVersion>8.0</LangVersion>
    <Nullable>enable</Nullable>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="fmp-lib-mvcs" Version="1.6.1" />
  </ItemGroup>

</Project>
"""


def generate(_options, _outputdir: str):
    # 生成项目文件
    org_name = _options["org_name"]
    module_name = _options["module_name"]
    contents = template.replace("{{org}}", org_name).replace("{{module}}", module_name)
    project_name = "fmp-{}-{}-lib-bridge".format(org_name.lower(), module_name.lower())
    writer.writeVS2022Project(_outputdir, project_name, contents, False)
    # 生成IDTO
    IDTO.generate(_options, os.path.join(_outputdir, project_name))
    # 生成IUiBridge.cs
    IUiBridge.generate(_options, os.path.join(_outputdir, project_name))
    # 生成IUiProtoBridge.cs
    IUiProtoBridge.generate(_options, os.path.join(_outputdir, project_name))
    # 生成IViewBridge.cs
    IViewBridge.generate(_options, os.path.join(_outputdir, project_name))
    # 生成IViewProtoBridge.cs
    IViewProtoBridge.generate(_options, os.path.join(_outputdir, project_name))
