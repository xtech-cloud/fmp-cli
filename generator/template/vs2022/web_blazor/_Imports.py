import os
from typing import Dict, List, Tuple
from generator.template.utility import writer

template = """
@using AntDesign
@using AntDesign.Charts
@using AntDesign.ProLayout
@using System.Net.Http
@using System.Net.Http.Json
@using Microsoft.AspNetCore.Components.Forms
@using Microsoft.AspNetCore.Components.Routing
@using Microsoft.AspNetCore.Components.Web
@using Microsoft.AspNetCore.Components.WebAssembly.Http
"""


def generate(_orgname: str, _modulename: str, _outputdir: str):
    contents = (
        template.replace("{{org}}", _orgname)
        .replace("{{module}}", _modulename)
    )
    filepath = os.path.join(_outputdir, "_Imports.razor")
    writer.write(filepath, contents, False)
