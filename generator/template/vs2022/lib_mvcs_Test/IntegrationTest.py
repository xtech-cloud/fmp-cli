import os
from typing import Dict, List, Tuple
from generator.template.utility import writer

template = """
using {{org}}.FMP.MOD.{{module}}.LIB.MVCS;

public class IntegrationTest : IntegrationTestBase
{
    public class TestView
    {

    }

    public IntegrationTest(TestFixture _testFixture) : base(_testFixture)
    {
    }

    public override async Task Test()
    {
    }
}
"""

def generate(_options, _outputdir: str):
    org_name = _options["org_name"]
    module_name = _options["module_name"]

    contents = template.replace("{{org}}", org_name).replace("{{module}}", module_name)
    filepath = os.path.join(_outputdir, "IntegrationTest.cs")
    writer.write(filepath, contents, False)
