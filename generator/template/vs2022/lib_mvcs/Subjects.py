import os
from typing import Dict, List, Tuple
from generator.template.utility import writer

template = """
namespace {{org}}.FMP.MOD.{{module}}.LIB.MVCS
{
    public class Subjects
    {
        /// <summary>
        /// 示例
        /// </summary>
        /// <example>
        /// var data = new Dictionary<string, object>();
        /// data["uid"] = "default";
        /// model.Publish(/{{org}}/{{module}}/Sample, data);
        /// </example>
        public const string Sample = "/{{org}}/{{module}}/Sample";
    }
}
"""

def generate(_options, _outputdir: str):
    org_name = _options["org_name"]
    module_name = _options["module_name"]
    # 生成项目文件
    contents = (
        template.replace("{{org}}", org_name)
        .replace("{{module}}", module_name)
    )
    filepath = os.path.join(_outputdir, "Subjects.cs")
    writer.write(filepath, contents, False)
