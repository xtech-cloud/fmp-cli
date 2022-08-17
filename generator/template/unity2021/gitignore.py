import os
from generator.template.utility import writer

template = r"""
/_dist_/
/_build_/
/{{module_name}}/Assets/TextMesh Pro/
/{{module_name}}/Assets/TextMesh Pro.meta
/{{module_name}}/Assets/Plugins/
/{{module_name}}/Assets/Plugins.meta
/{{module_name}}/Assets/3rd/
/{{module_name}}/Assets/3rd.meta
/{{module_name}}/Library/
/{{module_name}}/obj/
/{{module_name}}/Logs/
/{{module_name}}/Temp/
/{{module_name}}/UserSettings/
/{{module_name}}/*.sln
/{{module_name}}/*.csproj
/{{module_name}}/.vsconfig
/.UNITY_HOME.env
"""

def generate(_options, _outputdir: str):
    output_dir = _outputdir

    contents = template
    contents = contents.replace("{{module_name}}", _options["module_name"])
    output_path = os.path.join(output_dir, ".gitignore")
    writer.write(output_path, contents, False)
