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
    /// 内容类的基类
    /// </summary>
    public class MyContentBase
    {
        /// <summary>
        /// 包名
        /// </summary>
        public string bundle { get; set; } = "";

        /// <summary>
        /// 别名
        /// </summary>
        /// <remarks>
        /// 可用于首字母检索，以及显示在菜单中
        /// </remarks>
        public string alias { get; set; } = "";

        /// <summary>
        /// 别名的多国语言
        /// </summary>
        public Dictionary<string, string> alias_i18nS { get; set; } = new Dictionary<string, string>();

        /// <summary>
        /// 标题
        /// </summary>
        public string title { get; set; } = "";

        /// <summary>
        /// 标题的多国语言
        /// </summary>
        public Dictionary<string, string> title_i18n { get; set; } = new Dictionary<string, string>();

        /// <summary>
        /// 主题
        /// </summary>
        public string topic { get; set; } = "";

        /// <summary>
        /// 主题的多国语言
        /// </summary>
        public Dictionary<string, string> topic_i18nS { get; set; } = new Dictionary<string, string>();

        /// <summary>
        /// 题注
        /// </summary>
        public string caption { get; set; } = "";

        /// <summary>
        /// 题注的多国语言
        /// </summary>
        public Dictionary<string, string> caption_i18nS { get; set; } = new Dictionary<string, string>();

        /// <summary>
        /// 描述
        /// </summary>
        public string description { get; set; } = "";

        /// <summary>
        /// 描述的多国语言
        /// </summary>
        public Dictionary<string, string> description_i18nS { get; set; } = new Dictionary<string, string>();

        /// <summary>
        /// 键值对
        /// </summary>
        public Dictionary<string, string> kvS { get; set; } = new Dictionary<string, string>();
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
    output_path = os.path.join(output_dir, "MyContentBase.cs")
    writer.write(output_path, contents, True)