import os
from typing import Dict, List, Tuple
from generator.template.utility import writer

template = """
using Grpc.Net.Client;
using {{org}}.FMP.MOD.{{module}}.LIB.Proto;

public class IntegrationTest : IntegrationTestBase
{
    [Fact]
    public override async Task Test()
    {
        var channel = GrpcChannel.ForAddress("https://localhost:19000", new GrpcChannelOptions());
        throw new NotImplementedException();

        /*
        var clientHealthy = new Healthy.HealthyClient(channel);
        var response = await clientHealthy.EchoAsync(new HealthyEchoRequest { Msg = "hello" });
        Assert.Equal(0, response.Status.Code);
        */
    }
}
"""

def generate(_options, _outputdir: str):
    org_name = _options["org_name"]
    module_name = _options["module_name"]

    contents = template.replace("{{org}}", org_name).replace("{{module}}", module_name)
    filepath = os.path.join(_outputdir, "IntegrationTest.cs")
    writer.write(filepath, contents, False)
