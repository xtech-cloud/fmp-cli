import os
import sys
import yaml
from generator import vs2022
from deploy import docker

def useWizard():
    print("1. generate")
    print("2. deploy")
    index = input("enter you choice:")

    if "1" == index:
        org_name = input("enter organization name (default XTC):")
        if "" == org_name:
            org_name = "XTC"
        module_name = input("enter module name (e.g. mymodule):")
        if "" == module_name:
            print("!!! module name is required")
            sys.exit(0)
        database_driver = input("choice database's driver [none/mongodb/mysql] (default none):")
        if "" == database_driver:
            database_driver = "none"
        debug = input("print log [y/n] (default n):")
        if "" == debug:
            debug = "n"
        unity = input("generate unity's solution [y/n] (default n):")
        if "" == unity:
            unity = "n"
        vs2022.generate(debug == "y", org_name, module_name, database_driver, "./")
        if "y" == unity:
            unity2021.generate(debug == "y", org_name, module_name, "./")

    elif "2" == index:
        print("1. DSC (Data Storage Center)")
        index = input("enter you choice:")
        target = ""
        if "1" == index:
            target = "DSC"
        docker.buildCompose(target, "./")

def useYaml():
    print("! use fmp.yaml")
    with open('fmp.yaml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        if "generate" in data:
            print("! found generate task")
            print("> run generate")
            print("```")
            config = data["generate"]
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

            vs2022.generate(debug, config["org_name"], config["module_name"], database_driver, "./")

print("****************************************************")
print("* FMP Client - ver 1.8.0")
print("****************************************************")

if os.path.exists("./fmp.yaml"):
    useYaml()
else:
    useWizard()

