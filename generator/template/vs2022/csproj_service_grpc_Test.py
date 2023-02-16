import os
from typing import Dict, List, Tuple
from generator.template.utility import writer
from generator.template.vs2022.service_grpc_Test import Usings
from generator.template.vs2022.service_grpc_Test import TestServerCallContext
from generator.template.vs2022.service_grpc_Test import UnitTestBase
from generator.template.vs2022.service_grpc_Test import UnitTest
from generator.template.vs2022.service_grpc_Test import IntegrationTestBase
from generator.template.vs2022.service_grpc_Test import IntegrationTest
from generator.template.vs2022.service_grpc_Test import DatabaseOptions
from generator.template.vs2022.service_grpc_Test import TestFixtureBase
from generator.template.vs2022.service_grpc_Test import TestFixture

template = """
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <TargetFramework>net7.0</TargetFramework>
    <RootNamespace>{{org}}.FMP.MOD.{{module}}.Test</RootNamespace>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>

    <IsPackable>false</IsPackable>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="Microsoft.NET.Test.Sdk" Version="17.1.0" />
    <PackageReference Include="Moq" Version="4.18.1" />
    <PackageReference Include="xunit" Version="2.4.1" />
    <PackageReference Include="xunit.runner.visualstudio" Version="2.4.3">
      <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
      <PrivateAssets>all</PrivateAssets>
    </PackageReference>
    <PackageReference Include="coverlet.collector" Version="3.1.2">
      <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
      <PrivateAssets>all</PrivateAssets>
    </PackageReference>
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="..\\fmp-{{org_lower}}-{{module_lower}}-service-grpc\\fmp-{{org_lower}}-{{module_lower}}-service-grpc.csproj" />
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
    project_name = "fmp-{}-{}-service-grpc_Test".format(
        org_name.lower(), module_name.lower()
    )
    writer.writeVS2022Project(_outputdir, project_name, contents, False)

    # 生成Usings
    Usings.generate(_options, os.path.join(_outputdir, project_name))
    # 生成TestServerCallContext
    TestServerCallContext.generate(_options, os.path.join(_outputdir, project_name))
    # 生成UnitTestBase
    UnitTestBase.generate(_options, os.path.join(_outputdir, project_name))
    # 生成UnitTest
    UnitTest.generate(_options, os.path.join(_outputdir, project_name))
    # 生成IntegrationTestBase
    IntegrationTestBase.generate(_options, os.path.join(_outputdir, project_name))
    # 生成IntegrationTest
    IntegrationTest.generate(_options, os.path.join(_outputdir, project_name))
    # 生成DatabaseOptions
    DatabaseOptions.generate(_options, os.path.join(_outputdir, project_name))
    # 生成TestFixtureBase
    TestFixtureBase.generate(_options, os.path.join(_outputdir, project_name))
    # 生成TestFixture
    TestFixture.generate(_options, os.path.join(_outputdir, project_name))
