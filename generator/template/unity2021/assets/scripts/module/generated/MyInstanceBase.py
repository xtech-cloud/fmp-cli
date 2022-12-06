import os
import uuid
from generator.template.utility import writer

template = """
//*************************************************************************************
//   !!! Generated by the fmp-cli {{version}}.  DO NOT EDIT!
//*************************************************************************************

using System.IO;
using System.Threading;
using System.Threading.Tasks;
using System.Collections.Generic;
using UnityEngine;
using LibMVCS = XTC.FMP.LIB.MVCS;
using {{org_name}}.FMP.MOD.{{module_name}}.LIB.Bridge;
using {{org_name}}.FMP.MOD.{{module_name}}.LIB.MVCS;
using {{org_name}}.FMP.MOD.{{module_name}}.LIB.Proto;

namespace {{org_name}}.FMP.MOD.{{module_name}}.LIB.Unity
{
    public class MyInstanceBase
    {
        public string uid { get; private set; }
        public GameObject rootUI { get; private set; }
        public GameObject rootAttachments { get; private set; }

        /// <summary>
        /// 内容对象池，管理从内容目录中加载到内存中的对象
        /// </summary>
        /// <remarks>
        /// 在实例打开(Open)时准备，在实例关闭(Close)时清理
        /// </remarks>
        public ObjectsPool contentObjectsPool { get; private set; }

        /// <summary>
        /// 主题对象池，管理从主题目录加载到内存中的对象
        /// </summary>
        /// <remarks>
        /// 在实例创建(Create)时准备，在实例删除(Delete)时清理
        /// </remarks>
        public ObjectsPool themeObjectsPool { get; private set; }

        /// <summary>
        /// 模块预加载阶段，预加载到内存中的对象的列表的副本
        /// </summary>
        /// <remarks>
        /// key: 对象的检索路径
        /// object: 对象的实例
        /// </remarks>
        public Dictionary<string, object> preloadsRepetition { get; set; }
        

{{member_blocks}}

        protected MyEntryBase entry_ { get; set; }
        protected LibMVCS.Logger logger_ { get; set; }
        protected MyConfig config_ { get; set; }
        protected MyCatalog catalog_ { get; set; }
        protected MyConfig.Style style_ { get; set; }
        protected Dictionary<string, LibMVCS.Any> settings_ { get; set; }
        protected MonoBehaviour mono_ {get;set;}

        public MyInstanceBase(string _uid, string _style, MyConfig _config, MyCatalog _catalog, LibMVCS.Logger _logger, Dictionary<string, LibMVCS.Any> _settings, MyEntryBase _entry, MonoBehaviour _mono, GameObject _rootAttachments)
        {
            uid = _uid;
            config_ = _config;
            catalog_ = _catalog;
            logger_ = _logger;
            settings_ = _settings;
            entry_ = _entry;
            mono_ = _mono;
            rootAttachments = _rootAttachments;
            foreach(var style in config_.styles)
            {
                if (style.name.Equals(_style))
                {
                    style_ = style;
                    break;
                }
            }
            contentObjectsPool = new ObjectsPool(uid + ".Content", logger_);
            themeObjectsPool = new ObjectsPool(uid + ".Theme", logger_);
        }

        /// <summary>
        /// 实例化UI
        /// </summary>
        /// <param name="_instanceUI">ui的实例模板</param>
        /// <param name="_parent">父对象</param>
        public void InstantiateUI(GameObject _instanceUI, Transform _parent)
        {
            rootUI = Object.Instantiate(_instanceUI, _parent);
            rootUI.name = uid;
        }

        public void SetupBridges()
        {
{{dynamic_register_blocks}}
        }

        /// <summary>
        /// 当被显示时
        /// </summary>
        public virtual void HandleShowed()
        {
            rootUI.gameObject.SetActive(true);
        }

        /// <summary>
        /// 当被隐藏时
        /// </summary>
        public virtual void HandleHided()
        {
            rootUI.gameObject.SetActive(false);
        }

        /// <summary>
        /// 将目标按锚点在父对象中对齐
        /// </summary>
        /// <param name="_target">目标</param>
        /// <param name="_anchor">锚点</param>
        protected void alignByAncor(Transform _target, MyConfig.Anchor _anchor)
        {
            if (null == _target)
                return;
            RectTransform rectTransform = _target.GetComponent<RectTransform>();
            if (null == rectTransform)
                return;

            RectTransform parent = _target.transform.parent.GetComponent<RectTransform>();
            float marginH = 0;
            if (_anchor.marginH.EndsWith("%"))
            {
                float margin = 0;
                float.TryParse(_anchor.marginH.Replace("%", ""), out margin);
                marginH = (margin / 100.0f) * (parent.rect.width / 2);
            }
            else
            {
                float.TryParse(_anchor.marginH, out marginH);
            }

            float marginV = 0;
            if (_anchor.marginV.EndsWith("%"))
            {
                float margin = 0;
                float.TryParse(_anchor.marginV.Replace("%", ""), out margin);
                marginV = (margin / 100.0f) * (parent.rect.height / 2);
            }
            else
            {
                float.TryParse(_anchor.marginV, out marginV);
            }

            Vector2 anchorMin = new Vector2(0.5f, 0.5f);
            Vector2 anchorMax = new Vector2(0.5f, 0.5f);
            Vector2 pivot = new Vector2(0.5f, 0.5f);
            if (_anchor.horizontal.Equals("left"))
            {
                anchorMin.x = 0;
                anchorMax.x = 0;
                pivot.x = 0;
            }
            else if (_anchor.horizontal.Equals("right"))
            {
                anchorMin.x = 1;
                anchorMax.x = 1;
                pivot.x = 1;
                marginH *= -1;
            }

            if (_anchor.vertical.Equals("top"))
            {
                anchorMin.y = 1;
                anchorMax.y = 1;
                pivot.y = 1;
                marginV *= -1;
            }
            else if (_anchor.vertical.Equals("bottom"))
            {
                anchorMin.y = 0;
                anchorMax.y = 0;
                pivot.y = 0;
            }

            Vector2 position = new Vector2(marginH, marginV);
            rectTransform.anchorMin = anchorMin;
            rectTransform.anchorMax = anchorMax;
            rectTransform.pivot = pivot;
            rectTransform.anchoredPosition = position;
            rectTransform.sizeDelta = new Vector2(_anchor.width, _anchor.height);
        }


        /// <summary>
        /// 从主题目录中加载纹理
        /// </summary>
        /// <param name="_file">文件相对于 themes/{ModuleName} 的路径</param>
        protected void loadTextureFromTheme(string _file, System.Action<Texture2D> _onFinish, System.Action _onError)
        {
            string path = settings_["path.themes"].AsString();
            path = System.IO.Path.Combine(path, MyEntryBase.ModuleName);
            string filefullpath = System.IO.Path.Combine(path, _file);
            themeObjectsPool.LoadTexture(filefullpath, null, _onFinish, _onError);
        }

        /// <summary>
        /// 从主题目录中加载文本
        /// </summary>
        /// <param name="_file">文件相对于 themes/{ModuleName} 的路径</param>
        protected void loadTextFromTheme(string _file, System.Action<byte[]> _onFinish, System.Action _onError)
        {
            string path = settings_["path.themes"].AsString();
            path = System.IO.Path.Combine(path, MyEntryBase.ModuleName);
            string filefullpath = System.IO.Path.Combine(path, _file);
            themeObjectsPool.LoadText(filefullpath, null, _onFinish, _onError);
        }
        
        /// <summary>
        /// 从主题目录加载音频
        /// </summary>
        /// <param name="_file">文件相对于 themes/{ModuleName} 的路径</param>
        protected void loadAudioFromTheme(string _file, System.Action<AudioClip> _onFinish, System.Action _onError)
        {
            string path = settings_["path.themes"].AsString();
            path = System.IO.Path.Combine(path, MyEntryBase.ModuleName);
            string filefullpath = System.IO.Path.Combine(path, _file);
            themeObjectsPool.LoadAudioClip(filefullpath, null, _onFinish, _onError);
        }

{{method_blocks}}

    }
}
"""

template_members = """
        public I{{service}}ViewBridge viewBridge{{service}} { get; set; }
"""

template_dynamic_register_blocks = """
            var facade{{service}} = entry_.getDynamic{{service}}Facade(uid);
            var bridge{{service}} = new {{service}}UiBridge();
            bridge{{service}}.logger = logger_;
            facade{{service}}.setUiBridge(bridge{{service}});
            viewBridge{{service}} = facade{{service}}.getViewBridge() as I{{service}}ViewBridge;
"""

template_method = """
        protected virtual void submit{{service}}{{rpc}}({{request}} _request)
        {
            var dto = new {{request}}DTO(_request);
            SynchronizationContext context = SynchronizationContext.Current;
            Task.Run(async () =>
            {
                try
                {
                    var reslut = await viewBridge{{service}}.On{{rpc}}Submit(dto, context);
                    if (!LibMVCS.Error.IsOK(reslut))
                    {
                        logger_.Error(reslut.getMessage());
                    }
                }
                catch (System.Exception ex)
                {
                    logger_.Exception(ex);
                }
            });
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

    member_blocks = ""
    method_blocks = ""
    dynamic_register_blocks = ""
    services = _options["services"]
    for service in services.keys():
        dynamic_register_block = template_dynamic_register_blocks
        dynamic_register_block = dynamic_register_block.replace("{{service}}", service)
        dynamic_register_blocks = dynamic_register_blocks + dynamic_register_block
        member_blocks = member_blocks + template_members.replace("{{service}}", service)
        for rpc_name in services[service].keys():
            rpc_map = services[service][rpc_name]
            method_block = template_method
            method_block = method_block.replace("{{service}}", service)
            method_block = method_block.replace("{{rpc}}", rpc_name)
            method_block = method_block.replace("{{request}}", rpc_map[0])
            method_blocks = method_blocks + method_block

    contents = template
    contents = contents.replace("{{org_name}}", _options["org_name"])
    contents = contents.replace("{{module_name}}", _options["module_name"])
    contents = contents.replace("{{version}}", _options["version"])
    contents = contents.replace("{{member_blocks}}", member_blocks)
    contents = contents.replace("{{method_blocks}}", method_blocks)
    contents = contents.replace("{{dynamic_register_blocks}}", dynamic_register_blocks)
    output_path = os.path.join(output_dir, "MyInstanceBase.cs")
    writer.write(output_path, contents, True)
