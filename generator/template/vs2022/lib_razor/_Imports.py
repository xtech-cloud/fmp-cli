import os
from typing import Dict, List, Tuple
from generator.template.utility import writer

template = """
@using AntDesign
"""


def generate(_orgname: str, _modulename: str, _outputdir: str):
    contents = (
        template.replace("{{org}}", _orgname)
        .replace("{{module}}", _modulename)
    )
    filepath = os.path.join(_outputdir, "_Imports.razor")
    writer.write(filepath, contents, False)
