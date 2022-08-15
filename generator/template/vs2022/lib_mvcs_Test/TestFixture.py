import os
from typing import Dict, List, Tuple
from generator.template.utility import writer

template = """
public class TestFixture: TestFixtureBase
{
    public TestFixture()
    : base()
    {
    }

    public override void Dispose()
    {
        base.Dispose();
    }
}
"""


def generate(_options, _outputdir: str):
    org_name = _options["org_name"]
    module_name = _options["module_name"]

    contents = template
    filepath = os.path.join(_outputdir, "TestFixture.cs")
    writer.write(filepath, contents, False)
