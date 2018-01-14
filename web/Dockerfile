# 基础镜像
FROM daocloud.io/python:2.7

ENV DJANGO_PRODUCTION false
RUN mkdir /mysite
ADD . /mysite
# app 所在目录
WORKDIR /mysite

# 安装 app 所需依赖
RUN pip install --no-cache-dir -r /mysite/mysite/requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
                                                             
