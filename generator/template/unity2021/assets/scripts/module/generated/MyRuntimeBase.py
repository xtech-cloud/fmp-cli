import os
import uuid
from generator.template.utility import writer

template = """
//*************************************************************************************
//   !!! Generated by the fmp-cli {{version}}.  DO NOT EDIT!
//*************************************************************************************

using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using LibMVCS = XTC.FMP.LIB.MVCS;

namespace {{org_name}}.FMP.MOD.{{module_name}}.LIB.Unity
{
    /// <summary>
    /// 运行时基类
    /// </summary>
    ///<remarks>
    /// 存储模块运行时创建的对象
    ///</remarks>
    public abstract class MyRuntimeBase
    {
        /// <summary>
        /// ui的根对象
        /// </summary>
        public GameObject rootUI { get; private set; }

        /// <summary>
        /// 附件的根对象
        /// </summary>
        public GameObject rootAttachment { get; private set; }

        /// <summary>
        /// ui的实例对象
        /// </summary>
        public GameObject instanceUI { get; private set; }

        /// <summary>
        /// 实例表，键为实例的uid
        /// </summary>
        public Dictionary<string, MyInstance> instances { get; private set; } = new Dictionary<string, MyInstance>();

        protected MonoBehaviour mono_ { get; set; }
        protected MyConfig config_ { get; set; }
        protected Dictionary<string, LibMVCS.Any> settings_ { get; set; }
        protected LibMVCS.Logger logger_ { get; set; }
        protected MyEntryBase entry_ { get; set; }

        public MyRuntimeBase(MonoBehaviour _mono, MyConfig _config, Dictionary<string, LibMVCS.Any> _settings, LibMVCS.Logger _logger, MyEntryBase _entry)
        {
            mono_ = _mono;
            config_ = _config;
            settings_= _settings;
            logger_ = _logger;
            entry_ = _entry; 
        }

        /// <summary>
        /// 处理从UAB中实例化的根对象
        /// </summary>
        /// <param name="_root">根对象</param>
        /// <param name="_uiSlot">ui的挂载槽</param>
        public virtual void ProcessRoot(GameObject _root, Transform _uiSlot)
        {
            string attachmentsRootName = string.Format("[Attachments_Root_({0})]", MyEntry.ModuleName);
            var attachmentsRoot = _root.transform.Find(attachmentsRootName);
            if (null != attachmentsRoot)
            {
                rootAttachment = attachmentsRoot.gameObject;
                rootAttachment.transform.SetParent(null);
            }

            string uiRootName = string.Format("Canvas/[UI_Root_({0})]", MyEntry.ModuleName);
            var uiRoot = _root.transform.Find(uiRootName);
            if (null == uiRoot)
            {
                logger_.Error("{0} not found", uiRoot);
                return;
            }

            // 将ui挂载到指定的槽上
            rootUI = uiRoot.gameObject;
            rootUI.transform.SetParent(_uiSlot);
            // 挂载后重置参数
            rootUI.transform.localScale = Vector3.one;
            rootUI.transform.localRotation = Quaternion.identity;
            rootUI.transform.localPosition = Vector3.zero;
            RectTransform rt = rootUI.GetComponent<RectTransform>();
            rt.sizeDelta = Vector2.zero;
            rt.anchoredPosition = Vector2.zero;
            rootUI.SetActive(config_.ui.visible);
            // 销毁根对象
            GameObject.Destroy(_root);
            // 查找实例的对象
            var rInstance = rootUI.transform.Find("instance");
            if (null == rInstance)
            {
                logger_.Error("{0}/instance is required!", _root.name);
                return;
            }
            instanceUI = rInstance.gameObject;
            // 不显示模板
            instanceUI.gameObject.SetActive(false);
        }


        /// <summary>
        /// 创建实例
        /// </summary>
        /// <param name="_uid">实例的uid</param>
        /// <param name="_style">使用的样式名</param>
        /// <returns></returns>
        public virtual void CreateInstanceAsync(string _uid, string _style, System.Action<MyInstance> _onFinish)
        {
            mono_.StartCoroutine(createInstanceAsync(_uid, _style, _onFinish));
        }

        /// <summary>
        /// 删除实例
        /// </summary>
        /// <param name="_uid">实例的uid</param>
        public virtual void DeleteInstanceAsync(string _uid)
        {
            mono_.StartCoroutine(deleteInstanceAsync(_uid));
        }


        /// <summary>
        /// 打开实例
        /// </summary>
        /// <param name="_uid">实例的uid</param>
        /// <param name="_source">内容的源类型</param>
        /// <param name="_uri">内容的地址</param>
        /// <param name="_delay">延时时间，单位秒</param>
        public virtual void OpenInstanceAsync(string _uid, string _source, string _uri, float _delay)
        {
            mono_.StartCoroutine(openInstanceAsync(_uid, _source, _uri, _delay));
        }

        /// <summary>
        /// 关闭实例
        /// </summary>
        /// <param name="_uid">实例的uid</param>
        /// <param name="_delay">延时时间，单位秒</param>
        public virtual void CloseInstanceAsync(string _uid, float _delay)
        {
            mono_.StartCoroutine(closeInstanceAsync(_uid, _delay));
        }

        protected IEnumerator delayDo(float _time, System.Action _action)
        {
            if (0 == _time)
                yield return new WaitForEndOfFrame();
            else
                yield return new WaitForSeconds(_time);
            _action();
        }

        private IEnumerator createInstanceAsync(string _uid, string _style, System.Action<MyInstance> _onFinish)
        {
            logger_.Debug("create instance of {0}, uid is {1}, style is {2}", MyEntryBase.ModuleName, _uid, _style);
            // 延时一帧执行，在发布消息时不能动态注册
            yield return new WaitForEndOfFrame();

            MyInstance instance;
            if (instances.TryGetValue(_uid, out instance))
            {
                logger_.Error("instance is exists");
                yield break;
            }

            instance = new MyInstance(_uid, _style, config_, logger_, settings_, entry_, mono_, rootAttachment);
            instances[_uid] = instance;
            instance.InstantiateUI(instanceUI);
            instance.ApplyStyle();
            instance.HandleCreated();
            // 动态注册直系的MVCS
            entry_.DynamicRegister(_uid, logger_);
            instance.SetupBridges();
            _onFinish(instance);
        }

        private IEnumerator deleteInstanceAsync(string _uid)
        {
            logger_.Debug("delete instance of {0}, uid is {1}", MyEntryBase.ModuleName, _uid);
            // 延时一帧执行，在发布消息时不能动态注销
            yield return new WaitForEndOfFrame();

            MyInstance instance;
            if (!instances.TryGetValue(_uid, out instance))
            {
                logger_.Error("instance not found");
                yield break;
            }

            instance.HandleDeleted();
            GameObject.Destroy(instance.rootUI);
            instances.Remove(_uid);

            // 动态注销直系的MVCS
            entry_.DynamicCancel(_uid, logger_);
        }

        private IEnumerator openInstanceAsync(string _uid, string _source, string _uri, float _delay)
        {
            logger_.Debug("open instance of {0}, uid is {1}", MyEntryBase.ModuleName, _uid);

            MyInstance instance;
            if (!instances.TryGetValue(_uid, out instance))
            {
                logger_.Error("instance not found");
                yield break;
            }
            yield return new WaitForSeconds(_delay);
            instance.HandleOpened(_source, _uri);
        }

        private IEnumerator closeInstanceAsync(string _uid, float _delay)
        {
            logger_.Debug("close instance of {0}, uid is {1}", MyEntryBase.ModuleName, _uid);
            MyInstance instance;
            if (!instances.TryGetValue(_uid, out instance))
            {
                logger_.Error("instance not found");
                yield break;
            }
            yield return new WaitForSeconds(_delay);
            instance.HandleClosed();
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
    output_dir = os.path.join(output_dir, "_Generated_")
    os.makedirs(output_dir, exist_ok=True)

    contents = template
    contents = contents.replace("{{org_name}}", _options["org_name"])
    contents = contents.replace("{{module_name}}", _options["module_name"])
    contents = contents.replace("{{version}}", _options["version"])
    output_path = os.path.join(output_dir, "MyRuntimeBase.cs")
    writer.write(output_path, contents, True)
