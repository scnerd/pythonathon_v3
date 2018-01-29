#!/bin/bash
set -ex

function cleanup {
    name="${BACKUP_PATH}/db"
    i=0
    if [[ -e "${name}.json" ]] ; then
        mv "${name}.json" "${name}_backup.json"
    fi
    name="${name}.json"
    ./manage.py dumpdata ctf > $name
}
trap cleanup EXIT

sleep 1
./manage.py dumpdata ctf > "${BACKUP_PATH}/onlaunch.json"
./manage.py makemigrations
./manage.py migrate
./manage.py initadmin
./manage.py initjupyterhub
./manage.py collectstatic
uwsgi --http :8000 --socket :3031 --module pythonathon_v3.wsgi
# gunicorn pythonathon_v3.wsgi --bind 0.0.0.0:8000
