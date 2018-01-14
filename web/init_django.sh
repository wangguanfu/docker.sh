#!/bin/bash 
#

echo '---------------migrate database main------------------------'
docker exec -it django python /mysite/mysite/manage.py migrate

echo '---------------create superuser admin-----------------------'
docker exec -it django python /mysite/mysite/manage.py createsuperuser --username admin --email admin@admin.com --database default
