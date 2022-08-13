import os
from typing import Dict, List, Tuple
from generator.template.utility import writer

template = """
namespace {{org}}.FMP.MOD.{{module}}.LIB.Bridge
{
    /// <summary>
    /// {{service}}的视图桥接层（非协议部分）
    /// 处理UI的事件
    /// </summary>
    public interface I{{service}}ViewBridge : I{{service}}ViewProtoBridge
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
        filepath = os.path.join(_outputdir, "I{}ViewBridge.cs".format(service))
        writer.write(filepath, contents, False)
