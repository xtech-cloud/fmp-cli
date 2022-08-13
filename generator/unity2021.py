import os
from typing import Dict, List, Tuple
from generator import parse
from generator.template.unity2021 import manifest
from generator.template.unity2021 import packages_lock


def generate(
    _debug: bool, _orgname: str, _modulename: str, _workdir: str
):

    if "" == _orgname:
        print("org is empty")
        return

    if "" == _modulename:
        print("mod is empty")
        return

    dir_unity2021 = os.path.join(_workdir, "unity2021/{}".format(_modulename))
    os.makedirs(dir_unity2021, exist_ok=True)
    dir_packages = os.path.join(dir_unity2021, "Packages")
    os.makedirs(dir_packages, exist_ok=True)

    # 生成manifest
    manifest.generate(_orgname, _modulename, dir_packages)
    # 生成packages-lock
    packages_lock.generate(_orgname, _modulename, dir_packages)

