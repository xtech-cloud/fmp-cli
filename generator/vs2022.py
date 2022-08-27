import os
from typing import Dict, List, Tuple
from proto import parse
from generator.template.vs2022 import sln
from generator.template.vs2022 import csproj_lib_proto
from generator.template.vs2022 import csproj_lib_bridge
from generator.template.vs2022 import csproj_lib_mvcs
from generator.template.vs2022 import csproj_lib_mvcs_Test
from generator.template.vs2022 import csproj_lib_razor
from generator.template.vs2022 import csproj_service_grpc
from generator.template.vs2022 import csproj_service_grpc_Test
from generator.template.vs2022 import csproj_web_blazor
from generator.template.vs2022 import gitignore


def generate(_options, _workdir: str):

    os.makedirs("vs2022", exist_ok=True)
    dir_vs2022 = os.path.join(_workdir, "vs2022")
    # 生成解决方案文件
    sln.generate(_options, dir_vs2022)
    # 生成proto项目文件
    csproj_lib_proto.generate(_options, dir_vs2022)
    # 生成bridge项目文件
    csproj_lib_bridge.generate(_options, dir_vs2022)
    # 生成mvcs项目文件
    csproj_lib_mvcs.generate(_options, dir_vs2022)
    # 生成mvcs测试项目文件
    csproj_lib_mvcs_Test.generate(_options, dir_vs2022)
    # 生成razor项目文件
    csproj_lib_razor.generate(_options, dir_vs2022)
    # 生成service项目文件
    csproj_service_grpc.generate(_options, dir_vs2022)
    # 生成service测试项目文件
    csproj_service_grpc_Test.generate(_options, dir_vs2022)
    # 生成blazor项目文件
    csproj_web_blazor.generate(_options, dir_vs2022)
    # 生成.gitignore
    gitignore.generate(_options, dir_vs2022)
