# _*_ coding: utf-8 _*_
__author__ = 'maoxie'
__date__ = '2017/9/13 21:29'


import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    STATIC_FOLDER = 'static'
    CUSTOMER_UPLOAD_MAX_SIZE = 50*1024*1024  # 50MB
    # flask-mail
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = int(os.getenv('MAIL_PORT'))
    MAIL_USE_TLS = (os.getenv('MAIL_USE_TLS').upper() == 'TRUE')
    MAIL_USE_SSL = (os.getenv('MAIL_USE_SSL').upper() == 'TRUE')
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    # celery with redis
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
    # flask_cache with redis
    CACHE_REDIS = {
        "CACHE_TYPE": "redis",
        "CACHE_REDIS_HOST": "127.0.0.1",
        "CACHE_REDIS_PORT": 6379,
        "CACHE_REDIS_DB": 1,
        "CACHE_REDIS_PASSWORD": "",
    }
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') # or \
                              # 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    UPLOAD_FILES_PATH = os.getenv('CREDITE_UPLOAD_FILES_PATH')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') # or \
                              # 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    UPLOAD_FILES_PATH = os.getenv('CREDITE_UPLOAD_FILES_PATH')


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
