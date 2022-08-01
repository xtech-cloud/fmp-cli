import os
from typing import Dict, List, Tuple
from deploy.template.utility import writer
from deploy.template.mysql import conf as mysql_conf

template = """
version: "3"

services:

  mysql:
    image: mysql:8.0.26
    restart: always
    ports:
      - "3306:3306"
    volumes:
      - ./mysql/data:/var/lib/mysql
    environment:
      MYSQL_ROOT_PASSWORD: "mysql@XTC"
    networks:
      xtc:
        ipv4_address: 10.1.2.11

  mongo:
    image: mongo:5.0.9
    restart: always
    ports:
      - "27017:27017"
    volumes:
      - ./mongo/data:/data/db
    environment:
      MONGO_INITDB_ROOT_USERNAME: root
      MONGO_INITDB_ROOT_PASSWORD: "mongo@XTC"
    networks:
      xtc:
        ipv4_address: 10.1.2.21

  redis:
    image: redis:7.0.4
    restart: always
    ports:
      - "6379:6379"
    volumes:
      - ./redis/data:/data
    networks:
      xtc:
        ipv4_address: 10.1.2.31

  minio:
    image: minio/minio:RELEASE.2022-07-30T05-21-40Z
    restart: always
    ports:
      - "9000:9000"
      - "9001:9001"
    volumes:
      - ./minio/data:/data
    environment:
      MINIO_ROOT_USER: "3KJLIOSFODNN0EXAMPO0"
      MINIO_ROOT_PASSWORD: "vJalrXUtnFEMI/I5MDENG/bPxRfmCYEXAMPLEHEY"
    command: server /data --console-address ":9001"
    networks:
      xtc:
        ipv4_address: 10.1.2.41

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
    filepath = os.path.join(_outputdir, "docker-compose-dsc.yml")
    writer.write(filepath, contents, False)

    mysql_conf.build(_outputdir)

