# _*_ coding: utf-8 _*_
__author__ = 'maoxie'
__date__ = '2017/9/13 21:27'

from flask import Flask, render_template
from flask_bootstrap import Bootstrap, WebCDN, ConditionalCDN, \
    BOOTSTRAP_VERSION, JQUERY_VERSION, HTML5SHIV_VERSION, RESPONDJS_VERSION
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
import re

bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()


def change_cdn_domestic(tar_app):
    # bootstrap使用国内CDN
    static = tar_app.extensions['bootstrap']['cdns']['static']
    local = tar_app.extensions['bootstrap']['cdns']['local']

    def change_one(tar_lib, tar_ver, fallback):
        tar_js = ConditionalCDN('BOOTSTRAP_SERVE_LOCAL', fallback,
                                WebCDN('//cdn.bootcss.com/' + tar_lib + '/' + tar_ver + '/'))
        tar_app.extensions['bootstrap']['cdns'][tar_lib] = tar_js

    libs = {'jquery': {'ver': JQUERY_VERSION, 'fallback': local},
            'bootstrap': {'ver': BOOTSTRAP_VERSION, 'fallback': local},
            'html5shiv': {'ver': HTML5SHIV_VERSION, 'fallback': static},
            'respond.js': {'ver': RESPONDJS_VERSION, 'fallback': static}}
    for lib, par in libs.items():
        change_one(lib, par['ver'], par['fallback'])


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    # bootstrap使用国内CDN
    change_cdn_domestic(app)

    def cdn_url_builder(error, endpoint, values):
        # error handler to build url for resources on cdn.
        # refer to https://github.com/pallets/flask/issues/785
        if not re.match(r'.*\.static', endpoint):
            return
        filename = values.pop('filename')
        # Ignore _external flag, we're always external
        values.pop('_external', None)
        cdn_url = config[config_name].CDN_URL
        return 'http://%s/static/%s' % (
            cdn_url,
            filename
        )

    app.url_build_error_handlers.append(cdn_url_builder)

    # 注册蓝本
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
