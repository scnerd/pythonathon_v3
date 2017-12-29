docker run -it --rm --name pythonathon_v3_depl -v "$PWD":/usr/src/myapp -w /usr/src/pythonathon python:3.6 gunicorn pythonathon_v3.wsgi
