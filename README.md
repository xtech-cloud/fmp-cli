# 开发环境

python: 3.8.3

# 依赖包

- conda

```bash
conda config --add channels https://mirrors.aliyun.com/anaconda/cloud/conda-forge
conda config --set show_channel_urls yes

conda install grpcio==1.46.0 -c conda-forge
conda install grpcio-tools==1.46.0 -c conda-forge
conda install pyyaml==5.1.2 -c conda-forge
conda install colorama==0.4.0 -c conda-forge
conda install requests==2.23.0 -c conda-forge
pip install pyinstaller==5.6.2
```

# 编译proto
```bash
python -m grpc_tools.protoc -I./proto/Repository --python_out=./mygrpc --grpc_python_out=./mygrpc ./proto/Repository/*.proto
                                                                                                                      ```


# 构建独立可执行程序

##

## Windows

运行install.bat


# 运行错误解决方法
- assertion failed: pem_root_certs != nullptr

在fmp-cli.spec中加入
```
datas=[
('roots.pem', 'grpc/_cython/_credentials/'),
],
```

