import os
import sys
import yaml
from common import logger
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
        logger.error("directory {} not found".format(proto_dir))
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
        logger.trace(services)
        logger.trace(messages)

    return {
        "version": _version,
        "org_name": _orgname,
        "module_name": _modulename,
        "enums": enums,
        "services": services,
        "messages": messages,
        "database_driver": _databasedriver,
    }


def run(_version, _config):
    config = _config
    logger.debug("! found generate task")
    if "active" not in config:
        logger.error("active is required!")
        return 1
    if not config["active"]:
        return -1
    logger.info("> run generate")
    logger.debug("```")
    if "org_name" not in config:
        logger.error("org_name is required!!")
        return 1
    if "module_name" not in config:
        logger.error("module_name is required!!")
        return 1
    debug = False
    if "debug" in config:
        debug = config["debug"]
    database_driver = "none"
    if "database_driver" in config:
        database_driver = config["database_driver"]
    unity = False
    if "unity_solution" in config:
        unity = config["unity_solution"]
    logger.debug("org_name: {}".format(config["org_name"]))
    logger.debug("module_name: {}".format(config["module_name"]))
    logger.debug("database_driver: {}".format(database_driver))
    logger.debug("unity_soluton: {}".format(unity))
    logger.debug("debug: {}".format(debug))
    logger.debug("```")

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
        logger.warn("!!! 手动运行unity2021/copy-dll.bat更新依赖库")
    return 0
