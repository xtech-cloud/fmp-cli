import os
from typing import Dict, List, Tuple
from deploy.template.utility import writer

template = """
version: "3"

services:
  fmp-daemon:
    image: xtechcloud/fmp-daemon:v1.0.0
    restart: always
    ports:
      - "16166:16166"
      - "28000-28099:28000-28099"
      - "29000-29099:29000-29099"
    volumes:
      - ./fmp-daemon/apps:/app/apps
      - ./fmp-daemon/cers:/app/cers
    networks:
      xtc:
        ipv4_address: 10.1.100.11

networks:
  xtc:
    driver: bridge
    ipam:
      driver: default
      config:
      - subnet: 10.1.0.0/16
"""


def build(
    _outputdir: str,
):
    contents = template
    filepath = os.path.join(_outputdir, "docker-compose-msa.yml")
    writer.write(filepath, contents, False)
