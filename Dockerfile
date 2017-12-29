FROM python:3.6.4-alpine3.7

EXPOSE 8000
WORKDIR /usr/src/pythonathon

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "/usr/local/bin/gunicorn", "pythonathon_v3.wsgi" ]
