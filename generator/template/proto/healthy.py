import os
from generator.template.utility import writer

template = """
syntax = "proto3";
import "shared.proto";

option csharp_namespace = "{{org}}.FMP.MOD.{{module}}.LIB.Proto";
package {{org_lower}}.fmp.{{module_lower}};

// 健康
service Healthy {
    // 回显
    rpc Echo(HealthyEchoRequest) returns (HealthyEchoResponse) {}
}

// 回显的请求
message HealthyEchoRequest {
    string msg = 1;
}

// 回显的回复
message HealthyEchoResponse {
    Status status = 1;
    string msg = 2;
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
    filepath = os.path.join(_outputdir, "healthy.proto")
    writer.write(filepath, contents, False)
