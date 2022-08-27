import os
import sys
import yaml
from common import logger
from generator import proto
from generator import vs2022
from generator import unity2021
from deploy import docker
from utility import filetohex
from task import generate
from task import publish

def useWizard(_version):
    print("1. create")
    print("2. deploy")
    print("3. utility")
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

version = "1.30.0"
logger.info("****************************************************")
logger.info("* FMP Client - ver {}".format(version))
logger.info("****************************************************")

fmp_yaml = "./fmp.yaml"
if os.path.exists("./.fmp.yaml"):
    fmp_yaml = "./.fmp.yaml"

if os.path.exists(fmp_yaml):
    logger.debug("! use fmp.yaml")
    with open(fmp_yaml) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        if "generate" in data:
            config = data["generate"]
            code = generate.run(version, config)
            printResult("Generate", code)
        if "publish" in data:
            config = data["publish"]
            code = publish.run(version, config)
            printResult("Publish", code)
else:
    useWizard(version)
