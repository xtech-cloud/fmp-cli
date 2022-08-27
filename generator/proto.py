import os
from proto import parse
from generator.template.proto import healthy
from generator.template.proto import shared


def generate(_orgname: str, _modulename: str, _workdir: str):

    options = {
        "org_name": _orgname,
        "module_name": _modulename,
    }
    dir_proto = os.path.join(_workdir, "proto")
    os.makedirs(dir_proto, exist_ok=True)
    dir_proto = os.path.join(dir_proto, _modulename)
    os.makedirs(dir_proto, exist_ok=True)

    # proto/shared.proto
    shared.generate(options, dir_proto)
    # proto/healthy.proto
    healthy.generate(options, dir_proto)
