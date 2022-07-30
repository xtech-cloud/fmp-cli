import os
import sys
from generator import vs2022

print("****************************************************")
print("* FMP Client - ver 1.6.1")
print("****************************************************")

print("1. generate")
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

    vs2022.generate(debug == "y", org_name, module_name, database_driver, "./")
