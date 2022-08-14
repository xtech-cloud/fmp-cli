import os
import uuid
from generator.template.utility import writer

template = """<?xml version="1.0" encoding="utf-8"?>
<MyConfig version="1.0">
    <!-- UI 
      visible: 预加载完成后是否显示
      slot: ui根节点在主Canvas中的挂载路径
    -->
    <UI visible="true" slot="[root]"/>
    <!-- 远程过程调用
      address: 地址
    -->
    <GRPC address="https://localhost:19000"/>
    <!-- 样式列表
      name: 名称
    -->
    <Styles>
        <Style name="default"></Style>
        </Styles>
        <!-- 预创建的实例列表
          uid: 实例的唯一ID
          style: 使用的样式名
        -->
        <Instances>
          <Instance uid="default" style="default"></Instance>
        </Instances>
</MyConfig>
"""

def generate(_options, _outputdir: str):
    output_dir = os.path.join(_outputdir, "Assets")
    os.makedirs(output_dir, exist_ok=True)
    output_dir = os.path.join(output_dir, "Exports")
    os.makedirs(output_dir, exist_ok=True)

    contents = template
    output_path = os.path.join(output_dir, "{}_{}.xml".format(_options["org_name"], _options["module_name"]))
    writer.write(output_path, contents, False)
