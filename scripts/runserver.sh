#!/bin/sh
#python manage.py runserver 0.0.0.0:8000
gunicorn --bind 0.0.0.0:8000 core.wsgi --workers=4
