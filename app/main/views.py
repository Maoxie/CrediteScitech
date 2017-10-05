# _*_ coding: utf-8 _*_
__author__ = 'maoxie'
__date__ = '2017/9/13 21:30'

from datetime import datetime
from flask import render_template, session, redirect, url_for

from . import main
from . import init_data
#from .forms import ##TODO
from .. import db
#from ..models import ##TODO


@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@main.route('/profession/<int:pid>', methods=['GET'])
def profession(pid):
    # TODO: get from db
    # pid starts from 1
    content = init_data.professions[pid-1]
    all_professions = init_data.professions_list
    return render_template('profession.html',
                           all_professions=all_professions,
                           current_page=pid,
                           content=content)


@main.route('/qc', methods=['GET'])
def qc():
    return render_template('qc.html')


@main.route('/about', methods=['GET'])
def about():
    return render_template('about-us.html')