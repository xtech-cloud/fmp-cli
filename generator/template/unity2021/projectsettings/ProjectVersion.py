import os
import uuid
from generator.template.utility import writer

template = """
m_EditorVersion: 2021.3.8f1
m_EditorVersionWithRevision: 2021.3.8f1 (b30333d56e81)
"""


def generate(_options, _outputdir: str):
    output_dir = os.path.join(_outputdir, "ProjectSettings")
    os.makedirs(output_dir, exist_ok=True)

    contents = template
    output_path = os.path.join(output_dir, "ProjectVersion.txt")
    writer.write(output_path, contents, False)
