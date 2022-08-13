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


def generate(_options, _outputdir: str):
    org_name = _options["org_name"]
    module_name = _options["module_name"]

    contents = (
        template.replace("{{org}}", org_name)
        .replace("{{module}}", module_name)
    )
    filepath = os.path.join(_outputdir, "_Imports.razor")
    writer.write(filepath, contents, False)
