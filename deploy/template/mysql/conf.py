import os
from typing import Dict, List, Tuple
from deploy.template.utility import writer

template = """
[mysqld]
character_set_server=utf8
[client]
default-character-set=utf8
"""


def build(
    _outputdir: str,
):
    contents = template
    outputdir = os.path.join(_outputdir, "mysql")
    outputdir = os.path.join(outputdir, "conf")
    os.makedirs(outputdir, exist_ok=True)
    filepath = os.path.join(outputdir, "mysql.cnf")
    writer.write(filepath, contents, False)

