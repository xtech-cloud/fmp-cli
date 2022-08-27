import sys
import os
import requests
import hashlib
import json
import grpc
from mygrpc import shared_pb2
from mygrpc import shared_pb2_grpc
from mygrpc import agent_pb2
from mygrpc import agent_pb2_grpc
from shutil import copyfile
from common import logger


def run(_version, _config):
    config = _config
    if "active" not in config:
        logger.error("active is required!")
        return 1
    if not config["active"]:
        logger.error("active is false")
        return 1
    logger.debug("! found deploy task")
    logger.info("> run deploy")
    logger.debug("```")
    if "org_name" not in config:
        logger.error("org_name is required!!")
        return 1
    if "module_name" not in config:
        logger.error("module is required!!")
        return 1
    if "environment" not in config:
        logger.error("environment is required!!")
        return 1
    if "agent_port" not in config:
        logger.error("agent_port is required!!")
        return 1

    org_name = _config["org_name"]
    module_name = _config["module_name"]
    environment = _config["environment"]
    repository: str = _config["repository"]
    agent_port = _config["agent_port"]
    # TODO read version from file
    version = "1.0.0"
    if environment == "develop":
        version = "develop"
    files = [
        (
            "{}.{}.zip".format(org_name, module_name),
            "vs2022/fmp-{}-{}-service-grpc/bin/{}.{}.zip".format(
                org_name.lower(),
                module_name.lower(),
                org_name,
                module_name,
            ),
        ),
    ]

    logger.debug("org: {}".format(org_name))
    logger.debug("module: {}".format(module_name))
    logger.debug("environment: {}".format(environment))
    logger.debug("repository: {}".format(repository))
    logger.debug("```")

    manifest = {}
    manifest["entries"] = []
    if repository.startswith("file://"):
        """
        文件形式
        """
        repo_dir = os.path.join(repository[7:], "agents")
        org_dir = os.path.join(repo_dir, org_name)
        module_dir = os.path.join(org_dir, module_name) + "@" + version
        os.makedirs(module_dir, exist_ok=True)
        for tup in files:
            if os.path.exists(tup[1]):
                copyfile(tup[1], os.path.join(module_dir, tup[0]))
                md5 = hashlib.md5()
                with open(tup[1], "rb") as f:
                    while True:
                        data = f.read(10240)
                        if not data:
                            break
                        md5.update(data)
                entry = {
                    "file": tup[0],
                    "size": os.path.getsize(tup[1]),
                    "hash": md5.hexdigest(),
                }
                manifest["entries"].append(entry)
                logger.debug("deploy {}".format(tup[0]))
        # 保存清单文件
        with open(
            os.path.join(module_dir, "manifest.json"), "w", encoding="utf-8"
        ) as wf:
            wf.write(json.dumps(manifest))
        wf.close()
    elif repository.startswith("grpc://"):
        """
        网络形式
        """
        endpoint = repository[7:]
        channel = grpc.insecure_channel(endpoint)
        stub = agent_pb2_grpc.AgentStub(channel)
        # 创建Module
        rspCreate = stub.Create(
            agent_pb2.AgentCreateRequest(
                org=org_name,
                name=module_name,
                version=version,
            )
        )
        if not (0 == rspCreate.status.code or 1 == rspCreate.status.code):
            logger.error(rspCreate)
            return 1
        # 更新
        rspUpdate = stub.Update(agent_pb2.AgentUpdateRequest(uuid=rspCreate.uuid, port=agent_port))
        if not (0 == rspUpdate.status.code or 1 == rspUpdate.status.code):
            logger.error(rspUpdate)
            return 1
        # 获取上传地址
        rspPrepare = stub.PrepareUpload(shared_pb2.UuidRequest(uuid=rspCreate.uuid))
        if not (0 == rspPrepare.status.code):
            logger.error(rspPrepare)
            return 1
        # 上传全部文件
        for tup in files:
            if os.path.exists(tup[1]):
                if tup[0] in rspPrepare.urls:
                    logger.trace("upload {} ......".format(tup[0]))
                    uploadUrl = rspPrepare.urls[tup[0]]
                    headers = {"content-type": "binary/octet-stream"}
                    r = requests.put(
                        uploadUrl, data=open(tup[1], "rb"), headers=headers
                    )
                    if 200 != r.status_code:
                        logger.error(r)
        # 刷新
        rspFlush = stub.FlushUpload(shared_pb2.UuidRequest(uuid=rspCreate.uuid))
        if not (0 == rspFlush.status.code):
            logger.error(rspFlush)
            return 1

    return 0
