#!/bin/bash
python manage.py migrate --noinput
python create_superuser.py
python manage.py collectstatic --noinput
gunicorn yemek_otomasyonu.wsgi
