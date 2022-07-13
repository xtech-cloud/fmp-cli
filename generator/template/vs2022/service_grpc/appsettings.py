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
  }
}
"""

template_development = """
{
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning"
    }
  }
}

"""

def generate(
    _orgname: str,
    _modulename: str,
    _outputdir: str,
):
    filepath = os.path.join(_outputdir, "appsettings.json")
    writer.write(filepath, template, False)
    filepath = os.path.join(_outputdir, "appsettings.Development.json")
    writer.write(filepath, template_development, False)
