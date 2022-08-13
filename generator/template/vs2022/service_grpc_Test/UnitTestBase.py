import os
from typing import Dict, List, Tuple
from generator.template.utility import writer

template = """
//*************************************************************************************
//   !!! Generated by the fmp-cli {{version}}.  DO NOT EDIT!
//*************************************************************************************

public abstract class {{service}}UnitTestBase : IClassFixture<TestFixture>
{
    /// <summary>
    /// 测试上下文
    /// </summary>
    protected TestFixture fixture_ { get; set; }

    public {{service}}UnitTestBase(TestFixture _testFixture)
    {
        fixture_ = _testFixture;
    }

{{method_blocks}}
}
"""

template_method = """
    [Fact]
    public abstract Task {{rpc}}Test();
"""


def generate(_options, _outputdir: str):
    org_name = _options["org_name"]
    module_name = _options["module_name"]
    services = _options["services"]

    for service in services.keys():
        method_blocks = ""
        for rpc_name in services[service].keys():
            rpc_map = services[service][rpc_name]
            method_block = (
                template_method.replace("{{service}}", service)
                .replace("{{rpc}}", rpc_name)
                .replace("{{request}}", rpc_map[0])
            )
            method_blocks = method_blocks + method_block
        contents = (
            template.replace("{{org}}", org_name)
            .replace("{{module}}", module_name)
            .replace("{{service}}", service)
            .replace("{{method_blocks}}", method_blocks)
        )
        filepath = os.path.join(_outputdir, "{}UnitTestBase.cs".format(service))
        writer.write(filepath, contents, True)
