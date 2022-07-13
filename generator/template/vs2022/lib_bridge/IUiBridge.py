import os
from typing import Dict, List, Tuple
from generator.template.utility import writer

template = """
namespace {{org}}.FMP.MOD.{{module}}.LIB.Bridge
{
    /// <summary>
    /// {{service}}的UI桥接层（非协议部分）
    /// 刷新从视图收到的数据
    /// </summary>
    public interface I{{service}}UiBridge : I{{service}}UiProtoBridge
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
        filepath = os.path.join(_outputdir, "I{}UiBridge.cs".format(service))
        writer.write(filepath, contents, False)
