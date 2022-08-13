import os
from typing import Dict, List, Tuple
from generator.template.utility import writer

template = """
public static class MyProgram
{
    public static void PreBuild(WebApplicationBuilder? _builder)
    {
        //_builder?.Services.AddSingleton<YourDAO>();
    }

    public static void PreRun(WebApplication? _app)
    {
    }
}
"""

def generate(_options, _outputdir: str):
    contents = template
    filepath = os.path.join(_outputdir, "MyProgram.cs")
    writer.write(filepath, contents, False)
