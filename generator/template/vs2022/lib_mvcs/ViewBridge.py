import os
from typing import Dict, List, Tuple
from generator.template.utility import writer

template = """
using XTC.FMP.LIB.MVCS;

namespace {{org}}.FMP.MOD.{{module}}.LIB.MVCS
{
    /// <summary>
    /// {{service}}视图桥接层
    /// </summary>
    public class {{service}}ViewBridge : {{service}}ViewBridgeBase
    {
        
    }
}
"""


def generate(_options, _outputdir: str):
    org_name = _options["org_name"]
    module_name = _options["module_name"]
    services = _options["services"]
    for service in services.keys():
        contents = (
            template.replace("{{org}}", org_name)
            .replace("{{module}}", module_name)
            .replace("{{service}}", service)
        )
        filepath = os.path.join(_outputdir, "{}ViewBridge.cs".format(service))
        writer.write(filepath, contents, False)
