import sys
import os
import requests
import hashlib
import json
import grpc
import subprocess
import shutil
from mygrpc import shared_pb2
from mygrpc import shared_pb2_grpc
from mygrpc import application_pb2
from mygrpc import application_pb2_grpc
from shutil import copyfile
from common import logger


def run(_org, _name, _version, _platform, _filepath, _repository):
    if _repository.startswith("grpc://") or _repository.startswith("grpcs://"):
        """
        网络形式
        """
        if _repository.startswith("grpc://"):
            endpoint = _repository[7:]
            channel = grpc.insecure_channel(endpoint)
        elif _repository.startswith("grpcs://"):
            endpoint = _repository[8:]
            channel = grpc.secure_channel(endpoint, grpc.ssl_channel_credentials())
        stub = application_pb2_grpc.ApplicationStub(channel)
        # 创建Application
        rspCreate = stub.Create(
            application_pb2.ApplicationCreateRequest(
                org=_org,
                name=_name,
                version=_version,
                platform=_platform,
            )
        )
        if not (0 == rspCreate.status.code or 1 == rspCreate.status.code):
            logger.error(rspCreate)
            return 1
        # 获取上传地址
        rspPrepare = stub.PrepareUpload(shared_pb2.UuidRequest(uuid=rspCreate.uuid))
        if not (0 == rspPrepare.status.code):
            logger.error(rspPrepare)
            return 1
        # 上传文件
        logger.trace("upload {} ......".format(_filepath))
        filename = "{}.{}.zip".format(_org, _name)
        uploadUrl = rspPrepare.urls[filename]
        headers = {"content-type": "binary/octet-stream"}
        r = requests.put(
            uploadUrl, data=open(_filepath, "rb"), headers=headers
        )
        if 200 != r.status_code:
            logger.error(r)
        # 刷新
        rspFlush = stub.FlushUpload(shared_pb2.UuidRequest(uuid=rspCreate.uuid))
        if not (0 == rspFlush.status.code):
            logger.error(rspFlush)
            return 1

