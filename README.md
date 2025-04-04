# 4459_Project

Generate the pb2 files with: 
```
python -m grpc_tools.protoc -I./protos --python_out=. --pyi_out=. --grpc_python_out=. ./protos/*
```

# How to Run

## 1. Start proxy server
```
python3 proxy.py
```

## 2. Start heartbeat server
```
python3 heartbeat.py
```

## 3. Start primary server
```
python3 server primary 50051
```

## 4. Start backup server
```
python3 server backup 50055 
```

## 5. Add clients, CLI or GUI available (tkinter required)
```
python3 grpc_client.py
```
```
python3 gui_client.py
```


