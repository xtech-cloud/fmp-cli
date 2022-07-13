import os
from typing import Dict, List, Tuple
from generator.template.utility import writer

template = """
public static class MyProgram
{
    public static void PreBuild(WebApplicationBuilder? _builder)
    {
    }

    public static void PreRun(WebApplication? _app)
    {
    }
}
"""

def generate(
    _orgname: str,
    _modulename: str,
    _outputdir: str,
):
    contents = template
    filepath = os.path.join(_outputdir, "MyProgram.cs")
    writer.write(filepath, contents, False)
