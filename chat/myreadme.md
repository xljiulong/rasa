# 系统配置
## 环境创建
```
conda create -n py39 python=3.9
```
## 激活环境
```
conda activate py39
```

## 删除环境
```
conda env remove -n py39
```

## 设置源
```
export PIP_INDEX_URL=https://mirrors.aliyun.com/pypi/simple/
or 
export PIP_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple 

```

## 代理设置
```
export HTTP_PROXY=http://192.168.200.26:58591
export HTTPS_PROXY=http://192.168.200.26:58591
```
## 取消代理
```

```
# rasa安装
```
pip install rasa
```

# rasa
## 命令行说明
> https://rasa.com/docs/rasa/command-line-interface/


# rasa 操作
## 启动action server
```
rasa run actions
```

## 启动会话
```
rasa shell
/session_start
```

# 容器操作
## 启动 
```
docker-compose up -d --build


# poetry 
## 参考资料
```
https://blog.kyomind.tw/python-poetry/
```

## 初始化
```
poetry init (已经存在项目)
poetry new proj_name
```

## 创建环境
```
poetry install
```

## 使用虚拟环境
```
poetry run cmds
or
poetry shell
then run 
```

## 安装包
```
poetry add pkg
poetry add pytest --dev # 开发依赖
```


## 查看依赖
```
poetry show
poetry show --tree
poetry show --outdated
```

## 更新依赖
```
poetry update
poetry update foo
```

## 卸载某个包
```
poetry remove foo
```

## 更新lock文件
```
poetry lock
```

## 配置源
```
pyproject.toml 
[[tool.poetry.source]]
name = "douban"
url = "https://pypi.doubanio.com/simple/"
```