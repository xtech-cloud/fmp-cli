import os
from typing import Dict, List, Tuple
from generator.template.utility import writer

template = """
//*************************************************************************************
//   !!! Generated by the fmp-cli.  DO NOT EDIT!
//*************************************************************************************

using {{org}}.FMP.MOD.{{module}}.LIB.Proto;
using {{org}}.FMP.MOD.{{module}}.LIB.Bridge;

namespace {{org}}.FMP.MOD.{{module}}.LIB.MVCS
{
{{message_blocks}}
}
"""

template_message = """
    public class {{message}}DTO : IDTO
    {
        public {{message}}DTO({{message}} _value)
        {
            Value = _value;    
        }
        public readonly {{message}} Value;
    }
"""


def generate(_options, _outputdir: str):
    org_name = _options["org_name"]
    module_name = _options["module_name"]
    messages = _options["messages"]
    message_blocks = ""
    # 遍历所有消息
    for message_name in messages.keys():
        # 遍历所有字段
        for field in messages[message_name]:
            # 字段名
            field_name = field[0]
            # 字段类型
            field_type = field[1]
        message_block = template_message.replace("{{message}}", message_name)
        message_blocks = message_blocks + message_block + "\n\n"

    # 生成项目文件
    contents = (
        template.replace("{{org}}", org_name)
        .replace("{{module}}", module_name)
        .replace("{{message_blocks}}", message_blocks)
    )
    contents = contents.replace("{{version}}", _options["version"])
    filepath = os.path.join(_outputdir, "ProtoDTO.cs")
    writer.write(filepath, contents, True)
