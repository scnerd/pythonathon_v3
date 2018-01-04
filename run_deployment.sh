#!/bin/sh
set -ex

sleep 2
./manage.py migrate
./manage.py initadmin
gunicorn pythonathon_v3.wsgi --bind 0.0.0.0:8000
