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
      "Protocols": "Http1"
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


def generate(
    _orgname: str,
    _modulename: str,
    _outputdir: str,
    _databasedriver: str,
):
    contents = template
    if "mongodb" == _databasedriver:
        contents = contents.replace("{{db_blocks}}", template_driver_mongodb)
    else:
        contents = contents.replace("{{db_blocks}}", template_driver_none)
    contents = contents.replace("{{module}}", _modulename)
    contents = contents.replace("{{org}}", _orgname)
    filepath = os.path.join(_outputdir, "appsettings.json")
    writer.write(filepath, contents, False)


    contents = template_development
    if "mongodb" == _databasedriver:
        contents = contents.replace("{{db_blocks}}", template_driver_mongodb)
    else:
        contents = contents.replace("{{db_blocks}}", template_driver_none)
    contents = contents.replace("{{module}}", _modulename)
    filepath = os.path.join(_outputdir, "appsettings.Development.json")
    writer.write(filepath, contents, False)
