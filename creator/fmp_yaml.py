import os
from common import logger

template_fmp_yaml = """org_name: {{org_name}}
module_name: {{module_name}}
generate:
  active: true
  database_driver: none
  debug: false
  unity_solution: true
publish:
  active: true
  environment: product
  repository: grpc://localhost:18000
deploy:
  active: true
  environment: product
  repository: grpc://localhost:18000
  agent_port: 28000
"""

template_gitignore = ".fmp.yaml"

def writeYaml(_org, _name):
    contents = template_fmp_yaml
    contents = contents.replace("{{org_name}}", _org)
    contents = contents.replace("{{module_name}}", _name)

    filepath = "fmp.yaml"
    if os.path.exists(filepath):
        logger.error(filepath + "exists")
        return

    logger.trace("write " + filepath)
    with open(filepath, "w", encoding="utf-8") as wf:
        wf.write(contents)
        wf.close()

def writeGitIgnore():
    contents = template_gitignore

    filepath = ".gitignore"
    if os.path.exists(filepath):
        logger.error(filepath + "exists")
        return

    logger.trace("write " + filepath)
    with open(filepath, "w", encoding="utf-8") as wf:
        wf.write(contents)
        wf.close()


def run(_org, _name):
    writeYaml(_org, _name)
    writeGitIgnore()
