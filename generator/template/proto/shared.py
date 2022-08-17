import os
from generator.template.utility import writer

template = """
syntax = "proto3";

option csharp_namespace = "{{org}}.FMP.MOD.{{module}}.LIB.Proto";
package {{org_lower}}.fmp.{{module_lower}};

// 状态
message Status
{
    int32 code = 1;  // 状态码
    string message = 2;  // 状态信息
}

// 空白请求
message BlankRequest
{
}

// 空白回复
message BlankResponse
{
    Status status = 1;  // 状态
}

// 作用域的请求
message ScopeRequest
{
    string scope = 1;  // 作用域
}

// 作用域的回复
message ScopeResponse
{
    Status status = 1;  // 状态
    string scope = 2;  // 作用域
}

// UUID的请求
message UuidRequest
{
    string uuid = 1;  // 唯一识别码
}

// UUID的回复
message UuidResponse
{
    Status status = 1;  // 状态
    string uuid = 2;  // 唯一识别码
}
"""


def generate(_options, _outputdir: str):
    org_name = _options["org_name"]
    module_name = _options["module_name"]

    contents = template
    contents = contents.replace("{{org}}", org_name)
    contents = contents.replace("{{module}}", module_name)
    contents = contents.replace("{{org_lower}}", org_name.lower())
    contents = contents.replace("{{module_lower}}", module_name.lower())
    filepath = os.path.join(_outputdir, "shared.proto")
    writer.write(filepath, contents, False)
