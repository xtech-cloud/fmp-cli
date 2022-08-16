import os
from typing import Dict, List, Tuple
from generator.template.utility import writer

template = """
//*************************************************************************************
//   !!! Generated by the fmp-cli {{version}}.  DO NOT EDIT!
//*************************************************************************************

using System.Threading;
using System.Threading.Tasks;
using Grpc.Net.Client;
using XTC.FMP.LIB.MVCS;
using {{org}}.FMP.MOD.{{module}}.LIB.Proto;

namespace {{org}}.FMP.MOD.{{module}}.LIB.MVCS
{
    /// <summary>
    /// {{service}}服务层基类
    /// </summary>
    public class {{service}}ServiceBase : Service
    {
        public {{service}}ServiceMock mock { get; set; } = new {{service}}ServiceMock();
    
        /// <summary>
        /// 带uid参数的构造函数
        /// </summary>
        /// <param name="_uid">实例化后的唯一识别码</param>
        /// <param name="_gid">直系的组的ID</param>
        public {{service}}ServiceBase(string _uid, string _gid) : base(_uid)
        {
            gid_ = _gid;
        }

        /// <summary>
        /// 注入GRPC通道
        /// </summary>
        /// <param name="_channel">GRPC通道</param>
        public void InjectGrpcChannel(GrpcChannel? _channel)
        {
            grpcChannel_ = _channel;
        }

{{method_blocks}}

        /// <summary>
        /// 获取直系数据层
        /// </summary>
        /// <returns>数据层</returns>
        protected {{service}}Model? getModel()
        {
            if(null == model_)
                model_ = findModel({{service}}Model.NAME + "." + gid_) as {{service}}Model;
            return model_;
        }

        /// <summary>
        /// 获取GRPC客户端
        /// </summary>
        /// <returns>GRPC客户端</returns>
        protected {{service}}.{{service}}Client? getGrpcClient()
        {
            if (null == grpcChannel_)
                return null;

            if(null == client{{service}}_)
            {
                client{{service}}_ = new {{service}}.{{service}}Client(grpcChannel_);
            }
            return client{{service}}_;
        }

        /// <summary>
        /// 直系的MVCS的四个组件的组的ID
        /// </summary>
        protected string gid_ = "";

        /// <summary>
        /// GRPC客户端
        /// </summary>
        protected {{service}}.{{service}}Client? client{{service}}_;

        /// <summary>
        /// GRPC通道
        /// </summary>
        protected GrpcChannel? grpcChannel_;

        /// <summary>
        /// 直系数据层
        /// </summary>
        private {{service}}Model? model_;
    }

}
"""

template_method = """
        /// <summary>
        /// 调用{{rpc}}
        /// </summary>
        /// <param name="_request">{{rpc}}的请求</param>
        /// <returns>错误</returns>
        public virtual async Task<Error> Call{{rpc}}({{request}}? _request, SynchronizationContext? _context)
        {
            getLogger()?.Trace("Call {{rpc}} ...");
            if (null == _request)
            {
                return Error.NewNullErr("parameter:_request is null");
            }

            {{response}}? response = null;
            if (null != mock.Call{{rpc}}Delegate)
            {
                getLogger()?.Trace("use mock ...");
                response = await mock.Call{{rpc}}Delegate(_request);
            }
            else
            {
                var client = getGrpcClient();
                if (null == client)
                {
                    return await Task.FromResult(Error.NewNullErr("client is null"));
                }
                response = await client.{{rpc}}Async(_request);
            }

            getModel()?.UpdateProto{{rpc}}(response, _context);
            return Error.OK;
        }
"""


def generate(_options, _outputdir: str):
    org_name = _options["org_name"]
    module_name = _options["module_name"]
    services = _options["services"]
    for service in services.keys():
        method_blocks = ""
        for rpc_name in services[service].keys():
            rpc_map = services[service][rpc_name]
            method_block = (
                template_method.replace("{{service}}", service)
                .replace("{{rpc}}", rpc_name)
                .replace("{{request}}", rpc_map[0])
                .replace("{{response}}", rpc_map[1])
            )
            method_blocks = method_blocks + method_block
        contents = (
            template.replace("{{org}}", org_name)
            .replace("{{module}}", module_name)
            .replace("{{service}}", service)
            .replace("{{method_blocks}}", method_blocks)
        )
        contents = contents.replace("{{version}}", _options["version"])
        filepath = os.path.join(_outputdir, "{}ServiceBase.cs".format(service))
        writer.write(filepath, contents, True)
