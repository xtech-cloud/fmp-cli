import os
from typing import Dict, List, Tuple
from generator.template.utility import writer

template = """
//*************************************************************************************
//   !!! Generated by the fmp-cli.  DO NOT EDIT!
//*************************************************************************************

using Grpc.Net.Client;
using XTC.FMP.LIB.MVCS;

namespace {{org}}.FMP.MOD.{{module}}.LIB.MVCS
{

    /// <summary>
    /// 模块选项
    /// </summary>
    public class Options : UserData
    {
        /// <summary>
        /// 获取GRPC通道
        /// </summary>
        public GrpcChannel? getChannel()
        {
            return channel_;
        }

        /// <summary>
        /// 设置GRPC通道
        /// </summary>
        /// <param name="_channel">GRPC通道</param>
        public void setChannel(GrpcChannel? _channel)
        {
            channel_ = _channel;
        }

        /// <summary>
        /// GRPC通道
        /// </summary>
        private GrpcChannel? channel_;
    }

    /// <summary>
    /// 模块入口基类
    /// </summary>
    public class BaseEntry : UserData
    {
        /// <summary>
        /// 模块选项
        /// </summary>
        protected Options? options_;
{{member_blocks}}

        /// <summary>
        /// 注入MVCS框架
        /// </summary>
        /// <param name="_framework">MVCS框架</param>
        /// <param name="_options">模块选项</param>
        public void Inject(Framework _framework, Options _options)
        {
            framework_ = _framework;
            options_ = _options;
        }

        /// <summary>
        /// 静态注册
        /// </summary>
        /// <param name="_logger">日志</param>
        /// <returns>错误</returns>
        protected Error staticRegister(Logger? _logger)
        {
            _logger?.Trace("StaticRegister");

            if (null == framework_)
            {
                return Error.NewNullErr("framework is null");
            }
{{static_register_blocks}}
            return Error.OK;
        }

        /// <summary>
        /// 动态注册
        /// </summary>
        /// <param name="_logger">日志</param>
        /// <returns>错误</returns>
        protected Error dynamicRegister(Logger _logger)
        {
            _logger.Trace("DynamicRegister");

            if (null == framework_)
            {
                return Error.NewNullErr("framework is null");
            }
{{dynamic_register_blocks}}
            return Error.OK;
        }

        /// <summary>
        /// 静态注销
        /// </summary>
        /// <param name="_logger">日志</param>
        /// <returns>错误</returns>
        protected Error staticCancel(Logger _logger)
        {
            _logger?.Trace("StaticCancel");

            if (null == framework_)
            {
                return Error.NewNullErr("framework is null");
            }
{{static_cancel_blocks}}
            return Error.OK;
        }

        /// <summary>
        /// 动态注销
        /// </summary>
        /// <param name="_logger">日志</param>
        /// <returns>错误</returns>
        protected Error dynamicCancel(Logger _logger)
        {
            _logger?.Trace("DynamicCancel");

            if (null == framework_)
            {
                return Error.NewNullErr("framework is null");
            }
{{dynamic_cancel_blocks}}
            return Error.OK;
        }

        /// <summary>
        /// MVCS框架
        /// </summary>
        private Framework? framework_;
    }
}

"""

template_member = """
        protected {{service}}Facade? facade{{service}}_;
        protected {{service}}Model? model{{service}}_;
        protected {{service}}View? view{{service}}_;
        protected {{service}}Controller? controller{{service}}_;
        protected {{service}}Service? service{{service}}_;

        /// <summary>
        /// 获取{{service}}的UI装饰层
        /// </summary>
        /// <returns>UI装饰层</returns>
        public {{service}}Facade? get{{service}}Facade()
        {
            return facade{{service}}_;
        }
"""

template_static_register = """
            // 注册数据层
            model{{service}}_ = new {{service}}Model({{service}}Model.NAME);
            framework_.getStaticPipe().RegisterModel(model{{service}}_);
            // 注册视图层
            view{{service}}_ = new {{service}}View({{service}}View.NAME);
            framework_.getStaticPipe().RegisterView(view{{service}}_);
            // 注册控制层
            controller{{service}}_ = new {{service}}Controller({{service}}Controller.NAME);
            framework_.getStaticPipe().RegisterController(controller{{service}}_);
            // 注册服务层
            service{{service}}_ = new {{service}}Service({{service}}Service.NAME);
            framework_.getStaticPipe().RegisterService(service{{service}}_);
            service{{service}}_.InjectGrpcChannel(options_?.getChannel());
            // 注册UI装饰层
            facade{{service}}_ = new {{service}}Facade({{service}}Facade.NAME);
            var bridge{{service}} = new {{service}}ViewBridge();
            bridge{{service}}.service = service{{service}}_;
            facade{{service}}_.setViewBridge(bridge{{service}});
            framework_.getStaticPipe().RegisterFacade(facade{{service}}_);
"""

template_dynamic_register = """
            // 注册数据层
            model{{service}}_ = new {{service}}Model({{service}}Model.NAME);
            framework_.getDynamicPipe().PushModel(model{{service}}_);
            // 注册视图层
            view{{service}}_ = new {{service}}View({{service}}View.NAME);
            framework_.getDynamicPipe().PushView(view{{service}}_);
            // 注册控制层
            controller{{service}}_ = new {{service}}Controller({{service}}Controller.NAME);
            framework_.getDynamicPipe().PushController(controller{{service}}_);
            // 注册服务层
            service{{service}}_ = new {{service}}Service({{service}}Service.NAME);
            framework_.getDynamicPipe().PushService(service{{service}}_);
            service{{service}}_.InjectGrpcChannel(options_?.getChannel());
            // 注册UI装饰层
            facade{{service}}_ = new {{service}}Facade({{service}}Facade.NAME);
            var bridge{{service}} = new {{service}}ViewBridge();
            bridge{{service}}.service = service{{service}}_;
            facade{{service}}_.setViewBridge(bridge{{service}});
            framework_.getDynamicPipe().PushFacade(facade{{service}}_);
"""

template_static_cancel = """
            // 注销服务层
            framework_.getStaticPipe().CancelService(service{{service}}_);
            // 注销控制层
            framework_.getStaticPipe().CancelController(controller{{service}}_);
            // 注销视图层
            framework_.getStaticPipe().CancelView(view{{service}}_);
            // 注销UI装饰层
            framework_.getStaticPipe().CancelFacade(facade{{service}}_);
            // 注销数据层
            framework_.getStaticPipe().CancelModel(model{{service}}_);
"""

template_dynamic_cancel = """
            // 注销服务层
            framework_.getDynamicPipe().PopService(service{{service}}_);
            // 注销控制层
            framework_.getDynamicPipe().PopController(controller{{service}}_);
            // 注销视图层
            framework_.getDynamicPipe().PopView(view{{service}}_);
            // 注销UI装饰层
            framework_.getDynamicPipe().PopFacade(facade{{service}}_);
            // 注销数据层
            framework_.getDynamicPipe().PopModel(model{{service}}_);
"""


def generate(
    _orgname: str,
    _modulename: str,
    _outputdir: str,
    _enums: List[str],
    _services: Dict[str, Dict[str, Tuple]],
    _messages: Dict[str, List[Tuple]],
):
    member_blocks = ""
    static_register_blocks = ""
    dynamic_register_blocks = ""
    static_cancel_blocks = ""
    dynamic_cancel_blocks = ""
    for service in _services.keys():
        for rpc_name in _services[service].keys():
            member_block = template_member.replace("{{service}}", service)
            member_blocks = member_blocks + member_block
            static_register_block = template_static_register.replace("{{service}}", service)
            static_register_blocks = static_register_blocks + static_register_block
            dynamic_register_block = template_dynamic_register.replace("{{service}}", service)
            dynamic_register_blocks = dynamic_register_blocks + dynamic_register_block 
            static_cancel_block = template_static_cancel.replace("{{service}}", service)
            static_cancel_blocks = static_cancel_blocks + static_cancel_block 
            dynamic_cancel_block = template_dynamic_cancel.replace("{{service}}", service)
            dynamic_cancel_blocks = dynamic_cancel_blocks + dynamic_cancel_block 
    # 生成项目文件
    contents = (
        template.replace("{{org}}", _orgname)
        .replace("{{module}}", _modulename)
        .replace("{{member_blocks}}", member_blocks)
        .replace("{{static_register_blocks}}", static_register_blocks)
        .replace("{{dynamic_register_blocks}}", dynamic_register_blocks)
        .replace("{{static_cancel_blocks}}", static_cancel_blocks)
        .replace("{{dynamic_cancel_blocks}}", dynamic_cancel_blocks)
    )
    filepath = os.path.join(_outputdir, "BaseEntry.cs")
    writer.write(filepath, contents, True)
