import os
import uuid
from generator.template.utility import writer

template = """
using System;
using LibMVCS = XTC.FMP.LIB.MVCS;
using {{org_name}}.FMP.MOD.{{module_name}}.LIB.MVCS;
using {{org_name}}.FMP.MOD.{{module_name}}.LIB.Bridge;

namespace {{org_name}}.FMP.MOD.{{module_name}}.LIB.Unity
{
    public class {{service}}UiBridge : {{service}}UiBridgeBase
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

    services = _options["services"]

    for service in services.keys():
        contents = template
        contents = contents.replace("{{org_name}}", _options["org_name"])
        contents = contents.replace("{{module_name}}", _options["module_name"])
        contents = contents.replace("{{service}}", service)
        output_path = os.path.join(output_dir, "{}UiBridge.cs".format(service))
        writer.write(output_path, contents, False)
