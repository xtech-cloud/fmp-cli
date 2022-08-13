import os
import sys
from generator import vs2022
from deploy import docker

print("****************************************************")
print("* FMP Client - ver 1.7.6")
print("****************************************************")

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
