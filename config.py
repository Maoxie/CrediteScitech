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
    CDN_URL = os.getenv('DEV_CDN_URL') or ''
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') # or \
                              # 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class ProductionConfig(Config):
    CDN_URL = os.getenv('CREDITE_CDN_URL')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') # or \
                              # 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
