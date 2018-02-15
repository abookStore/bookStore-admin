# -*- coding: utf-8 -*-
from bookStore import app


@app.route('/')
# @app.route('/<path:path>')
def index(path=''):
    return 'Hi! This is bookStore.'