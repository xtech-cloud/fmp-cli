import os
from typing import Dict, List, Tuple
from generator.template.utility import writer

template = """

//*************************************************************************************
//   !!! Generated by the fmp-cli {{version}}.  DO NOT EDIT!
//*************************************************************************************

namespace {{org}}.FMP.MOD.{{module}}.App.Service
{

    public class ArgumentRequiredException : Exception
    {
        public ArgumentRequiredException(string _message) : base(_message)
        {

        }
    }

    /// <summary>
    /// 参数检查
    /// </summary>
    public class ArgumentChecker
    {
        /// <summary>
        /// 检查必须的字符型参数
        /// </summary>
        /// <param name="_value">参数的值</param>
        /// <param name="_name">参数的名字</param>
        /// <exception cref="ArgumentException">参数为空或空白符，抛出异常</exception>
        public static void CheckRequiredString(string _value, string _name)
        {
            if (!string.IsNullOrWhiteSpace(_value))
                return;
            throw new ArgumentRequiredException(string.Format("argument {0} is required!", _name));
        }

        /// <summary>
        /// 检查必须的数值型参数
        /// </summary>
        /// <param name="_value">参数的值</param>
        /// <param name="_name">参数的名字</param>
        /// <exception cref="ArgumentException">参数等于0，抛出异常</exception>
        public static void CheckRequiredNumber(int _value, string _name)
        {
            if (0 != _value)
                return;
            throw new ArgumentRequiredException(string.Format("argument {0} is required!", _name));
        }

        /// <summary>
        /// 检查必须的对象型参数
        /// </summary>
        /// <param name="_value">参数的值</param>
        /// <param name="_name">参数的名字</param>
        /// <exception cref="ArgumentException">参数等于0，抛出异常</exception>
        public static void CheckRequiredObject(object _value, string _name)
        {
            if (null != _value)
                return;
            throw new ArgumentRequiredException(string.Format("argument {0} is required!", _name));
        }
    }
}
"""

def generate(_options, _outputdir: str):
    org_name = _options["org_name"]
    module_name = _options["module_name"]

    contents = template.replace("{{org}}", org_name).replace("{{module}}", module_name)
    contents = contents.replace("{{version}}", _options["version"])
    filepath = os.path.join(_outputdir, "ArgumentChecker.cs")
    writer.write(filepath, contents, True)
