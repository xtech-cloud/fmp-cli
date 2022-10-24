import os
from typing import Dict, List, Tuple
from generator.template.utility import writer

template = """
using {{org}}.FMP.MOD.{{module}}.App.Service;
public static class MyProgram
{
    public static void PreBuild(WebApplicationBuilder? _builder)
    {
        _builder?.Services.AddSingleton<SingletonServices>();
    }

    public static void PreRun(WebApplication? _app)
    {
    }
}
"""


def generate(_options, _outputdir: str):
    org_name = _options["org_name"]
    module_name = _options["module_name"]

    contents = template.replace("{{org}}", org_name).replace("{{module}}", module_name)
    filepath = os.path.join(_outputdir, "MyProgram.cs")
    writer.write(filepath, contents, False)
