# 基础镜像
FROM daocloud.io/python:2.7


RUN mkdir /code
RUN mkdir /code/db
WORKDIR /code
ADD ./mysite/requirements.txt /code
# app 所在目录
WORKDIR /code

# 安装 app 所需依赖
RUN pip install --no-cache-dir -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
ADD . /code                                                             
