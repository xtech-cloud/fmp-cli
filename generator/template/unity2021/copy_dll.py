template = r"""
REM !!! Generated by the fmp-cli {{version}}.  DO NOT EDIT!

md {{module_name}}\Assets\3rd\fmp-{{org_name_lower}}-{{module_name_lower}}

cd ..\vs2022
dotnet build -c Release

copy fmp-{{org_name_lower}}-{{module_name_lower}}-lib-mvcs\bin\Release\netstandard2.1\*.dll ..\unity2021\{{module_name}}\Assets\3rd\fmp-{{org_name_lower}}-{{module_name+lower}}\
"""

def generate(_options, _outputdir: str):
    output_dir = os.path.join(_outputdir, "Packages")
    os.makedirs(output_dir, exist_ok=True)

    contents = template
    contents = contents.replace("{{version}}", _options["version"])
    contents = contents.replace("{{org_name}}", _options["org_name"])
    contents = contents.replace("{{module_name}}", _options["module_name"])
    contents = contents.replace("{{org_name_lower}}", _options["org_name"].lower())
    contents = contents.replace("{{module_name_lower}}", _options["module_name"].lower())
    output_path = os.path.join(output_dir, "copy-dll.bat")
    writer.write(output_path, contents, False)
