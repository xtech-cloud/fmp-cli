import os
from typing import Dict, List, Tuple
from generator.template.utility import writer

template_mongodb = """
//*************************************************************************************
//   !!! Generated by the fmp-cli.  DO NOT EDIT!
//*************************************************************************************

using MongoDB.Bson.Serialization.Attributes;
using MongoDB.Bson.Serialization.IdGenerators;

namespace {{org}}.FMP.MOD.{{module}}.App.Service
{
    /// <summary>
    /// 数据实体
    /// </summary>
    /// <example>
    /// public class YourDAO : DAO<YourEntity>
    /// {
    ///     public YourDAO(IOptions<DBSettings> _settings) : base(_settings)
    ///     {
    ///     }
    /// }
    /// </example>
    public class Entity
    {
        /// <summary>
        /// 实体的唯一识别ID
        /// </summary>
        /// <remarks>
        /// 不使用ObjectId
        /// </remarks>
        [BsonId(IdGenerator = typeof(CombGuidGenerator))]
        public Guid? Uuid { get; set; }
    }
}
"""

def generate(
    _orgname: str,
    _modulename: str,
    _outputdir: str,
    _databasedriver: str
):
    if "mongodb" == _databasedriver:
        contents = template_mongodb.replace("{{org}}", _orgname).replace("{{module}}", _modulename)
        filepath = os.path.join(_outputdir, "Entity.cs")
        writer.write(filepath, contents, False)
