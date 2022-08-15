import os
import uuid
from generator.template.utility import writer

template = """
Microsoft Visual Studio Solution File, Format Version 12.00
# Visual Studio Version 17
VisualStudioVersion = 17.2.32526.322
MinimumVisualStudioVersion = 10.0.40219.1
Project("{{{guid_sln}}}") = "fmp-{{org.lower}}-{{module.lower}}-lib-mvcs", "fmp-{{org.lower}}-{{module.lower}}-lib-mvcs\\fmp-{{org.lower}}-{{module.lower}}-lib-mvcs.csproj", "{{{guid_lib_mvcs}}}"
EndProject
Project("{{{guid_sln}}}") = "fmp-{{org.lower}}-{{module.lower}}-lib-mvcs_Test", "fmp-{{org.lower}}-{{module.lower}}-lib-mvcs_Test\\fmp-{{org.lower}}-{{module.lower}}-lib-mvcs_Test.csproj", "{{{guid_lib_mvcs_Test}}}"
EndProject
Project("{{{guid_sln}}}") = "fmp-{{org.lower}}-{{module.lower}}-lib-proto", "fmp-{{org.lower}}-{{module.lower}}-lib-proto\\fmp-{{org.lower}}-{{module.lower}}-lib-proto.csproj", "{{{guid_lib_proto}}}"
EndProject
Project("{{{guid_sln}}}") = "fmp-{{org.lower}}-{{module.lower}}-lib-bridge", "fmp-{{org.lower}}-{{module.lower}}-lib-bridge\\fmp-{{org.lower}}-{{module.lower}}-lib-bridge.csproj", "{{{guid_lib_bridge}}}"
EndProject
Project("{{{guid_sln}}}") = "fmp-{{org.lower}}-{{module.lower}}-lib-razor", "fmp-{{org.lower}}-{{module.lower}}-lib-razor\\fmp-{{org.lower}}-{{module.lower}}-lib-razor.csproj", "{{{guid_lib_razor}}}"
EndProject
Project("{{{guid_sln}}}") = "fmp-{{org.lower}}-{{module.lower}}-service-grpc", "fmp-{{org.lower}}-{{module.lower}}-service-grpc\\fmp-{{org.lower}}-{{module.lower}}-service-grpc.csproj", "{{{guid_service_grpc}}}"
EndProject
Project("{{{guid_sln}}}") = "fmp-{{org.lower}}-{{module.lower}}-service-grpc_Test", "fmp-{{org.lower}}-{{module.lower}}-service-grpc_Test\\fmp-{{org.lower}}-{{module.lower}}-service-grpc_Test.csproj", "{{{guid_service_grpc_Test}}}"
EndProject
Project("{{{guid_sln}}}") = "fmp-{{org.lower}}-{{module.lower}}-web-blazor", "fmp-{{org.lower}}-{{module.lower}}-web-blazor\\fmp-{{org.lower}}-{{module.lower}}-web-blazor.csproj", "{{{guid_web_blazor}}}"
EndProject
Global
	GlobalSection(SolutionConfigurationPlatforms) = preSolution
		Debug|Any CPU = Debug|Any CPU
		Release|Any CPU = Release|Any CPU
	EndGlobalSection
	GlobalSection(ProjectConfigurationPlatforms) = postSolution
                {{{guid_lib_mvcs}}}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{{{guid_lib_mvcs}}}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{{{guid_lib_mvcs}}}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{{{guid_lib_mvcs}}}.Release|Any CPU.Build.0 = Release|Any CPU
		{{{guid_lib_mvcs_Test}}}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{{{guid_lib_mvcs_Test}}}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{{{guid_lib_mvcs_Test}}}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{{{guid_lib_mvcs_Test}}}.Release|Any CPU.Build.0 = Release|Any CPU
		{{{guid_lib_proto}}}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{{{guid_lib_proto}}}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{{{guid_lib_proto}}}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{{{guid_lib_proto}}}.Release|Any CPU.Build.0 = Release|Any CPU
		{{{guid_service_grpc}}}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{{{guid_service_grpc}}}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{{{guid_service_grpc}}}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{{{guid_service_grpc}}}.Release|Any CPU.Build.0 = Release|Any CPU
		{{{guid_lib_bridge}}}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{{{guid_lib_bridge}}}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{{{guid_lib_bridge}}}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{{{guid_lib_bridge}}}.Release|Any CPU.Build.0 = Release|Any CPU
		{{{guid_web_blazor}}}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{{{guid_web_blazor}}}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{{{guid_web_blazor}}}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{{{guid_web_blazor}}}.Release|Any CPU.Build.0 = Release|Any CPU
		{{{guid_lib_razor}}}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{{{guid_lib_razor}}}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{{{guid_lib_razor}}}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{{{guid_lib_razor}}}.Release|Any CPU.Build.0 = Release|Any CPU
		{{{guid_service_grpc_Test}}}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{{{guid_service_grpc_Test}}}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{{{guid_service_grpc_Test}}}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{{{guid_service_grpc_Test}}}.Release|Any CPU.Build.0 = Release|Any CPU
	EndGlobalSection
	GlobalSection(SolutionProperties) = preSolution
		HideSolutionNode = FALSE
	EndGlobalSection
	GlobalSection(ExtensibilityGlobals) = postSolution
		SolutionGuid = {{{guid_sln}}}
	EndGlobalSection
EndGlobal
"""


def generate(_options, _outputdir: str):
    org_name = _options["org_name"]
    module_name = _options["module_name"]

    guid_sln = str(uuid.uuid4()).upper()
    guid_lib_proto = str(uuid.uuid4()).upper()
    guid_lib_bridge = str(uuid.uuid4()).upper()
    guid_lib_mvcs = str(uuid.uuid4()).upper()
    guid_lib_mvcs_Test = str(uuid.uuid4()).upper()
    guid_lib_razor = str(uuid.uuid4()).upper()
    guid_web_blazor = str(uuid.uuid4()).upper()
    guid_service_grpc = str(uuid.uuid4()).upper()
    guid_service_grpc_Test = str(uuid.uuid4()).upper()

    contents = (
        template.replace("{{org.lower}}", org_name.lower())
        .replace("{{module.lower}}", module_name.lower())
        .replace("{{guid_lib_proto}}", guid_lib_proto)
        .replace("{{guid_lib_bridge}}", guid_lib_bridge)
        .replace("{{guid_lib_mvcs}}", guid_lib_mvcs)
        .replace("{{guid_lib_mvcs_Test}}", guid_lib_mvcs_Test)
        .replace("{{guid_lib_razor}}", guid_lib_razor)
        .replace("{{guid_web_blazor}}", guid_web_blazor)
        .replace("{{guid_service_grpc}}", guid_service_grpc)
        .replace("{{guid_service_grpc_Test}}", guid_service_grpc_Test)
        .replace("{{guid_sln}}", guid_sln)
    )

    output_path = os.path.join(
        _outputdir, "fmp-{}-{}.sln".format(org_name.lower(), module_name.lower())
    )
    writer.write(output_path, contents, False)
