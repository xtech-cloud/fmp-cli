import os
import uuid
from generator.template.utility import writer

template = """

using System.Collections.Generic;
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

        public MyInstance(string _uid, string _style, MyConfig _config, LibMVCS.Logger _logger, Dictionary<string, LibMVCS.Any> _settings, MyEntryBase _entry, MonoBehaviour _mono, GameObject _rootAttachments)
            : base(_uid, _style, _config, _logger, _settings, _entry, _mono, _rootAttachments)
        {
        }

        /// <summary>
        /// 应用样式
        /// </summary>
        public void ApplyStyle()
        {
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
        public void HandleOpened(string _source, string _uri)
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
