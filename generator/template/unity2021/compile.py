import os
from generator.template.utility import writer

template = r"""
@echo off

REM !!! Generated by the fmp-cli {{version}}.  DO NOT EDIT!

for /F %%i in ('git tag --contains') do ( set VERSION=%%i)
IF "%VERSION%" ==""  (
    echo [31m tag is required! [0m
    pause
    EXIT
)

set WORK_DIR=%cd%
IF NOT EXIST .UNITY_HOME.env (
    echo [31m .UNITY_HOME.env is required ! [0m
    pause
    EXIT
)

set /P UNITY_HOME=<.UNITY_HOME.env
IF NOT EXIST %UNITY_HOME% (
    echo [31m %UNITY_HOME% not found ! [0m
    pause
    EXIT
)

mkdir _build_
mkdir _dist_
DEL /Q/S _dist_\*.dll
copy Unity.csproj.keep _build_\Unity.csproj
xcopy /Q/S/Y {{module_name}}\Assets\Scripts\Module _build_\Module\
cd _build_
powershell -Command "(gc Unity.csproj) -replace '{{UNITY_HOME}}', '%UNITY_HOME%' | Out-File Unity.csproj"
powershell -Command "(gc Unity.csproj) -replace '{{WORK_DIR}}', '%WORK_DIR%' | Out-File Unity.csproj"
powershell -Command "(gc Unity.csproj) -replace '{{VERSION}}', '%VERSION%' | Out-File Unity.csproj"

dotnet build -c=Release
cd ..
DEL /Q/S _build_\bin\Release\netstandard2.1\Unity*
move _build_\bin\Release\netstandard2.1\*.Unity.dll .\_dist_\
RD /Q/S _build_
pause
"""

def generate(_options, _outputdir: str):
    output_dir = _outputdir

    contents = template
    contents = contents.replace("{{version}}", _options["version"])
    contents = contents.replace("{{module_name}}", _options["module_name"])
    output_path = os.path.join(output_dir, "compile.bat")
    writer.write(output_path, contents, True)
