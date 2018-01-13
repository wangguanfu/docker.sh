#!/bin/bash 
#

echo '---------------migrate database main------------------------'
docker exec -it mysite python manage.py migrate

echo '---------------create superuser admin-----------------------'
docker exec -it mysite python manage.py createsuperuser --username admin --email admin@admin.com --database default
