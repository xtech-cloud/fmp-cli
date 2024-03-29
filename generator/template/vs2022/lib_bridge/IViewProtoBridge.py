import os
from typing import Dict, List, Tuple
from generator.template.utility import writer

template = """
//*************************************************************************************
//   !!! Generated by the fmp-cli {{version}}.  DO NOT EDIT!
//*************************************************************************************

using System.Threading;
using System.Threading.Tasks;
using XTC.FMP.LIB.MVCS;

namespace {{org}}.FMP.MOD.{{module}}.LIB.Bridge
{
    /// <summary>
    /// {{service}}的视图桥接层（协议部分）
    /// 处理UI的事件
    /// </summary>
    public interface I{{service}}ViewProtoBridge : View.Facade.Bridge
    {
{{rpc_blocks}}
    }
}

"""

template_method = """
        /// <summary>
        /// 处理{{rpc}}的提交
        /// </summary>
        Task<Error> On{{rpc}}Submit(IDTO _dto, object? _context);
"""


def generate(_options, _outputdir: str):
    org_name = _options["org_name"]
    module_name = _options["module_name"]
    services = _options["services"]

    for service in services.keys():
        rpc_block = ""
        for rpc_name in services[service].keys():
            rpc = template_method.replace("{{rpc}}", rpc_name)
            rpc_block = rpc_block + str.format("{}\n", rpc)
        contents = template
        contents = contents.replace("{{org}}", org_name)
        contents = contents.replace("{{module}}", module_name)
        contents = contents.replace("{{service}}", service)
        contents = contents.replace("{{rpc_blocks}}", rpc_block)
        contents = contents.replace("{{version}}", _options["version"])
        filepath = os.path.join(_outputdir, "I{}ViewProtoBridge.cs".format(service))
        writer.write(filepath, contents, True)
