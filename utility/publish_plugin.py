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
from mygrpc import plugin_pb2
from mygrpc import plugin_pb2_grpc
from shutil import copyfile
from common import logger


def run(_name, _version, _filepath, _repository):
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
        stub = plugin_pb2_grpc.PluginStub(channel)
        # 创建Plugin
        rspCreate = stub.Create(
            plugin_pb2.PluginCreateRequest(
                name=_name,
                version=_version,
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
        filename = "{}.dll".format(_name)
        uploadUrl = rspPrepare.urls[filename]
        headers = {"content-type": "binary/octet-stream"}
        r = requests.put(uploadUrl, data=open(_filepath, "rb"), headers=headers)
        if 200 != r.status_code:
            logger.error(r)
        # 刷新
        rspFlush = stub.FlushUpload(shared_pb2.UuidRequest(uuid=rspCreate.uuid))
        if not (0 == rspFlush.status.code):
            logger.error(rspFlush)
            return 1
