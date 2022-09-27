import os
from typing import Dict, List, Tuple
from generator.template.utility import writer

template = """
namespace {{org}}.FMP.MOD.{{module}}.LIB.MVCS
{
    public class Permissions
    {
        public const string Create = "/{{org}}/{{module}}/Create";
        public const string Update = "/{{org}}/{{module}}/Update";
        public const string Retrieve = "/{{org}}/{{module}}/Retrieve";
        public const string Delete = "/{{org}}/{{module}}/Delete";
    }
}
"""

def generate(_options, _outputdir: str):
    org_name = _options["org_name"]
    module_name = _options["module_name"]
    # 生成项目文件
    contents = (
        template.replace("{{org}}", org_name)
        .replace("{{module}}", module_name)
    )
    filepath = os.path.join(_outputdir, "Permissions.cs")
    writer.write(filepath, contents, False)
