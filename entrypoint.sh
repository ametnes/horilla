#!/bin/bash

echo "Waiting for database to be ready..."
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --noinput
python3 manage.py createhorillauser --first_name "${HORILLA_ADMIN_FIRST_NAME}" --last_name "${HORILLA_ADMIN_LAST_NAME}" --username "${HORILLA_ADMIN_USER}" --password "${HORILLA_ADMIN_PASSWORD}" --email "${HORILLA_ADMIN_EMAIL}" --phone "${HORILLA_ADMIN_PHONE}"
gunicorn --bind 0.0.0.0:8000 --workers "${HORILLA_NUM_WORKERS}" --timeout "${HORILLA_TIMEOUT}" horilla.wsgi:application
