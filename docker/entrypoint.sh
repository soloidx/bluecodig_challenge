#!/usr/bin/env bash

/wait

alembic upgrade head
python manage.py runserver
