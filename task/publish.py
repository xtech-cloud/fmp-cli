import sys
import os
import hashlib
import json
from shutil import copyfile
from common import logger


def run(_version, _config):
    config = _config
    if "active" not in config:
        logger.error("active is required!")
        return 1
    if not config["active"]:
        logger.error("active is false")
        return 1
    logger.debug("! found publish task")
    logger.info("> run publish")
    logger.debug("```")
    if "org_name" not in config:
        logger.error("org_name is required!!")
        return 1
    if "module_name" not in config:
        logger.error("module is required!!")
        return 1
    if "environment" not in config:
        logger.error("environment is required!!")
        return 1
    if "repository" not in config:
        logger.error("repository is required!!")
        return 1

    org_name = _config["org_name"]
    module_name = _config["module_name"]
    environment = _config["environment"]
    repository: str = _config["repository"]
    files = [
        (
            "fmp-{}-{}-lib-proto.dll".format(org_name.lower(), module_name.lower()),
            "vs2022/fmp-{}-{}-lib-proto/bin/Release/netstandard2.1/fmp-{}-{}-lib-proto.dll".format(
                org_name.lower(),
                module_name.lower(),
                org_name.lower(),
                module_name.lower(),
            ),
        ),
        (
            "fmp-{}-{}-lib-bridge.dll".format(org_name.lower(), module_name.lower()),
            "vs2022/fmp-{}-{}-lib-bridge/bin/Release/netstandard2.1/fmp-{}-{}-lib-bridge.dll".format(
                org_name.lower(),
                module_name.lower(),
                org_name.lower(),
                module_name.lower(),
            ),
        ),
        (
            "fmp-{}-{}-lib-mvcs.dll".format(org_name.lower(), module_name.lower()),
            "vs2022/fmp-{}-{}-lib-mvcs/bin/Release/netstandard2.1/fmp-{}-{}-lib-mvcs.dll".format(
                org_name.lower(),
                module_name.lower(),
                org_name.lower(),
                module_name.lower(),
            ),
        ),
        (
            "fmp-{}-{}-lib-razor.dll".format(org_name.lower(), module_name.lower()),
            "vs2022/fmp-{}-{}-lib-razor/bin/Release/net6.0/fmp-{}-{}-lib-razor.dll".format(
                org_name.lower(),
                module_name.lower(),
                org_name.lower(),
                module_name.lower(),
            ),
        ),
        (
            "{}.FMP.MOD.{}.LIB.Unity.dll".format(org_name, module_name),
            "unity2021/_dist_/{}.FMP.MOD.{}.LIB.Unity.dll".format(
                org_name, module_name
            ),
        ),
        (
            "{}_{}@win32.uab".format(org_name.lower(), module_name.lower()),
            "unity2021/_dist_/win32/{}_{}.uab".format(
                org_name.lower(), module_name.lower()
            ),
        ),
    ]

    manifest = {}
    manifest["entries"] = []
    if repository.startswith("file://"):
        repo_dir = repository[7:]
        org_dir = os.path.join(repo_dir, org_name)
        os.makedirs(org_dir, exist_ok=True)
        # TODO read version from file
        version = "1.0.0"
        if environment == "develop":
            version = "develop"
        module_dir = os.path.join(org_dir, module_name) + "@" + version
        os.makedirs(module_dir, exist_ok=True)
        for tup in files:
            if os.path.exists(tup[1]):
                copyfile(tup[1], os.path.join(module_dir, tup[0]))
                md5 = hashlib.md5()
                with open(tup[1], "rb") as f:
                    while True:
                        data = f.read(10240)
                        if not data:
                            break
                        md5.update(data)
                entry = {
                    "file": tup[0],
                    "size": os.path.getsize(tup[1]),
                    "hash": md5.hexdigest(),
                }
                manifest["entries"].append(entry)
                logger.debug("publish {}".format(tup[0]))
    # 保存md5文件
    with open(os.path.join(module_dir, "md5.json"), "w", encoding="utf-8") as wf:
        wf.write(json.dumps(manifest))
        wf.close()

    return 0
