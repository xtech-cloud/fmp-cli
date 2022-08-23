import os
from typing import Dict, List, Tuple
from generator.template.utility import writer

template = """
{
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning"
    }
  },
  "AllowedHosts": "*",
  "Kestrel": {
    "EndpointDefaults": {
      "Protocols": "Http2"
    },
    "Endpoints": {
      "Http": {
        "Url": "http://localhost:18000"
      },
      "Https": {
        "Url": "https://localhost:19000"
      }
    }
  },
{{db_blocks}}
}
"""

template_development = """
{
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning"
    }
  },
{{db_blocks}}
}

"""

template_driver_mongodb = """
  "Database": {
    "Driver": "MongoDB",
    "ConnectionString": "mongodb://root:mongo%40XTC@localhost:27017",
    "DatabaseName": "{{org}}_FMP_{{module}}"
  }
"""

template_driver_none = """
  "Database": {
    "Driver": "None"
  }
"""


def generate(_options, _outputdir: str):
    org_name = _options["org_name"]
    module_name = _options["module_name"]
    database_driver = _options["database_driver"]

    contents = template
    if "mongodb" == database_driver:
        contents = contents.replace("{{db_blocks}}", template_driver_mongodb)
    else:
        contents = contents.replace("{{db_blocks}}", template_driver_none)
    contents = contents.replace("{{module}}", module_name)
    contents = contents.replace("{{org}}", org_name)
    filepath = os.path.join(_outputdir, "appsettings.json")
    writer.write(filepath, contents, False)

    contents = template_development
    if "mongodb" == database_driver:
        contents = contents.replace("{{db_blocks}}", template_driver_mongodb)
    else:
        contents = contents.replace("{{db_blocks}}", template_driver_none)
    contents = contents.replace("{{module}}", module_name)
    filepath = os.path.join(_outputdir, "appsettings.Development.json")
    writer.write(filepath, contents, False)
