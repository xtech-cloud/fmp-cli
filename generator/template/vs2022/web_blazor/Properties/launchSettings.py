import os
from typing import Dict, List, Tuple
from generator.template.utility import writer

template = """
{
  "iisSettings": {
    "windowsAuthentication": false,
    "anonymousAuthentication": true,
    "iisExpress": {
      "applicationUrl": "http://localhost:53775/",
      "sslPort": 44358
    }
  },
  "profiles": {
    "IIS Express": {
      "commandName": "IISExpress",
      "launchBrowser": true,
      "inspectUri": "{wsProtocol}://{url.hostname}:{url.port}/_framework/debug/ws-proxy?browser={browserInspectUri}",
      "environmentVariables": {
        "ASPNETCORE_ENVIRONMENT": "Development"
      }
    },
    "fmp_{{org_lower}}_{{module_lower}}_web_blazor": {
      "commandName": "Project",
      "launchBrowser": true,
      "inspectUri": "{wsProtocol}://{url.hostname}:{url.port}/_framework/debug/ws-proxy?browser={browserInspectUri}",
      "environmentVariables": {
        "ASPNETCORE_ENVIRONMENT": "Development"
      },
      "applicationUrl": "https://localhost:7114;http://localhost:5114"
    }
  }
}
"""


def generate(_options, _outputdir: str):
    org_name = _options["org_name"]
    module_name = _options["module_name"]

    sub_dir = os.path.join(_outputdir, "Properties")
    os.makedirs(sub_dir, exist_ok=True)

    contents = template.replace("{{org_lower}}", org_name.lower()).replace(
        "{{module_lower}}", module_name.lower()
    )
    filepath = os.path.join(sub_dir, "launchSettings.json")
    writer.write(filepath, contents, False)
