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
    return render_template('index.html',
                           name="Maoxie")
