import os
from typing import Dict, List, Tuple
from generator.template.utility import writer

template = """
{
  "ProSettings": {
    "NavTheme": "dark",
    "Layout": "side",
    "ContentWidth": "Fluid",
    "FixedHeader": false,
    "FixSiderbar": true,
    "Title": "Ant Design Pro",
    "PrimaryColor": "daybreak",
    "ColorWeak": false,
    "SplitMenus": false,
    "HeaderRender": true,
    "FooterRender": true,
    "MenuRender": true,
    "MenuHeaderRender": true,
    "HeaderHeight": 48
  }
}
"""

def generate(_options, _outputdir: str):
    sub_dir = os.path.join(_outputdir, "wwwroot")
    os.makedirs(sub_dir, exist_ok=True)

    filepath = os.path.join(sub_dir, "appsettings.json")
    writer.write(filepath, template, False)
