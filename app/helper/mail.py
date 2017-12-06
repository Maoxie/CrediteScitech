# _*_ coding: utf-8 _*_
__author__ = 'maoxie'
__date__ = '2017/11/30 23:26'

import os
from flask_mail import Message
from flask import current_app as app
from flask import render_template
from app import mail
from app import celery

FLASKY_MAIL_SUBJECT_PREFIX = u'[启信科技]'


def send_mail(to, subject, template, **kwargs):
    send_async_mail.delay(to, subject, template, **kwargs).get()


@celery.task
def send_async_mail(to, subject, template, **kwargs):
    msg = Message(FLASKY_MAIL_SUBJECT_PREFIX + subject,
                  sender=(u"启信科技", app.config['MAIL_USERNAME']), recipients=to)
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    with app.app_context():
        mail.send(msg)