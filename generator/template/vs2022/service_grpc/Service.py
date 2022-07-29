import os
from typing import Dict, List, Tuple
from generator.template.utility import writer

template = """
using Grpc.Core;
using System.Threading.Tasks;
using {{org}}.FMP.MOD.{{module}}.LIB.Proto;

namespace {{org}}.FMP.MOD.{{module}}.App.Service
{
    public class {{service}}Service : {{service}}ServiceBase
    {
        // 解开以下代码的注释，可支持数据库操作
        /*
        private readonly YourDAO yourDAO_;

         /// <summary>
        /// 构造函数
        /// </summary>
        /// <remarks>
        /// 支持多个参数，均为自动注入，注入点位于MyProgram.PreBuild
        /// </remarks>
        /// <param name="_yourDAO">自动注入的数据操作对象</param>
        public {{service}}Service(YourDAO _yourDAO)
        {
            yourDAO_ = _yourDAO;
        }
        */
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
        filepath = os.path.join(_outputdir, "{}Service.cs".format(service))
        writer.write(filepath, contents, False)
