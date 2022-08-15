import os
import uuid
from generator.template.utility import writer

template = """
namespace {{org_name}}.FMP.MOD.{{module_name}}.LIB.Unity
{
    public class MySubject : MySubjectBase
    {
    }
}
"""

def generate(_options, _outputdir: str):
    output_dir = os.path.join(_outputdir, "Assets")
    os.makedirs(output_dir, exist_ok=True)
    output_dir = os.path.join(output_dir, "Scripts")
    os.makedirs(output_dir, exist_ok=True)
    output_dir = os.path.join(output_dir, "Module")
    os.makedirs(output_dir, exist_ok=True)

    contents = template
    contents = contents.replace("{{org_name}}", _options["org_name"])
    contents = contents.replace("{{module_name}}", _options["module_name"])
    output_path = os.path.join(output_dir, "MySubject.cs")
    writer.write(output_path, contents, False)
