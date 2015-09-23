#!/bin/sh
cd /var/projects/ctzn && python manage.py migrate --noinput
cd /var/projects/ctzn/deploy/scripts/ && python deploy_docs.py
supervisord -n -c /etc/supervisor/supervisord.conf