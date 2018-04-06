FROM python:3.6-alpine
RUN apk add --no-cache bash

# psycopg2 for postgresql support
RUN apk update \
#  && apk add jpeg-dev zlib-dev \
  && apk add --virtual build-deps gcc linux-headers libc-dev python3-dev musl-dev \
  && apk add postgresql-dev \
  && pip install psycopg2 uwsgi \
  && apk del build-deps

EXPOSE 8000
EXPOSE 3031
WORKDIR /usr/src/pythonathon

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "./run_deployment.sh" ]
