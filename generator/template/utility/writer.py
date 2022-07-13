import os


def write(_filepath, _contents, _overwrite):
    if os.path.exists(_filepath) and not _overwrite:
        return
    print("write " + _filepath)
    with open(_filepath, "w", encoding="utf-8") as wf:
        wf.write(_contents)
        wf.close()


def writeVS2022Project(_sln_dir, _project_name, _contents, _overwrite):
    output_dir = os.path.join(_sln_dir, _project_name)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, _project_name + ".csproj")
    write(output_path, _contents, _overwrite)
