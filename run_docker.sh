#!/usr/bin/env bash

docker build -t pythonathon .
docker run -p 127.0.0.1:8000:8000 $@ -it pythonathon
