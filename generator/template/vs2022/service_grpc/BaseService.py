import os
from typing import Dict, List, Tuple
from generator.template.utility import writer

template = """
//*************************************************************************************
//   !!! Generated by the fmp-cli.  DO NOT EDIT!
//*************************************************************************************

using Grpc.Core;
using System.Threading.Tasks;
using {{org}}.FMP.MOD.{{module}}.LIB.Proto;

namespace {{org}}.FMP.MOD.{{module}}.App.Service
{
    /// <summary>
    /// {{service}}基类
    /// </summary>
    public class {{service}}BaseService : {{service}}.{{service}}Base
    {
{{method_blocks}}
    }
}

"""

template_method = """
        public override Task<{{response}}> {{rpc}}({{request}} _request, ServerCallContext _context)
        {
            return Task.FromResult(new {{response}}
            {
                Status = new LIB.Proto.Status() { Code=-1, Message="Not Implemented"},
            });
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
        method_blocks = ""
        for rpc_name in _services[service].keys():
            rpc_map = _services[service][rpc_name]
            method_block = (
                template_method.replace("{{service}}", service)
                .replace("{{rpc}}", rpc_name)
                .replace("{{response}}", rpc_map[1])
                .replace("{{request}}", rpc_map[0])
            )
            method_blocks = method_blocks + method_block
        contents = (
            template.replace("{{org}}", _orgname)
            .replace("{{module}}", _modulename)
            .replace("{{service}}", service)
            .replace("{{method_blocks}}", method_blocks)
        )
        filepath = os.path.join(_outputdir, "{}BaseService.cs".format(service))
        writer.write(filepath, contents, True)
