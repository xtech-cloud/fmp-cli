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

def generate(
    _orgname: str,
    _modulename: str,
    _outputdir: str,
    _enums: List[str],
    _services: Dict[str, Dict[str, Tuple]],
    _messages: Dict[str, List[Tuple]],
):
    method_blocks= ""
    for service in _services.keys():
        method_blocks = method_blocks + template_method.replace("{{service}}", service)
    contents = (
        template.replace("{{org}}", _orgname)
        .replace("{{module}}", _modulename)
        .replace("{{method_blocks}}", method_blocks)
    )
    filepath = os.path.join(_outputdir, "TestFixture.cs")
    writer.write(filepath, contents, False)
