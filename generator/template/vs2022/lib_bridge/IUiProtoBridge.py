import os
from typing import Dict, List, Tuple
from generator.template.utility import writer

template = """
//*************************************************************************************
//   !!! Generated by the fmp-cli.  DO NOT EDIT!
//*************************************************************************************

using XTC.FMP.LIB.MVCS;

namespace {{org}}.FMP.MOD.{{module}}.LIB.Bridge
{
    /// <summary>
    /// {{service}}的UI桥接层（协议部分）
    /// 刷新从视图收到的数据
    /// </summary>
    public interface I{{service}}UiProtoBridge : View.Facade.Bridge
    {
        /// <summary>
        /// 全局警告
        /// </summary>
        /// <param name="_code">错误码</param>
        /// <param name="_code">错误信息</param>
        void Alert(string _code, string _message);
{{rpc_blocks}}
    }
}

"""

template_method = """
        /// <summary>
        /// 刷新{{rpc}}的数据
        /// </summary>
        void Refresh{{rpc}}(IDTO _dto);
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
        rpc_block = ""
        for rpc_name in _services[service].keys():
            rpc = template_method.replace("{{rpc}}", rpc_name)
            rpc_block = rpc_block + str.format("{}\n", rpc)
        contents = template
        contents = contents.replace("{{org}}", _orgname)
        contents = contents.replace("{{module}}", _modulename)
        contents = contents.replace("{{service}}", service)
        contents = contents.replace("{{rpc_blocks}}", rpc_block)
        filepath = os.path.join(_outputdir, "I{}UiProtoBridge.cs".format(service))
        writer.write(filepath, contents, True)