FROM python:3.6-alpine

EXPOSE 8000
WORKDIR /usr/src/pythonathon

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "/usr/local/bin/gunicorn", "-b", "0.0.0.0:8000", "pythonathon_v3.wsgi" ]
