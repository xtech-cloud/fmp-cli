import os
from typing import Dict, List, Tuple
from generator.template.utility import writer

template_mongodb = """
//*************************************************************************************
//   !!! Generated by the fmp-cli.  DO NOT EDIT!
//*************************************************************************************

using Microsoft.Extensions.Options;
using MongoDB.Driver;

namespace {{org}}.FMP.MOD.{{module}}.App.Service
{
    /// <summary>
    /// 泛型数据访问对象
    /// </summary>
    /// <typeparam name="T">Entity的派生类</typeparam>
    /// <example>
    /// public class YourDAO : DAO<YourEntity>
    /// {
    ///     public YourDAO(IOptions<DatabaseSettings> _settings) 
    ///         : base(_settings, "TableName")
    ///     {
    ///     }
    ///}
    /// </example>
    public class DAO<T> where T : Entity
    {
        protected readonly IMongoCollection<T> collection_;

        /// <summary>
        /// 构造函数
        /// </summary>
        /// <param name="_settings">数据库设置</param>
        /// <param name="_collectionName">Entity对应的数据库集合名</param>
        public DAO(IOptions<DatabaseSettings> _settings, string _collectionName)
        {
            var mongoClient = new MongoClient(_settings.Value.ConnectionString);
            var db = mongoClient.GetDatabase(_settings.Value.DatabaseName);
            collection_ = db.GetCollection<T>(_collectionName);
        }

        /// <summary>
        /// 异步创建实体
        /// </summary>
        /// <param name="_entity">实体的实例</param>
        /// <returns></returns>
        public async Task CreateAsync(T _entity) =>
           await collection_.InsertOneAsync(_entity);

        /// <summary>
        /// 异步列举实体
        /// </summary>
        /// <param name="_offset">偏移量</param>
        /// <param name="_count">查询量</param>
        /// <returns></returns>
        public async Task<List<T>> ListAsync(int _offset, int _count) =>
            await collection_.Find(_ => true).Limit(_count).ToListAsync();

        /// <summary>
        /// 获取实体
        /// </summary>
        /// <param name="_uuid">实体的uuid</param>
        /// <returns></returns>
        public async Task<T?> GetAsync(string _uuid) =>
            await collection_.Find(x => x.Uuid.ToString() == _uuid).FirstOrDefaultAsync();

        /// <summary>
        /// 更新实体
        /// </summary>
        /// <param name="_uuid">实体的uuid</param>
        /// <param name="_entity">实体的实例</param>
        /// <returns></returns>
        public async Task UpdateAsync(string _uuid, T _entity) =>
            await collection_.ReplaceOneAsync(x => x.Uuid.ToString() == _uuid, _entity);

        /// <summary>
        /// 异步移除实体
        /// </summary>
        /// <param name="_uuid">实体的uuid</param>
        /// <returns></returns>
        public async Task RemoveAsync(string _uuid) =>
            await collection_.DeleteOneAsync(x => x.Uuid.ToString() == _uuid);
    }
}
"""

def generate(
    _orgname: str,
    _modulename: str,
    _outputdir: str,
    _databasedriver: str,
):
    if "mongodb" == _databasedriver:
        contents = template_mongodb.replace("{{org}}", _orgname).replace("{{module}}", _modulename)
        filepath = os.path.join(_outputdir, "DAO.cs")
        writer.write(filepath, contents, True)
