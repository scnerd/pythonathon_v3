#!/bin/sh
set -ex

sleep 2
./manage.py migrate
./manage.py initadmin
uwsgi --http :8000 --socket :3031 --module pythonathon_v3.wsgi
# gunicorn pythonathon_v3.wsgi --bind 0.0.0.0:8000
