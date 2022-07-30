import os
from typing import Dict, List, Tuple
from generator.template.utility import writer

template = """
using {{org}}.FMP.MOD.{{module}}.LIB.Proto;

public class {{service}}Test : {{service}}UnitTestBase
{
    public {{service}}Test(TestFixture _testFixture)
        : base(_testFixture)
    {
    }

{{method_blocks}}
}
"""

template_method = """
    public override async Task {{rpc}}Test()
    {
        var request = new {{request}}();
        var response = await fixture_.getService{{service}}().{{rpc}}(request, fixture_.context);
        Assert.Equal(0, response.Status.Code);
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
        method_blocks = ""
        for rpc_name in _services[service].keys():
            rpc_map = _services[service][rpc_name]
            method_block = (
                template_method.replace("{{service}}", service)
                .replace("{{rpc}}", rpc_name)
                .replace("{{request}}", rpc_map[0])
            )
            method_blocks = method_blocks + method_block
        contents = (
            template.replace("{{org}}", _orgname)
            .replace("{{module}}", _modulename)
            .replace("{{service}}", service)
            .replace("{{method_blocks}}", method_blocks)
        )
        filepath = os.path.join(_outputdir, "{}UnitTest.cs".format(service))
        writer.write(filepath, contents, False)
