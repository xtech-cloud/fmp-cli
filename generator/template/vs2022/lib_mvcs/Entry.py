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
        /// <remarks>
        /// 使用(NAME+"."+_id)作为uid，注册一套MVCS
        /// </remarks>
        /// <param name="_id">id</param>
        /// <param name="_logger">日志</param>
        /// <returns>错误</returns>
        public Error StaticRegister(string _id, Logger? _logger)
        {
            return base.staticRegister(_id, _logger);
        }

        /// <summary>
        /// 动态注册
        /// </summary>
        /// <remarks>
        /// 使用(NAME+"."+_id)作为uid，注册一套MVCS
        /// </remarks>
        /// <param name="_id">id</param>
        /// <param name="_logger">日志</param>
        /// <returns>错误</returns>
        public Error DynamicRegister(string _id, Logger _logger)
        {
            return base.dynamicRegister(_id, _logger);
        }

        /// <summary>
        /// 静态注销
        /// </summary>
        /// <remarks>
        /// 使用(NAME+"."+_id)作为uid，注销一套MVCS
        /// </remarks>
        /// <param name="_id">id</param>
        /// <param name="_logger">日志</param>
        /// <returns>错误</returns>
        public Error StaticCancel(string _id, Logger _logger)
        {
            return base.staticCancel(_id, _logger);
        }

        /// <summary>
        /// 动态注销
        /// </summary>
        /// <remarks>
        /// 使用(NAME+"."+_id)作为uid，注销一套MVCS
        /// </remarks>
        /// <param name="_id">id</param>
        /// <param name="_logger">日志</param>
        /// <returns>错误</returns>
        public Error DynamicCancel(string _id, Logger _logger)
        {
            return base.dynamicCancel(_id, _logger);
        }
    }
}

"""

def generate(_orgname: str, _modulename: str, _outputdir: str):
    # 生成项目文件
    contents = template.replace("{{org}}", _orgname).replace("{{module}}", _modulename)
    filepath = os.path.join(_outputdir, 'Entry.cs')
    writer.write(filepath, contents, False)
