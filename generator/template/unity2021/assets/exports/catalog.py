import os
import uuid
from generator.template.utility import writer

template = """{
    "sectionS":[
        {
            "name":"".
            "path": "/",
            "instanceS": [
                "default"
            ],
            "contentS": [
                "{{org_name}}.{{module_name}}/+"
            ],
            "kvS":[
                "key1":"value1",
                "key2":"value2"
            ]
        }
    ]
}
"""

def generate(_options, _outputdir: str):
    output_dir = os.path.join(_outputdir, "Assets")
    os.makedirs(output_dir, exist_ok=True)
    output_dir = os.path.join(output_dir, "Exports")
    os.makedirs(output_dir, exist_ok=True)

    contents = template
    contents = contents.replace("{{org_name}}", _options["org_name"])
    contents = contents.replace("{{module_name}}", _options["module_name"])

    output_path = os.path.join(output_dir, "{}_{}.json".format(_options["org_name"], _options["module_name"]))
    writer.write(output_path, contents, False)
