#!/bin/sh
set -ex

./manage.py migrate
./manage.py initadmin
gunicorn pythonathon_v3.wsgi
