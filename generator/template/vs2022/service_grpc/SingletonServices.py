import os
from typing import Dict, List, Tuple
from generator.template.utility import writer

template = """
using Grpc.Core;
using System.Threading.Tasks;
using {{org}}.FMP.MOD.{{module}}.LIB.Proto;

namespace {{org}}.FMP.MOD.{{module}}.App.Service
{
    public class SingletonServices 
    {
        
        /* 解开注释可用于支持数据库操作
        private MongoClient mongoClient_;
        private IMongoDatabase mongoDatabase_;
        private YourDAO daoYour_;

        /// <summary>
        /// 构造函数
        /// </summary>
        /// <remarks>
        /// 参数为自动注入，支持多个参数，DatabaseSettings的注入点在Program.cs中，自定义设置可在MyProgram.PreBuild中注入
        /// </remarks>
        public SingletonServices(IOptions<DatabaseSettings> _databaseSettings, IOptions<MinIOSettings> _minioSettings)
        {
            mongoClient_ = new MongoClient(_databaseSettings.Value.ConnectionString);
            mongoDatabase_ = mongoClient_.GetDatabase(_databaseSettings.Value.DatabaseName);

            daoYour_ = new YourDAO(mongoDatabase_);
        }

        public YourDAO getYourDAO()
        {
            return daoYour_;
        }
        */
    }
}
"""


def generate(_options, _outputdir: str):
    org_name = _options["org_name"]
    module_name = _options["module_name"]
    services = _options["services"]

    for service in services.keys():
        contents = (
            template.replace("{{org}}", org_name)
            .replace("{{module}}", module_name)
            .replace("{{service}}", service)
        )
        filepath = os.path.join(_outputdir, "SingletonServices.cs")
        writer.write(filepath, contents, False)
