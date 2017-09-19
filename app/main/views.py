# _*_ coding: utf-8 _*_
__author__ = 'maoxie'
__date__ = '2017/9/13 21:30'

from datetime import datetime
from flask import render_template, session, redirect, url_for

from . import main
#from .forms import ##TODO
from .. import db
#from ..models import ##TODO


@main.route('/', methods=['GET', 'POST'])
def index():
    organization_logos = [
        url_for('static', filename='media/index/in-index-org-1.png', _external=True),
        url_for('static', filename='media/index/in-index-org-2.jpg', _external=True),
        url_for('static', filename='media/index/in-index-org-3.jpg', _external=True),
        url_for('static', filename='media/index/in-index-org-4.png', _external=True),
        url_for('static', filename='media/index/in-index-org-5.jpg', _external=True),
        url_for('static', filename='media/index/in-index-org-6.png', _external=True),
        url_for('static', filename='media/index/in-index-org-7.png', _external=True)
    ]
    return render_template('index.html',
                           name="Maoxie", org_logos=organization_logos)
