import sys
import os
from shutil import copyfile
from common import logger


def run(_version, _config):
    config = _config
    if "active" not in config:
        logger.err("active is required!")
        return 1
    if not config["active"]:
        logger.err("active is false")
        return 1
    logger.debug("! found publish task")
    logger.info("> run publish")
    logger.debug("```")
    if "org_name" not in config:
        logger.err("org_name is required!!")
        return 1
    if "module_name" not in config:
        logger.err("module is required!!")
        return 1
    if "environment" not in config:
        logger.err("environment is required!!")
        return 1
    if "repository" not in config:
        logger.err("repository is required!!")
        return 1

    home_dir = os.path.expanduser("~")

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

    if repository.startswith("file://"):
        repo_dir = repository[7:]
        org_dir = os.path.join(repo_dir, org_name)
        os.makedirs(org_dir, exist_ok=True)
        version = "develop"
        if environment == "product":
            version = "1.0.0"
        module_dir = os.path.join(org_dir, module_name) + "@" + version
        os.makedirs(module_dir, exist_ok=True)
        for tup in files:
            if os.path.exists(tup[1]):
                copyfile(tup[1], os.path.join(module_dir, tup[0]))

    return 0
