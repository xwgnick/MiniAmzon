#!/bin/bash
echo "Starting frontend..."
python3 manage.py makemigrations
python3 manage.py migrate
sleep 30
python3 manage.py runserver 0.0.0.0:8080