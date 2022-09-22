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
    <TargetFramework>net6.0</TargetFramework>
    <RazorLangVersion>3.0</RazorLangVersion>
    <RootNamespace>{{org}}.FMP.MOD.{{module}}.App.Web</RootNamespace>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="AntDesign.Charts" Version="0.2.3" />
    <PackageReference Include="AntDesign.ProLayout" Version="0.12.4" />
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


def generate(_options, _outputdir: str):
    org_name = _options["org_name"]
    module_name = _options["module_name"]
    datbase_driver = _options["database_driver"]

    contents = (
        template.replace("{{org}}", org_name)
        .replace("{{module}}", module_name)
        .replace("{{org_lower}}", org_name.lower())
        .replace("{{module_lower}}", module_name.lower())
    )
    project_name = "fmp-{}-{}-web-blazor".format(org_name.lower(), module_name.lower())
    writer.writeVS2022Project(_outputdir, project_name, contents, False)

    # 生成Program
    Program.generate(_options, os.path.join(_outputdir, project_name))
    # 生成ConsoleLogger
    ConsoleLogger.generate(_options, os.path.join(_outputdir, project_name))
    # 生成_Imports
    _Imports.generate(_options, os.path.join(_outputdir, project_name))
    # 生成App
    App.generate(_options, os.path.join(_outputdir, project_name))
    # 生成Pages/Welcome
    Welcome.generate(_options, os.path.join(_outputdir, project_name))
    # 生成Layouts/BasicLayout
    BasicLayout.generate(_options, os.path.join(_outputdir, project_name))
    # 生成Properties/launchSettings
    launchSettings.generate(_options, os.path.join(_outputdir, project_name))
    # 生成wwwroot/index
    index.generate(_options, os.path.join(_outputdir, project_name))
    # 生成wwwroot/appsettings
    appsettings.generate(_options, os.path.join(_outputdir, project_name))
    # 生成wwwroot/css/site
    site.generate(_options, os.path.join(_outputdir, project_name))
