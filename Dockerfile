FROM python:3.6-alpine

EXPOSE 8000
WORKDIR /usr/src/pythonathon

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "./run_deployment.sh" ]
