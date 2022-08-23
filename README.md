# 开发环境

python: 3.8.3

# 依赖包

```bash
pip install grpcio==1.47.0
pip install grpcio-tools==1.47.0
```

# 编译proto
```bash
python -m grpc_tools.protoc -I./proto/Repository --python_out=./mygrpc --grpc_python_out=./mygrpc ./proto/Repository/*.proto
```


# 构建独立可执行程序

## 

## Windows

运行install.bat

