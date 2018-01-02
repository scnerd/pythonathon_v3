FROM python:3.6-alpine

# psycopg2 for postgresql support
RUN apk update \
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  && pip install psycopg2 \
  && apk del build-deps

EXPOSE 8000
WORKDIR /usr/src/pythonathon

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "./run_deployment.sh" ]
