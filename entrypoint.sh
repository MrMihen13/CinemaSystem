#!/bin/sh

python manage.py migrate || exit 1
gunicorn cinema_system.wsgi:application --bind 0.0.0.0:8000 --reload --log-level DEBUG
