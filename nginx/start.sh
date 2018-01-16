#!/bin/bash 
#
docker build -t nginx .
docker run --name nginx-server \
--link django:web \
-v /mysite/mysite/static:/www/static \
--volumes-from django \
-p 80:80 \
-d nginx
