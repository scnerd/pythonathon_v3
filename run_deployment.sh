#!/usr/bin/env bash

./manage.py migrate
gunicorn pythonathon_v3.wsgi
