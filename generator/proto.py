import os
from proto import parse
from generator.template.proto import healthy
from generator.template.proto import shared
from generator.template.proto import google_api_http
from generator.template.proto import google_api_annotations


def generate(_orgname: str, _modulename: str, _workdir: str):

    options = {
        "org_name": _orgname,
        "module_name": _modulename,
    }
    dir_proto = os.path.join(_workdir, "proto")
    os.makedirs(dir_proto, exist_ok=True)
    dir_proto = os.path.join(dir_proto, _modulename)
    os.makedirs(dir_proto, exist_ok=True)

    # proto/google/api/http.proto
    google_api_http.generate(options, dir_proto)
    # proto/google/api/annotations.proto
    google_api_annotations.generate(options, dir_proto)
    # proto/shared.proto
    shared.generate(options, dir_proto)
    # proto/healthy.proto
    healthy.generate(options, dir_proto)
