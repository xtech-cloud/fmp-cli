import os
import uuid
from generator.template.utility import writer

template = """
using System;
using LibMVCS = XTC.FMP.LIB.MVCS;

namespace {{org_name}}.FMP.MOD.{{module_name}}.LIB.Unity
{
    /// <summary>
    /// 虚拟数据
    /// </summary>
    public class DummyModel : LibMVCS.Model
    {
        public const string NAME = "{{org_name}}.FMP.MOD.{{module_name}}.LIB.Unity.DummyModel";

        public class DummyStatus : LibMVCS.Model.Status
        {
            public const string NAME = "{{org_name}}.FMP.MOD.{{module_name}}.LIB.Unity.DummyStatus";
        }

        public DummyModel(string _uid) : base(_uid)
        {
        }

        protected override void preSetup()
        {
            LibMVCS.Error err;
            status_ = spawnStatus<DummyStatus>(DummyStatus.NAME, out err);
            if(!LibMVCS.Error.IsOK(err))
            {
                getLogger().Error(err.getMessage());
            }
        }

        protected override void postDismantle()
        {
            LibMVCS.Error err;
            killStatus(DummyStatus.NAME, out err);
            if(!LibMVCS.Error.IsOK(err))
            {
                getLogger().Error(err.getMessage());
            }
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
    output_path = os.path.join(output_dir, "DummyModel.cs")
    writer.write(output_path, contents, False)
