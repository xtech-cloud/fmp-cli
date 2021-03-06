import os
from typing import Dict, List, Tuple
from generator.template.utility import writer

template = """
//*************************************************************************************
//   !!! Generated by the fmp-cli.  DO NOT EDIT!
//*************************************************************************************

using XTC.FMP.LIB.MVCS;
using {{org}}.FMP.MOD.{{module}}.LIB.Proto;

namespace {{org}}.FMP.MOD.{{module}}.LIB.MVCS
{
    /// <summary>
    /// {{service}}数据层基类
    /// </summary>
    public class {{service}}BaseModel : Model
    {
        /// <summary>
        /// 带uid参数的构造函数
        /// </summary>
        /// <param name="_uid">实例化后的唯一识别码</param>
        public {{service}}BaseModel(string _uid) : base(_uid)
        {

        }

{{method_blocks}}

        /// <summary>
        /// 获取直系控制层
        /// </summary>
        /// <returns>控制层</returns>
        protected {{service}}Controller? getController()
        {
            if(null == controller_)
                controller_ = findController({{service}}Controller.NAME) as {{service}}Controller;
            return controller_;
        }

        /// <summary>
        /// 直系控制层
        /// </summary>
        private {{service}}Controller? controller_;
    }
}


"""

template_method = """
        /// <summary>
        /// 更新{{rpc}}的数据
        /// </summary>
        /// <param name="_response">{{rpc}}的回复</param>
        public void UpdateProto{{rpc}}({{response}} _response)
        {
            getController()?.UpdateProto{{rpc}}(status_ as {{service}}Model.{{service}}Status, _response);
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
            )
            method_blocks = method_blocks + method_block
        contents = (
            template.replace("{{org}}", _orgname)
            .replace("{{module}}", _modulename)
            .replace("{{service}}", service)
            .replace("{{method_blocks}}", method_blocks)
        )
        filepath = os.path.join(_outputdir, "{}BaseModel.cs".format(service))
        writer.write(filepath, contents, True)
