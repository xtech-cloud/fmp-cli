import os
from typing import Dict, List, Tuple
from generator.template.utility import writer

template = """
namespace {{org}}.FMP.MOD.{{module}}.LIB.MVCS
{
    public class Permissions
    {
{{blocks}}
    }
}
"""

template_blocks = """
        public const string {{service}}Create = "/{{org}}/{{module}}/{{service}}/Create";
        public const string {{service}}Update = "/{{org}}/{{module}}/{{service}}/Update";
        public const string {{service}}Retrieve = "/{{org}}/{{module}}/{{service}}/Retrieve";
        public const string {{service}}Delete = "/{{org}}/{{module}}/{{service}}/Delete";
"""


def generate(_options, _outputdir: str):
    org_name = _options["org_name"]
    module_name = _options["module_name"]
    services = _options["services"]
    blocks = ""
    for service in services.keys():
        block = template_blocks.replace("{{org}}", org_name).replace("{{module}}", module_name).replace("{{service}}", service)
        blocks = blocks + block
    # 生成项目文件
    contents = (
        template.replace("{{org}}", org_name)
        .replace("{{module}}", module_name)
        .replace("{{blocks}}", blocks)
    )
    filepath = os.path.join(_outputdir, "Permissions.cs")
    writer.write(filepath, contents, False)
