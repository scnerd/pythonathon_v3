#!/bin/sh
set -ex

./manage.py migrate
gunicorn pythonathon_v3.wsgi
