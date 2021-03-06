#!/bin/bash 
#

echo "---------------start mysql image-------------------"
docker run --name mysql \
-v $(pwd)/conf.d:/etc/mysql/conf.d \
-v $(pwd)/data:/var/lib/mysql \
-e MYSQL_ROOT_PASSWORD=mysql \
-p 3307:3306 \
-d daocloud.io/mysql:5.7.20 \
--character-set-server=utf8 --collation-server=utf8_unicode_ci
#sleep 15
