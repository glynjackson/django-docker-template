#!/bin/sh
cd /var/projects/mysite && python manage.py migrate --noinput
supervisord -n -c /etc/supervisor/supervisord.conf