import os
from typing import Dict, List, Tuple
from generator import parse
from generator.template.vs2022 import sln
from generator.template.vs2022 import csproj_lib_proto
from generator.template.vs2022 import csproj_lib_bridge
from generator.template.vs2022 import csproj_lib_mvcs
from generator.template.vs2022 import csproj_lib_razor
from generator.template.vs2022 import csproj_service_grpc
from generator.template.vs2022 import csproj_service_grpc_Test
from generator.template.vs2022 import csproj_web_blazor


def generate(_debug: bool, _orgname: str, _modulename: str, _workdir: str):
    org_name = _orgname
    mod_name = _modulename

    if "" == org_name:
        print("org is empty")
        return

    if "" == mod_name:
        print("mod is empty")
        return

    proto_dir = os.path.join(_workdir, "proto")
    proto_dir = os.path.join(proto_dir, _modulename)
    if not os.path.exists(proto_dir):
        print("directory {} not found".format(proto_dir))
        return

    # 解析协议文件
    enums: List[str] = []

    services: Dict[str, Dict[str, Tuple]] = {}
    """
    service Healthy {
      rpc Echo(EchoRequest) returns (EchoResponse) {}
    }
    转换格式为
    {
        startkit:
        {
            healthy: (EchoRequest, EchoResponse)
        }
    }
    """

    messages: Dict[str, List[Tuple]] = {}
    """
    message EchoRequest {
      string msg = 1;  // 消息
    }
    转换为
    {
        EchoRequest:
        [
            (msg, string, 消息),
        ]
    }
    """
    parse.scan_protos(proto_dir, enums, services, messages)
    if _debug:
        print(services)
        print(messages)

    os.makedirs("vs2022", exist_ok=True)
    dir_vs2022 = os.path.join(_workdir, "vs2022")
    # 生成解决方案文件
    sln.generate(_orgname, _modulename, dir_vs2022)
    # 生成proto项目文件
    csproj_lib_proto.generate(_orgname, _modulename, dir_vs2022)
    # 生成bridge项目文件
    csproj_lib_bridge.generate(
        _orgname, _modulename, dir_vs2022, enums, services, messages
    )
    # 生成mvcs项目文件
    csproj_lib_mvcs.generate(
        _orgname, _modulename, dir_vs2022, enums, services, messages
    )
    # 生成razor项目文件
    csproj_lib_razor.generate(
        _orgname, _modulename, dir_vs2022, enums, services, messages
    )
    # 生成service项目文件
    csproj_service_grpc.generate(
        _orgname, _modulename, dir_vs2022, enums, services, messages
    )
    # 生成service测试项目文件
    csproj_service_grpc_Test.generate(
        _orgname, _modulename, dir_vs2022, enums, services, messages
    )
    # 生成blazor项目文件
    csproj_web_blazor.generate(
        _orgname, _modulename, dir_vs2022, enums, services, messages
    )
