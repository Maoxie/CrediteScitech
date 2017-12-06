# _*_ coding: utf-8 _*_
__author__ = 'maoxie'
__date__ = '2017/12/6 22:27'


import os
from app import celery, create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app.app_context().push()