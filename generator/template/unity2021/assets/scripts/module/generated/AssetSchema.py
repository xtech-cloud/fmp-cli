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
    /// 资源包的meta结构
    /// </summary>
    public class BundleMetaSchema
    {
        /// <summary>
        /// 路径是否匹配表达式
        /// </summary>
        /// <param name="_contentUri">内容的短路径</param>
        /// <param name="_pattern">正则表达式</param>
        /// <returns>是否匹配</returns>
        public static bool IsMatch(string _contentUri, string _pattern)
        {
            Regex regex = new Regex(_pattern);
            return regex.IsMatch(_contentUri);
        }

        /// <summary>
        /// 内容名称的列表
        /// </summary>
        public string[] contentS { get; set; } = new string[0];
    } //class

    /// <summary>
    /// 资源内容的meta结构
    /// </summary>
    public class ContentMetaSchema
    {
    } //class
} //namespace

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
    output_path = os.path.join(output_dir, "AssetSchema.cs")
    writer.write(output_path, contents, True)
