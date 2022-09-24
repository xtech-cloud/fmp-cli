import os
import uuid
from generator.template.utility import writer

template = """
using UnityEngine;

/// <summary>
/// 根程序类
/// </summary>
/// <remarks>
/// 不参与模块编译，仅用于在编辑器中开发调试
/// </remarks>
public class Root : RootBase
{
    private void Awake()
    {
        doAwake();
    }

    private void Start()
    {
        entry_.__DebugPreload(exportRoot);
    }

    private void OnDestroy()
    {
        doDestroy();
    }

    private void OnGUI()
    {
        if (GUI.Button(new Rect(0, 0, 60, 30), "Create"))
        {
            entry_.__DebugCreate("test", "default");
        }

        if (GUI.Button(new Rect(0, 30, 60, 30), "Open"))
        {
            entry_.__DebugOpen("test", "file", "", 0.5f);
        }

        if (GUI.Button(new Rect(0, 60, 60, 30), "Show"))
        {
            entry_.__DebugShow("test", 0.5f);
        }

        if (GUI.Button(new Rect(0, 90, 60, 30), "Hide"))
        {
            entry_.__DebugHide("test", 0.5f);
        }

        if (GUI.Button(new Rect(0, 120, 60, 30), "Close"))
        {
            entry_.__DebugClose("test", 0.5f);
        }

        if (GUI.Button(new Rect(0, 150, 60, 30), "Delete"))
        {
            entry_.__DebugDelete("test");
        }
    }
}

"""

template_meta = """fileFormatVersion: 2
guid: 7e78cb5e6a443de41a50e65b8d1a169e
MonoImporter:
  externalObjects: {}
  serializedVersion: 2
  defaultReferences: []
  executionOrder: 0
  icon: {instanceID: 0}
  userData: 
  assetBundleName: 
  assetBundleVariant:  
"""

def generate(_options, _outputdir: str):
    output_dir = os.path.join(_outputdir, "Assets")
    os.makedirs(output_dir, exist_ok=True)
    output_dir = os.path.join(output_dir, "Scripts")
    os.makedirs(output_dir, exist_ok=True)

    contents = template
    output_path = os.path.join(output_dir, "Root.cs")
    writer.write(output_path, contents, False)

    contents = template_meta
    output_path = os.path.join(output_dir, "Root.cs.meta")
    writer.write(output_path, contents, False)
