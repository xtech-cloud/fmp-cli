import os
import uuid
from generator.template.utility import writer

template = """
using System;
using LibMVCS = XTC.FMP.LIB.MVCS;
using {{org_name}}.FMP.MOD.{{module_name}}.LIB.Bridge;
using {{org_name}}.FMP.MOD.{{module_name}}.LIB.MVCS;

namespace {{org_name}}.FMP.MOD.{{module_name}}.LIB.Unity
{
    /// <summary>
    /// 虚拟视图，用于处理消息订阅
    /// </summary>
    public class DummyView :  DummyViewBase
    {
        public DummyView(string _uid) : base(_uid)
        {
        }

        protected override void setup()
        {
            base.setup();
        }
    }
}

"""

def generate(_options, _outputdir: str):
    output_dir = os.path.join(_outputdir, "Assets")
    os.makedirs(output_dir, exist_ok=True)
    output_dir = os.path.join(output_dir, "Scripts")
    os.makedirs(output_dir, exist_ok=True)
    output_dir = os.path.join(output_dir, "Module")
    os.makedirs(output_dir, exist_ok=True)

    contents = template
    contents = contents.replace("{{org_name}}", _options["org_name"])
    contents = contents.replace("{{module_name}}", _options["module_name"])
    output_path = os.path.join(output_dir, "DummyView.cs")
    writer.write(output_path, contents, False)
