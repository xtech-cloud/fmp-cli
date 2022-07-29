import os
from generator.template.utility import writer

template = """
using XTC.FMP.LIB.MVCS;

namespace {{org}}.FMP.MOD.{{module}}.LIB.MVCS
{
    /// <summary>
    /// 模块入口
    /// </summary>
    public class Entry : EntryBase
    {

        /// <summary>
        /// 静态注册
        /// </summary>
        /// <param name="_logger">日志</param>
        /// <returns>错误</returns>
        public Error StaticRegister(Logger? _logger)
        {
            return base.staticRegister(_logger);
        }

        /// <summary>
        /// 动态注册
        /// </summary>
        /// <param name="_logger">日志</param>
        /// <returns>错误</returns>
        public Error DynamicRegister(Logger _logger)
        {
            return base.dynamicRegister(_logger);
        }

        /// <summary>
        /// 静态注销
        /// </summary>
        /// <param name="_logger">日志</param>
        /// <returns>错误</returns>
        public Error StaticCancel(Logger _logger)
        {
            return base.staticCancel(_logger);
        }

        /// <summary>
        /// 动态注销
        /// </summary>
        /// <param name="_logger">日志</param>
        /// <returns>错误</returns>
        public Error DynamicCancel(Logger _logger)
        {
            return base.dynamicCancel(_logger);
        }
    }
}

"""

def generate(_orgname: str, _modulename: str, _outputdir: str):
    # 生成项目文件
    contents = template.replace("{{org}}", _orgname).replace("{{module}}", _modulename)
    filepath = os.path.join(_outputdir, 'Entry.cs')
    writer.write(filepath, contents, False)
