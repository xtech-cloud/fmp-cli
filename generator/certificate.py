import os
from proto import parse
from generator.template.certificate import xtc_crt
from generator.template.certificate import xtc_key


def generate(_orgname: str, _modulename: str, _workdir: str):

    options = {
        "org_name": _orgname,
        "module_name": _modulename,
    }
    dir_cers = os.path.join(_workdir, "cers")
    os.makedirs(dir_cers, exist_ok=True)

    # cers/xtc.crt
    xtc_crt.generate(options, dir_cers)
    # cers/xtc.key
    xtc_key.generate(options, dir_cers)
