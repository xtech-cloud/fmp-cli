import os
from typing import Dict, List, Tuple
from generator.template.utility import writer

template = """
//*************************************************************************************
//   !!! Generated by the fmp-cli {{version}}.  DO NOT EDIT!
//*************************************************************************************

using System.Threading.Tasks;
using XTC.FMP.LIB.MVCS;
using {{org}}.FMP.MOD.{{module}}.LIB.Bridge;

namespace {{org}}.FMP.MOD.{{module}}.LIB.MVCS
{
    /// <summary>
    /// {{service}}的视图桥接层基类（协议部分）
    /// 处理UI的事件
    /// </summary>
    public class {{service}}ViewBridgeBase : I{{service}}ViewBridge
    {

        /// <summary>
        /// 直系服务层
        /// </summary>
        public {{service}}Service? service { get; set; }

{{method_blocks}}

    }
}
"""

template_method = """
        /// <summary>
        /// 处理{{rpc}}的提交
        /// </summary>
        /// <param name="_dto">{{request}}的数据传输对象</param>
        /// <returns>错误</returns>
        public async Task<Error> On{{rpc}}Submit(IDTO _dto)
        {
            {{request}}DTO? dto = _dto as {{request}}DTO;
            if(null == service)
            {
                return Error.NewNullErr("service is null");
            }
            return await service.Call{{rpc}}(dto?.Value);
        }
"""


def generate(_options, _outputdir: str):
    org_name = _options["org_name"]
    module_name = _options["module_name"]
    services = _options["services"]
    for service in services.keys():
        method_blocks = ""
        for rpc_name in services[service].keys():
            rpc_map = services[service][rpc_name]
            method_block = (
                template_method.replace("{{service}}", service)
                .replace("{{rpc}}", rpc_name)
                .replace("{{request}}", rpc_map[0])
            )
            method_blocks = method_blocks + method_block
        contents = (
            template.replace("{{org}}", org_name)
            .replace("{{module}}", module_name)
            .replace("{{service}}", service)
            .replace("{{method_blocks}}", method_blocks)
        )
        contents = contents.replace("{{version}}", _options["version"])
        filepath = os.path.join(_outputdir, "{}ViewBridgeBase.cs".format(service))
        writer.write(filepath, contents, True)
