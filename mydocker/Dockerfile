FROM harbor.spdiotdev.tech/docker/ubuntu:20.04


# env http_proxy "http://192.168.200.26:51837"
# env https_proxy "http://192.168.200.26:51837"

# ENV HOME=/workspace

# # update permissions & change user to not run as root
WORKDIR /workspace

# # copy files
# COPY . /build/

# # change working directory
# WORKDIR /build

RUN echo 'Asia/Shanghai' > /etc/timezone && \
    cp /etc/apt/sources.list /etc/apt/sources.list.bak && \
    apt-get update && apt-get install -y lsb-release && \
    echo "deb http://mirrors.aliyun.com/ubuntu/ $(lsb_release -sc) main restricted universe multiverse" > /etc/apt/sources.list && \
    echo "deb http://mirrors.aliyun.com/ubuntu/ $(lsb_release -sc)-updates main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb http://mirrors.aliyun.com/ubuntu/ $(lsb_release -sc)-backports main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb http://mirrors.aliyun.com/ubuntu/ $(lsb_release -sc)-security main restricted universe multiverse" >> /etc/apt/sources.list && \
    apt-get update 

RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libgdbm-dev \
    zlib1g-dev \
    liblzma-dev \
    openssh-server \
    pdsh \
    net-tools \
    iputils-ping \
    vim \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# 下载 Miniconda 安装脚本
RUN curl -fsSL https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o /miniconda.sh && \
    bash /miniconda.sh -b -p /opt/conda && \
    rm /miniconda.sh 

ENV PATH="/opt/conda/bin:$PATH"

# 创建一个新的 Conda 环境并安装 Python 3.10
RUN conda create --yes --prefix /opt/conda/envs/py310 python=3.10 && \
    . /opt/conda/etc/profile.d/conda.sh && \
    conda activate /opt/conda/envs/py310

# install dependencies
# RUN python -m venv /opt/venv && \
#   . /opt/venv/bin/activate && \
#   pip install --no-cache-dir -U "pip==22.*" -U "wheel>0.38.0" && \
#   poetry config installer.max-workers 10 && \
#   poetry install --no-dev --no-root --no-interaction && \
#   poetry build -f wheel -n && \
#   pip install --no-deps dist/*.whl && \
#   rm -rf dist *.egg-info

# # start a new build stage
# FROM ${IMAGE_BASE_NAME}:base-${BASE_IMAGE_HASH} as runner

# # copy everything from /opt
# COPY --from=builder /opt/venv /opt/venv

# # make sure we use the virtualenv
# ENV PATH="/opt/venv/bin:$PATH"

# # set HOME environment variable
# ENV HOME=/app

# # update permissions & change user to not run as root
# WORKDIR /app
# RUN chgrp -R 0 /app && chmod -R g=u /app && chmod o+wr /app
# USER 1001

# # create a volume for temporary data
# VOLUME /tmp

# # change shell
# SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# # the entry point
# EXPOSE 5005
# ENTRYPOINT ["rasa"]
# CMD ["--help"]
