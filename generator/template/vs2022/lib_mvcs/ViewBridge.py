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


def generate(
    _orgname: str,
    _modulename: str,
    _outputdir: str,
    _enums: List[str],
    _services: Dict[str, Dict[str, Tuple]],
    _messages: Dict[str, List[Tuple]],
):
    for service in _services.keys():
        contents = (
            template.replace("{{org}}", _orgname)
            .replace("{{module}}", _modulename)
            .replace("{{service}}", service)
        )
        filepath = os.path.join(_outputdir, "{}ViewBridge.cs".format(service))
        writer.write(filepath, contents, False)
