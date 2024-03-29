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
from mygrpc import module_pb2
from mygrpc import module_pb2_grpc
from shutil import copyfile
from common import logger


def run(_version, _config, _force):
    config = _config
    if not _force:
        if "active" not in config:
            logger.error("active is required!")
            return 1
        if not config["active"]:
            logger.warn("active is false")
            return -1
    logger.debug("! found publish task")
    logger.info("> run publish")
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
    if "repository" not in config:
        logger.error("repository is required!!")
        return 1

    org_name = _config["org_name"]
    module_name = _config["module_name"]
    environment = _config["environment"]
    repository: str = _config["repository"]
    p = os.popen("git tag --contains")
    git_version = p.read().strip()
    if "" == git_version:
        logger.error("The current commit has no tag!")
        return 1

    version = git_version
    if environment == "develop":
        version = "develop"
    files = [
        (
            "fmp-{}-{}-lib-proto.dll".format(org_name.lower(), module_name.lower()),
            "vs2022/fmp-{}-{}-lib-proto/bin/Release/netstandard2.1/publish/fmp-{}-{}-lib-proto.dll".format(
                org_name.lower(),
                module_name.lower(),
                org_name.lower(),
                module_name.lower(),
            ),
        ),
        (
            "fmp-{}-{}-lib-bridge.dll".format(org_name.lower(), module_name.lower()),
            "vs2022/fmp-{}-{}-lib-bridge/bin/Release/netstandard2.1/publish/fmp-{}-{}-lib-bridge.dll".format(
                org_name.lower(),
                module_name.lower(),
                org_name.lower(),
                module_name.lower(),
            ),
        ),
        (
            "fmp-{}-{}-lib-mvcs.dll".format(org_name.lower(), module_name.lower()),
            "vs2022/fmp-{}-{}-lib-mvcs/bin/Release/netstandard2.1/publish/fmp-{}-{}-lib-mvcs.dll".format(
                org_name.lower(),
                module_name.lower(),
                org_name.lower(),
                module_name.lower(),
            ),
        ),
        (
            "fmp-{}-{}-lib-razor.dll".format(org_name.lower(), module_name.lower()),
            "vs2022/fmp-{}-{}-lib-razor/bin/Release/net7.0/publish/fmp-{}-{}-lib-razor.dll".format(
                org_name.lower(),
                module_name.lower(),
                org_name.lower(),
                module_name.lower(),
            ),
        ),
        (
            "{}.FMP.MOD.{}.LIB.Unity.dll".format(org_name, module_name),
            "unity2021/_dist_/{}.FMP.MOD.{}.LIB.Unity.dll".format(
                org_name, module_name
            ),
        ),
        (
            "{}_{}@windows.uab".format(org_name.lower(), module_name.lower()),
            "unity2021/_dist_/windows/{}_{}.uab".format(
                org_name.lower(), module_name.lower()
            ),
        ),
        (
            "{}_{}@android.uab".format(org_name.lower(), module_name.lower()),
            "unity2021/_dist_/android/{}_{}.uab".format(
                org_name.lower(), module_name.lower()
            ),
        ),
        (
            "{}_{}@webgl.uab".format(org_name.lower(), module_name.lower()),
            "unity2021/_dist_/webgl/{}_{}.uab".format(
                org_name.lower(), module_name.lower()
            ),
        ),
        (
            "{}_{}.xml".format(org_name, module_name),
            "unity2021/{}/Assets/Exports/{}_{}.xml".format(
                module_name, org_name, module_name
            ),
        ),
        (
            "{}_{}.json".format(org_name, module_name),
            "unity2021/{}/Assets/Exports/{}_{}.json".format(
                module_name, org_name, module_name
            ),
        ),
    ]

    logger.debug("org: {}".format(org_name))
    logger.debug("module: {}".format(module_name))
    logger.debug("verison: {}".format(git_version))
    logger.debug("environment: {}".format(environment))
    logger.debug("repository: {}".format(repository))
    logger.debug("```")

    """
    发布vs2022
    """
    publish_vs2022_cmd = "dotnet publish -c Release /p:Version={}".format(git_version)
    publish_cwd = "vs2022/fmp-{}-{}-lib-proto".format(org_name.lower(), module_name.lower())
    logger.trace("publish proto ...")
    pbuild = subprocess.run(publish_vs2022_cmd, cwd=publish_cwd, stdout=subprocess.PIPE)
    if 0 != pbuild.returncode:
        logger.error("publish proto failure")
        return 1
    publish_cwd = "vs2022/fmp-{}-{}-lib-bridge".format(org_name.lower(), module_name.lower())
    logger.trace("publish bridge ...")
    pbuild = subprocess.run(publish_vs2022_cmd, cwd=publish_cwd, stdout=subprocess.PIPE)
    if 0 != pbuild.returncode:
        logger.error("publish bridge failure")
        return 1
    publish_cwd = "vs2022/fmp-{}-{}-lib-mvcs".format(org_name.lower(), module_name.lower())
    logger.trace("publish mvcs ...")
    pbuild = subprocess.run(publish_vs2022_cmd, cwd=publish_cwd, stdout=subprocess.PIPE)
    if 0 != pbuild.returncode:
        logger.error("publish mvcs failure")
        return 1
    publish_cwd = "vs2022/fmp-{}-{}-lib-razor".format(org_name.lower(), module_name.lower())
    logger.trace("publish razor ...")
    pbuild = subprocess.run(publish_vs2022_cmd, cwd=publish_cwd, stdout=subprocess.PIPE)
    if 0 != pbuild.returncode:
        logger.error("publish razor failure")
        return 1
    publish_cwd = "vs2022/fmp-{}-{}-service-grpc".format(org_name.lower(), module_name.lower())
    logger.trace("publish service ...")
    pbuild = subprocess.run(publish_vs2022_cmd, cwd=publish_cwd, stdout=subprocess.PIPE)
    if 0 != pbuild.returncode:
        logger.error("publish service failure")
        return 1

    """
    打包server
    """
    publish_rootdir = "vs2022/fmp-{}-{}-service-grpc/bin/Release/net7.0".format(
        org_name.lower(),
        module_name.lower(),
    )
    publish_basedir = "{}.{}".format(org_name, module_name)
    os.rename(os.path.join(publish_rootdir, "publish"), os.path.join(publish_rootdir, publish_basedir))

    zipfile_path = "vs2022/fmp-{}-{}-service-grpc/bin/{}.{}".format(
        org_name.lower(),
        module_name.lower(),
        org_name,
        module_name,
    )
    logger.trace("pack {}.zip ...".format(zipfile_path))
    shutil.make_archive(zipfile_path, "zip", publish_rootdir, publish_basedir)
    if os.path.exists(os.path.join(publish_rootdir, publish_basedir)):
        shutil.rmtree(os.path.join(publish_rootdir, publish_basedir))

    manifest = {}
    manifest["entries"] = []
    if repository.startswith("file://"):
        """
        文件形式
        """
        repo_dir = os.path.join(repository[7:], "modules")
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
                logger.debug("publish {}".format(tup[0]))
        # 保存清单文件
        with open(
            os.path.join(module_dir, "manifest.json"), "w", encoding="utf-8"
        ) as wf:
            wf.write(json.dumps(manifest))
        wf.close()
    elif repository.startswith("http://") or repository.startswith("https://"):
        url = repository + "/v1/xtc/repository/module/create"
        headers = {"content-type": "application/json"}
        body_dict = {}
        body_dict["org"] = org_name
        body_dict["name"] = module_name
        body_dict["version"] = version
        body_json = json.dumps(body_dict, ensure_ascii=False)
        r = requests.post(
            url, data=body_json, headers=headers
        )
        if 200 != r.status_code:
            logger.error(r)
            return 1
        replay_json = r.json()
        if "uuid" not in replay_json:
            logger.error(replay_json)
            return 1
        module_uuid = replay_json["uuid"]
        # 获取上传地址
        url = repository + "/v1/xtc/repository/module/prepareupload"
        body_dict = {}
        body_dict["uuid"] = replay_json["uuid"]
        body_json = json.dumps(body_dict, ensure_ascii=False)
        r = requests.post(
            url, data=body_json, headers=headers
        )
        if 200 != r.status_code:
            logger.error(r)
            return 1
        replay_json = r.json()
        if "urls" not in replay_json:
            logger.error(replay_json)
            return 1
        urls = replay_json["urls"]
        for tup in files:
            if os.path.exists(tup[1]):
                if tup[0] in urls:
                    logger.trace("upload {} ......".format(tup[0]))
                    uploadUrl = urls[tup[0]]
                    headers = {"content-type": "binary/octet-stream"}
                    logger.trace(uploadUrl)
                    r = requests.put(
                        uploadUrl, data=open(tup[1], "rb"), headers=headers
                    )
                    if 200 != r.status_code:
                        logger.error(r)
        # 刷新
        url = repository + "/v1/xtc/repository/module/flushupload"
        body_dict = {}
        body_dict["uuid"] = replay_json["uuid"]
        body_json = json.dumps(body_dict, ensure_ascii=False)
        r = requests.post(
            url, data=body_json, headers=headers
        )
        if 200 != r.status_code:
            logger.error(r)
            return 1
        # 更新
        url = repository + "/v1/xtc/repository/module/update"
        body_dict = {}
        body_dict["uuid"] = replay_json["uuid"]
        body_dict["cli"] = _version
        body_json = json.dumps(body_dict, ensure_ascii=False)
        r = requests.post(
            url, data=body_json, headers=headers
        )
        if 200 != r.status_code:
            logger.error(r)
            return 1
    elif repository.startswith("grpc://") or repository.startswith("grpcs://"):
        """
        网络形式
        """
        if repository.startswith("grpc://"):
            endpoint = repository[7:]
            channel = grpc.insecure_channel(endpoint)
        elif repository.startswith("grpcs://"):
            endpoint = repository[8:]
            channel = grpc.secure_channel(endpoint, grpc.ssl_channel_credentials())
        stub = module_pb2_grpc.ModuleStub(channel)
        # 创建Module
        rspCreate = stub.Create(
            module_pb2.ModuleCreateRequest(
                org=org_name,
                name=module_name,
                version=version,
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
        # 更新
        rspUpdate = stub.Update(module_pb2.ModuleUpdateRequest(uuid=rspCreate.uuid, cli=_version))
        if not (0 == rspPrepare.status.code):
            logger.error(rspPrepare)
            return 1

    return 0
