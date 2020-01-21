#!/bin/sh
gunicorn --reload --worker-class gevent --config settings.py app:app