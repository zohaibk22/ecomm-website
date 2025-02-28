#!/bin/sh

# Apply migrations
python manage.py migrate

# Start Django server with hot reload
exec watchfiles "python manage.py runserver 0.0.0.0:8000"