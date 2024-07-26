# 容器下载
```
docker pull harbor.spdiotdev.tech/docker/ubuntu:22.04
```
# 容器构建
```
docker build -f Dockerfile -t rasa-dev:0.1 .
```

# 容器启动  
```
docker run -dit --name rasa_dev --shm-size 24g -v /home/zhangjl19:/workspace rasa-mydev:0.1

docker-compose up -d --build
docker compose up -d 

```
> docker run -dit --name rasa_dev --shm-size 24g -v /home/zhangjl19:/workspace rasa:localdev init   
> docker run -dit --gpus=all --ipc=host --net=test-net --name llm_t2 --shm-size 24g -v /home/zhangjl19:/workspace ds_sp_cuda:torch201_cuda117 /bin/bash  

# poetry 简介
> https://aber.sh/articles/python-poetry/

# rasa源码环境搭建
> https://blog.csdn.net/yjsz2010/article/details/130008410

# 中文样例
> https://www.sunzhongwei.com/rasa-chinese-dialogue-robot-series-tutorial

# poetry  
## 修改源
```
poetry source add tsinghua https://pypi.tuna.tsinghua.edu.cn/simple  
```

## 导出requirements
```
poetry export -f requirements.txt -o requirements.txt --without-hashes --dev
```