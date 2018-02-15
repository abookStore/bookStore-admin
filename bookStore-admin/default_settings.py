# -*- coding: utf-8 -*-

import datetime
import subprocess


APPLICATION_ROOT = '/bookStore'
SESSION_COOKIE_NAME = 'oscar_session'

# app.debug
DEBUG = True

SECRET_KEY = 'This should be replaced on production'

# API & JSON
JSON_AS_ASCII = False
JSONIFY_PRETTYPRINT_REGULAR = None
JSON_SORT_KEYS = None

# database
SQLALCHEMY_DATABASE_URI = None
SQLALCHEMY_BINDS = {
}

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False

#
# celery
#
BROKER_URL = 'redis://localhost:6379/3'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/3'
CELERY_TASK_RESULT_EXPIRES = 600

# AppStore
FREE_APP_TAB = 1
PAID_APP_TAB = 0

STOREFRONT_CN = 1
STOREFRONTS = {
    STOREFRONT_CN: '143465-19'
}

# API
OSCAR_ACCESS_KEYS = {
    'B4A8611EFED44CA7C949': 'EFl0jD7gbCJ9wcyCYloUEgQw7j3elgN5MFyAs7Mc',  # kiwi
    'FD29D1F4F19E6924F5B7': '0RhfB7XkV97ZYKgNed6oL8FUFHz4lHX9oIoE58hn',  # tigger
}

