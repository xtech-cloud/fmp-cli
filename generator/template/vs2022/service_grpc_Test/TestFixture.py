import os
from typing import Dict, List, Tuple
from generator.template.utility import writer

template = """
using {{org}}.FMP.MOD.{{module}}.App.Service;

/// <summary>
/// 测试上下文，用于共享测试资源
/// </summary>
public class TestFixture : TestFixtureBase
{
    public TestFixture()
        : base()
    {
    }

    public override void Dispose()
    {
        base.Dispose();
    }

{{method_blocks}}
}
"""

template_method = """
    protected override void new{{service}}Service()
    {
        throw new NotImplementedException();
        //service{{service}}_ = new {{service}}Service(new {{service}}DAO(new DatabaseOptions()));
    }
"""


def generate(_options, _outputdir: str):
    org_name = _options["org_name"]
    module_name = _options["module_name"]
    services = _options["services"]

    filepath = os.path.join(_outputdir, "IntegrationTestBase.cs")
    writer.write(filepath, template, True)

    method_blocks = ""
    for service in services.keys():
        method_blocks = method_blocks + template_method.replace("{{service}}", service)
    contents = (
        template.replace("{{org}}", org_name)
        .replace("{{module}}", module_name)
        .replace("{{method_blocks}}", method_blocks)
    )
    filepath = os.path.join(_outputdir, "TestFixture.cs")
    writer.write(filepath, contents, False)
