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


    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') # or \
                              # 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    UPLOAD_FILES_PATH = os.path.join(basedir, 'app', 'static', 'customer_upload')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') # or \
                              # 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    UPLOAD_FILES_PATH = os.getenv('CREDITE_UPLOAD_FILES_PATH')


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
