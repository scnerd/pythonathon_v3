#!/usr/bin/env bash

docker build -t pythonathon .
docker run -p 8000:8000 $@ -it pythonathon
