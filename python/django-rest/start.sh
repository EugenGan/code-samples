#!/bin/bash

set -e

while ! (timeout 3 bash -c "</dev/tcp/${DB_HOST}/${DB_PORT}") &> /dev/null;
do
    echo waiting for PostgreSQL to start...;
    sleep 3;
done;

python3 manage.py migrate
python3 manage.py loaddata fixtures/*.json
python3 manage.py runserver 0.0.0.0:8000
