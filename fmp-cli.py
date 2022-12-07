import os
import sys
import yaml
import argparse
from common import logger
from generator import proto
from generator import vs2022
from generator import unity2021
from deploy import docker
from utility import filetohex
from utility import publish_application
from utility import publish_plugin
from task import generate
from task import publish
from task import deploy


def useWizard(_version):
    print("1. create")
    print("2. deploy")
    print("3. publish")
    print("4. utility")
    index = input("enter you choice:")

    if "1" == index:
        # TODO generate fmp.yaml
        pass
    elif "2" == index:
        print("1. DSC (Data Storage Center)")
        print("2. MSA (Micro Service Agent)")
        index = input("enter you choice:")
        target = ""
        if "1" == index:
            target = "DSC"
        elif "2" == index:
            target = "MSA"
        docker.buildCompose(target, "./")
    elif "3" == index:
        print("1. publish plugin")
        print("2. publish application")
        index = input("enter you choice:")
        if "1" == index:
            name = input("enter name:")
            version = input("enter version:")
            filepath = input("enter filepath:")
            repository = input("enter repository:")
            publish_plugin.run(name, version, filepath, repository)
        elif "2" == index:
            org = input("enter org:")
            name = input("enter name:")
            version = input("enter version:")
            platform = input("enter platform:")
            filepath = input("enter filepath:")
            repository = input("enter repository:")
            publish_application.run(org, name, version, platform, filepath, repository)
    elif "4" == index:
        print("1. file to hex")
        index = input("enter you choice:")
        if "1" == index:
            filepath = input("enter you filepath:")
            filetohex.run(filepath)


def printResult(_task, _code):
    if -1 == _code:
        logger.warn("-------------------------------------------------------------")
        logger.warn(" {} SKIP".format(_task))
        logger.warn("-------------------------------------------------------------")
    elif 0 == _code:
        logger.info("-------------------------------------------------------------")
        logger.info(" {} SUCCESS".format(_task))
        logger.info("-------------------------------------------------------------")
    else:
        logger.error("-------------------------------------------------------------")
        logger.error(" {} FAILURE".format(_task))
        logger.error("-------------------------------------------------------------")


def check_yaml_file(_print: bool, _exit: bool):
    """
    检测yaml文件是否存在
    """
    yaml_file = "./fmp.yaml"
    if os.path.exists("./.fmp.yaml"):
        yaml_file = "./.fmp.yaml"
    exists = os.path.exists(yaml_file)
    if not exists and _print:
        logger.error("fmp.yaml or .fmp.yaml not found")
    if not exists and _exit:
        sys.exit(1)
    return exists, yaml_file


def run_task_generate(_force: bool):
    """
    执行生成任务
    """
    exists, yaml_file = check_yaml_file(True, True)
    logger.debug("! use {}".format(yaml_file))
    with open(yaml_file) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        if "generate" in data:
            config = data["generate"]
            config["org_name"] = data["org_name"]
            config["module_name"] = data["module_name"]
            code = generate.run(version, config, _force)
            printResult("Generate", code)


def run_task_publish(_force: bool):
    """
    执行发布任务
    """
    exists, yaml_file = check_yaml_file(True, True)
    logger.debug("! use {}".format(yaml_file))
    with open(yaml_file) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        if "publish" in data:
            config = data["publish"]
            config["org_name"] = data["org_name"]
            config["module_name"] = data["module_name"]
            code = publish.run(version, config, _force)
            printResult("Publish", code)


def run_task_deploy(_force: bool):
    """
    执行部署任务
    """
    exists, yaml_file = check_yaml_file(True, True)
    logger.debug("! use {}".format(yaml_file))
    with open(yaml_file) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        if "deploy" in data:
            config = data["deploy"]
            config["org_name"] = data["org_name"]
            config["module_name"] = data["module_name"]
            code = deploy.run(version, config, _force)
            printResult("Deploy", code)


def parse_args():
    parser = argparse.ArgumentParser("FMP Cli")
    parser.add_argument("-g", help="generate", action="store_true")
    parser.add_argument("-p", help="publish", action="store_true")
    parser.add_argument("-d", help="deploy", action="store_true")
    args = parser.parse_args()
    if args.g:
        run_task_generate(True)
    if args.p:
        run_task_publish(True)
    if args.d:
        run_task_deploy(True)


if __name__ == "__main__":
    version = "1.68.0"
    logger.info("****************************************************")
    logger.info("* FMP Client - ver {}".format(version))
    logger.info("****************************************************")
    if len(sys.argv) > 1:
        parse_args()
        sys.exit(0)
    """
    无参数时使用fmp.yaml文件
    """
    exists, yaml_file = check_yaml_file(False, False)
    if exists:
        """
        执行fmp.yaml文件
        """
        run_task_generate(False)
        run_task_publish(False)
        run_task_deploy(False)
    else:
        """
        使用向导
        """
        useWizard(version)
