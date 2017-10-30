# _*_ coding: utf-8 _*_
__author__ = 'maoxie'
__date__ = '2017/9/13 21:29'


import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    CREDITE_PROJECT_URL = os.getenv('CREDITE_PROJECT_URL')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') # or \
                              # 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    UPLOAD_FILES_PATH = os.path.join(basedir, '/app/static/customer_upload')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') # or \
                              # 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    UPLOAD_FILES_PATH = os.getenv('CREDITE_UPLOAD_FILES_PATH')


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
