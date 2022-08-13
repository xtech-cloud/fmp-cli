import os
from typing import Dict, List, Tuple
from generator.template.utility import writer

template = """
namespace {{org}}.FMP.MOD.{{module}}.LIB.MVCS
{
    /// <summary>
    /// {{service}}服务层
    /// </summary>
    public class {{service}}Service : {{service}}ServiceBase
    {
        /// <summary>
        /// 完整名称
        /// </summary>
        public const string NAME = "{{org}}.FMP.MOD.{{module}}.LIB.MVCS.{{service}}Service";

        /// <summary>
        /// 带uid参数的构造函数
        /// </summary>
        /// <param name="_uid">实例化后的唯一识别码</param>
        /// <param name="_gid">直系的组的ID</param>
        public {{service}}Service(string _uid, string _gid) : base(_uid, _gid) 
        {
        }
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
        filepath = os.path.join(_outputdir, "{}Service.cs".format(service))
        writer.write(filepath, contents, False)
