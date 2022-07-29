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

def generate(
    _orgname: str,
    _modulename: str,
    _outputdir: str,
):
    contents = template.replace("{{org}}", _orgname).replace("{{module}}", _modulename)
    filepath = os.path.join(_outputdir, "IntegrationTest.cs")
    writer.write(filepath, contents, False)
