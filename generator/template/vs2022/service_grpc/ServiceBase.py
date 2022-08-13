import os
from typing import Dict, List, Tuple
from generator.template.utility import writer

template = """
//*************************************************************************************
//   !!! Generated by the fmp-cli {{version}}.  DO NOT EDIT!
//*************************************************************************************

using Grpc.Core;
using System.Threading.Tasks;
using {{org}}.FMP.MOD.{{module}}.LIB.Proto;

namespace {{org}}.FMP.MOD.{{module}}.App.Service
{
    /// <summary>
    /// {{service}}基类
    /// </summary>
    public class {{service}}ServiceBase : LIB.Proto.{{service}}.{{service}}Base
    {
    
{{method_blocks}}
    }
}

"""

template_method = """
        public override async Task<{{response}}> {{rpc}}({{request}} _request, ServerCallContext _context)
        {
            return await Task.Run(() => new {{response}} {
                    Status = new LIB.Proto.Status() { Code = -1, Message = "Not Implemented" },
            });
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
                .replace("{{response}}", rpc_map[1])
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
        filepath = os.path.join(_outputdir, "{}ServiceBase.cs".format(service))
        writer.write(filepath, contents, True)
