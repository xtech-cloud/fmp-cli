import os
from typing import Dict, List, Tuple
from generator.template.utility import writer
from generator.template.vs2022.web_blazor import Program
from generator.template.vs2022.web_blazor import ConsoleLogger
from generator.template.vs2022.web_blazor import App
from generator.template.vs2022.web_blazor import _Imports
from generator.template.vs2022.web_blazor.Layouts import BasicLayout
from generator.template.vs2022.web_blazor.Pages import Welcome
from generator.template.vs2022.web_blazor.Properties import launchSettings
from generator.template.vs2022.web_blazor.wwwroot import index
from generator.template.vs2022.web_blazor.wwwroot import appsettings
from generator.template.vs2022.web_blazor.wwwroot.css import site

template = """
<Project Sdk="Microsoft.NET.Sdk.BlazorWebAssembly">

  <PropertyGroup>
    <TargetFramework>net6</TargetFramework>
    <RazorLangVersion>3.0</RazorLangVersion>
    <RootNamespace>{{org}}.FMP.MOD.{{module}}.App.Web</RootNamespace>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="AntDesign.Charts" Version="0.2.3" />
    <PackageReference Include="AntDesign.ProLayout" Version="0.10.6" />
    <PackageReference Include="Microsoft.AspNetCore.Components.WebAssembly" Version="6.0.0" />
    <PackageReference Include="Microsoft.AspNetCore.Components.WebAssembly.DevServer" Version="6.0.0" PrivateAssets="all" />
    <PackageReference Include="Microsoft.Extensions.Options.ConfigurationExtensions" Version="6.0.0" />
    <PackageReference Include="System.Net.Http.Json" Version="6.0.0" />
    <PackageReference Include="Grpc.Net.Client.Web" Version="2.47.0" />
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="..\\fmp-{{org_lower}}-{{module_lower}}-lib-razor\\fmp-{{org_lower}}-{{module_lower}}-lib-razor.csproj" />
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
    project_name = "fmp-{}-{}-web-blazor".format(_orgname.lower(), _modulename.lower())
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
    # 生成ConsoleLogger
    ConsoleLogger.generate(
        _orgname, _modulename, os.path.join(_outputdir, project_name)
    )
    # 生成_Imports
    _Imports.generate(_orgname, _modulename, os.path.join(_outputdir, project_name))
    # 生成App
    App.generate(
        _orgname,
        _modulename,
        os.path.join(_outputdir, project_name),
        _enums,
        _services,
        _messages,
    )
    # 生成Pages/Welcome
    Welcome.generate(_orgname, _modulename, os.path.join(_outputdir, project_name))
    # 生成Layouts/BasicLayout
    BasicLayout.generate(
        _orgname,
        _modulename,
        os.path.join(_outputdir, project_name),
        _enums,
        _services,
        _messages,
    )
    # 生成Properties/launchSettings
    launchSettings.generate(
        _orgname, _modulename, os.path.join(_outputdir, project_name)
    )
    # 生成wwwroot/index
    index.generate(_orgname, _modulename, os.path.join(_outputdir, project_name))
    # 生成wwwroot/appsettings
    appsettings.generate(_orgname, _modulename, os.path.join(_outputdir, project_name))
    # 生成wwwroot/css/site
    site.generate(_orgname, _modulename, os.path.join(_outputdir, project_name))
