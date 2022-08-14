import os
import uuid
from generator.template.utility import writer

template = """
using System.Threading.Tasks;
using UnityEngine;
using UnityEngine.UI;
using LibMVCS = XTC.FMP.LIB.MVCS;
using {{org_name}}.FMP.MOD.{{module_name}}.LIB.Proto;
using {{org_name}}.FMP.MOD.{{module_name}}.LIB.MVCS;

namespace {{org_name}}.FMP.MOD.{{module_name}}.LIB.Unity
{
    /// <summary>
    /// 实例类
    /// </summary>
    public class MyInstance : MyInstanceBase
    {
        private MyConfig.Style style_ { get; set; }

        /// <summary>
        /// 应用样式
        /// </summary>
        /// <param name="_style">样式</param>
        public void ApplyStyle(MyConfig.Style _style)
        {
            style_ = _style;
        }

        /// <summary>
        /// 当被创建时
        /// </summary>
        public void HandleCreated()
        {
        }

        /// <summary>
        /// 当被删除时
        /// </summary>
        public void HandleDeleted()
        {
        }

        /// <summary>
        /// 当被打开时
        /// </summary>
        public void HandleOpened()
        {
            rootUI.gameObject.SetActive(true);
        }

        /// <summary>
        /// 当被关闭时
        /// </summary>
        public void HandleClosed()
        {
            rootUI.gameObject.SetActive(false);
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
    output_path = os.path.join(output_dir, "MyInstance.cs")
    writer.write(output_path, contents, False)
