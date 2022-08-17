import os
from generator.template.utility import writer

template = """
//*************************************************************************************
//   !!! Generated by the fmp-cli {{version}}.  DO NOT EDIT!
//*************************************************************************************

using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using LibMVCS = XTC.FMP.LIB.MVCS;

namespace {{org_name}}.FMP.MOD.{{module_name}}.LIB.Unity
{
    public class ObjectsPoolMonoBehaviour : MonoBehaviour
    {

    }

    public class ObjectsPool
    {
        protected string uid_ { get; set; }
        protected LibMVCS.Logger logger_ { get; set; }

        protected MonoBehaviour mono_;

        /// <summary>
        /// 加载到内存的对象
        /// </summary>
        protected List<UnityEngine.Object> objects = new List<UnityEngine.Object>();

        /// <summary>
        /// 加载协程的列表，键为协程的独占编号
        /// </summary>
        private Dictionary<string, Coroutine> exclusiveCoroutines = new Dictionary<string, Coroutine>();

        public ObjectsPool(string _uid, LibMVCS.Logger _logger)
        {
            uid_ = _uid;
            logger_ = _logger;
        }

        /// <summary>
        /// 准备
        /// </summary>
        public void Prepare()
        {
            if (null != mono_)
                return;
            var goMono = new GameObject(string.Format("[ObjectsPool_{0}_{1}]", MyEntryBase.ModuleName, uid_));
            mono_ = goMono.AddComponent<ObjectsPoolMonoBehaviour>();
        }

        /// <summary>
        /// 清理
        /// </summary>
        public void Dispose()
        {
            if (null == mono_)
                return;
            mono_.StopAllCoroutines();
            GameObject.Destroy(mono_.gameObject);
            mono_ = null;

            logger_.Trace("ready to dispose {0} Objects", objects.Count);
            foreach (var obj in objects)
            {
                UnityEngine.Object.Destroy(obj);
            }
            Resources.UnloadUnusedAssets();
            objects.Clear();
        }

        /// <summary>
        /// 加载AduioClip
        /// </summary>
        /// <param name="_file">文件地址</param>
        /// <param name="_exclusiveNumber">独占编号，先终止正在运行的指定编号的协程, null为使用非独占模式</param>
        /// <param name="_onFinish">完成的回调</param>
        public void LoadAudioClip(string _file, string _exclusiveNumber, Action<AudioClip> _onFinish)
        {
            Coroutine coroutine;
            if (null != _exclusiveNumber)
            {
                if (exclusiveCoroutines.TryGetValue(_exclusiveNumber, out coroutine))
                {
                    mono_.StopCoroutine(coroutine);
                    exclusiveCoroutines.Remove(_exclusiveNumber);
                }
            }
            coroutine = mono_.StartCoroutine(loadAudioClip(_file, _exclusiveNumber, _onFinish));
            if(null != _exclusiveNumber)
            {
                exclusiveCoroutines[_exclusiveNumber] = coroutine;
            }
        }

        /// <summary>
        /// 加载Texture
        /// </summary>
        /// <param name="_file"></param>
        /// <param name="_onFinish"></param>
        public void LoadTexture(string _file, string _exclusiveNumber, Action<Texture> _onFinish)
        {
            Coroutine coroutine;
            if (null != _exclusiveNumber)
            {
                if (exclusiveCoroutines.TryGetValue(_exclusiveNumber, out coroutine))
                {
                    mono_.StopCoroutine(coroutine);
                    exclusiveCoroutines.Remove(_exclusiveNumber);
                }
            }
            coroutine = mono_.StartCoroutine(loadTexture(_file, _exclusiveNumber, _onFinish));
            if(null != _exclusiveNumber)
            {
                exclusiveCoroutines[_exclusiveNumber] = coroutine;
            }
        }

        private IEnumerator loadAudioClip(string _file, string _exclusiveNumber, Action<AudioClip> _onFinish)
        {
            logger_.Trace("ready to load AduioClip from {0}", _file);
            using (var uwr = UnityWebRequestMultimedia.GetAudioClip(_file, AudioType.MPEG))
            {
                yield return uwr.SendWebRequest();
                if (uwr.result == UnityWebRequest.Result.ProtocolError)
                {
                    logger_.Error(uwr.error);
                    yield break;
                }
                AudioClip clip = DownloadHandlerAudioClip.GetContent(uwr);
                if (!objects.Contains(clip))
                    objects.Add(clip);
                logger_.Trace("load AduioClip:{0} success", _file);
                logger_.Trace("Currently, ObjectsPool has {0} Objects", objects.Count);
                if(null != _exclusiveNumber && exclusiveCoroutines.ContainsKey(_exclusiveNumber))
                {
                    exclusiveCoroutines.Remove(_exclusiveNumber);
                }
                _onFinish(clip);
            }
        }

        private IEnumerator loadTexture(string _file, string _exclusiveNumber, Action<Texture> _onFinish)
        {
            logger_.Trace("ready to load Texture from {0}", _file);
            using (var uwr = new UnityWebRequest(_file))
            {
                DownloadHandlerTexture handler = new DownloadHandlerTexture(true);
                uwr.downloadHandler = handler;
                yield return uwr.SendWebRequest();
                if (uwr.result == UnityWebRequest.Result.ProtocolError)
                {
                    logger_.Error(uwr.error);
                    yield break;
                }
                Texture2D texture = handler.texture;
                if (!objects.Contains(texture))
                    objects.Add(texture);
                logger_.Trace("load Texture:{0} success", _file);
                logger_.Trace("Currently, ObjectsPool has {0} Objects", objects.Count);
                if(null != _exclusiveNumber && exclusiveCoroutines.ContainsKey(_exclusiveNumber))
                {
                    exclusiveCoroutines.Remove(_exclusiveNumber);
                }
                _onFinish(texture);
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
    output_dir = os.path.join(output_dir, "_Generated_")
    os.makedirs(output_dir, exist_ok=True)

    contents = template
    contents = contents.replace("{{org_name}}", _options["org_name"])
    contents = contents.replace("{{module_name}}", _options["module_name"])
    contents = contents.replace("{{version}}", _options["version"])
    output_path = os.path.join(output_dir, "ObjectsPool.cs")
    writer.write(output_path, contents, True)
