import os
import sys
import yaml
from generator import proto
from generator import vs2022
from generator import unity2021
from generator import parse
from deploy import docker
from utility import filetohex

def buildOption(
    _version: str,
    _orgname: str,
    _modulename: str,
    _databasedriver: str,
    _debug: bool,
    _workdir: str,
):
    proto_dir = os.path.join(_workdir, "proto")
    proto_dir = os.path.join(proto_dir, _modulename)
    if not os.path.exists(proto_dir):
        print("directory {} not found".format(proto_dir))
        sys.exit(1)

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

    return {
        "version": _version,
        "org_name": _orgname,
        "module_name": _modulename,
        "enums": enums,
        "services": services,
        "messages": messages,
        "database_driver": _databasedriver,
    }


def useWizard(_version):
    print("1. generate")
    print("2. deploy")
    print("3. utility")
    index = input("enter you choice:")

    if "1" == index:
        org_name = input("enter organization name (default XTC):")
        if "" == org_name:
            org_name = "XTC"
        module_name = input("enter module name (e.g. mymodule):")
        if "" == module_name:
            print("!!! module name is required")
            sys.exit(0)
        database_driver = input(
            "choice database's driver [none/mongodb/mysql] (default none):"
        )
        if "" == database_driver:
            database_driver = "none"
        debug = input("print log [y/n] (default n):")
        if "" == debug:
            debug = "n"
        unity = input("generate unity's solution [y/n] (default n):")
        if "" == unity:
            unity = "n"
        options = buildOption(
            _version, org_name, module_name, database_driver, debug == "y", "./"
        )
        vs2022.generate(options, "./")
        if "y" == unity:
            unity2021.generate(options, "./")
            print("!!! 手动运行unity2021/copy-dll.bat更新依赖库")

    elif "2" == index:
        print("1. DSC (Data Storage Center)")
        index = input("enter you choice:")
        target = ""
        if "1" == index:
            target = "DSC"
        docker.buildCompose(target, "./")
    elif "3" == index:
        print("1. file to hex")
        index = input("enter you choice:")
        if "1" == index:
            filepath = input("enter you filepath:")
            filetohex.run(filepath)


def useYaml(_version):
    print("! use fmp.yaml")
    with open("fmp.yaml") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        if "generate" in data:
            config = data["generate"]
            if "active" not in config:
                print("active is required!")
                sys.exit(0)
            if not config["active"]:
                print("active is false")
                sys.exit(0)
            print("! found generate task")
            print("> run generate")
            print("```")
            if "org_name" not in config:
                print("org_name is required!!")
                sys.exit(1)
            if "module_name" not in config:
                print("module_name is required!!")
                sys.exit(1)
            debug = False
            if "debug" in config:
                debug = config["debug"]
            database_driver = "none"
            if "database_driver" in config:
                database_driver = config["database_driver"]
            unity = False
            if "unity_solution" in config:
                unity = config["unity_solution"]
            print("org_name: {}".format(config["org_name"]))
            print("module_name: {}".format(config["module_name"]))
            print("database_driver: {}".format(database_driver))
            print("unity_soluton: {}".format(unity))
            print("debug: {}".format(debug))
            print("```")

            proto.generate(config["org_name"], config["module_name"], "./")

            options = buildOption(
                _version,
                config["org_name"],
                config["module_name"],
                database_driver,
                debug,
                "./",
            )
            vs2022.generate(options, "./")
            if unity:
                unity2021.generate(options, "./")
                print("!!! 手动运行unity2021/copy-dll.bat更新依赖库")


version = "1.18.3"
print("****************************************************")
print("* FMP Client - ver {}".format(version))
print("****************************************************")

if os.path.exists("./fmp.yaml"):
    useYaml(version)
else:
    useWizard(version)
