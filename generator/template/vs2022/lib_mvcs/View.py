import os
from typing import Dict, List, Tuple
from generator.template.utility import writer

template = """
using XTC.FMP.LIB.MVCS;

namespace {{org}}.FMP.MOD.{{module}}.LIB.MVCS
{
    /// <summary>
    /// {{service}}视图层
    /// </summary>
    public class {{service}}View : {{service}}BaseView
    {
        /// <summary>
        /// 完整名称
        /// </summary>
        public const string NAME = "{{org}}.FMP.MOD.{{module}}.LIB.MVCS.{{service}}View";

        /// <summary>
        /// 带uid参数的构造函数
        /// </summary>
        /// <param name="_uid">实例化后的唯一识别码</param>
        public {{service}}View(string _uid) : base(_uid)
        {
        }
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
        filepath = os.path.join(_outputdir, "{}View.cs".format(service))
        writer.write(filepath, contents, False)
