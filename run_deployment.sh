#!/bin/bash
set -ex

function cleanup {
    name="${BACKUP_PATH}/db"
    i=0
    if [[ -e "${name}.json" ]] ; then
        mv "${name}.json" "${name}_backup.json"
    fi
    if [[ -e "${name}_questions.json" ]] ; then
        mv "${name}_questions.json" "${name}_questions_backup.json"
    fi
    qname="${name}_questions.json"
    name="${name}.json"
    ./manage.py dumpdata ctf > $qname
    ./manage.py dumpdata > $name
}
trap cleanup EXIT

sleep 1

./manage.py makemigrations
./manage.py migrate

if [[ -e ${RESTORE_PATH} ]]; then
./manage.py loaddata ${RESTORE_PATH};
mv ${RESTORE_PATH} "${RESTORE_PATH}.done"
else
set +e
./manage.py dumpdata ctf > "${BACKUP_PATH}/onlaunch_questions.json";
./manage.py dumpdata > "${BACKUP_PATH}/onlaunch.json";
set -e
fi

./manage.py initadmin
./manage.py initjupyterhub
./manage.py collectstatic
uwsgi --http :8000 --socket :3031 --module pythonathon_v3.wsgi
# gunicorn pythonathon_v3.wsgi --bind 0.0.0.0:8000
