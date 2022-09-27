import os
import uuid
from generator.template.utility import writer

template = """
//*************************************************************************************
//   !!! Generated by the fmp-cli {{version}}.  DO NOT EDIT!
//*************************************************************************************

using System.Collections.Generic;

namespace {{org_name}}.FMP.MOD.{{module_name}}.LIB.Unity
{
    /// <summary>
    /// 目录类的基类
    /// </summary>
    public class MyCatalogBase
    {
        /// <summary>
        /// 段
        /// </summary>
        public class Section
        {
            /// <summary>
            /// 段的名称
            /// </summary>
            public string name { get; set; } = "";

            /// <summary>
            /// 段的路径，支持/字符分割
            /// </summary>
            public string path { get; set; } = "";

            /// <summary>
            /// 实例
            /// </summary>
            public string[] instanceS { get; set; } = new string[0];

            /// <summary>
            /// 内容列表
            /// </summary>
            /// <remarks>
            /// 支持正则表达式
            /// </remarks>
            public string[] contentS { get; set; } = new string[0];

            /// <summary>
            /// 键值对
            /// </summary>
            public Dictionary<string, string> kvS { get; set; } = new Dictionary<string, string>();
        }

        public Section[] sectionS { get; set; } = new Section[0];
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
    output_dir = os.path.join(output_dir, "_Generated_")
    os.makedirs(output_dir, exist_ok=True)

    contents = template
    contents = contents.replace("{{org_name}}", _options["org_name"])
    contents = contents.replace("{{module_name}}", _options["module_name"])
    contents = contents.replace("{{version}}", _options["version"])
    output_path = os.path.join(output_dir, "MyCatalogBase.cs")
    writer.write(output_path, contents, True)
