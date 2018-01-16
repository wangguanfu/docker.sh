#!/bin/bash 
#
docker exec -d mysql mysql -uroot -pmysql -e "create database blog;"
docker build -t mysite/django .
docker run --name django \
-v /mysite \
-v /mysite/static \
--link mysql:mysql \
-p 8000:8000 \
-d mysite/django /usr/local/bin/uwsgi --http :8000 --chdir /mysite/mysite -w mmcsite.wsgi

