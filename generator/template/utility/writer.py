import os
from common import logger

def write(_filepath, _contents, _overwrite):
    if os.path.exists(_filepath) and not _overwrite:
        return
    logger.trace("write " + _filepath)
    with open(_filepath, "w", encoding="utf-8") as wf:
        wf.write(_contents)
        wf.close()


def writeVS2022Project(_sln_dir, _project_name, _contents, _overwrite):
    output_dir = os.path.join(_sln_dir, _project_name)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, _project_name + ".csproj")
    write(output_path, _contents, _overwrite)

def writeHexToBinary(_filepath, _bin_hex, _overwrite):
    if os.path.exists(_filepath) and not _overwrite:
        return
    logger.trace("write " + _filepath)
    contents = _bin_hex.replace("\r", "").replace("\n","")
    contents.strip()
    bytes_data = bytes.fromhex(contents)
    with open(_filepath, "wb") as wf:
        wf.write(bytes_data)
        wf.close()
