# _*_ coding: utf-8 _*_
__author__ = 'maoxie'
__date__ = '2017/9/13 21:30'

from datetime import datetime
from flask import render_template, session, redirect, url_for
from jinja2 import exceptions as JException
from flask_wtf import Form

from . import main
from . import init_data
from . import forms
#from .forms import ##TODO
from .. import db
#from ..models import ##TODO


@main.route('/', methods=['GET'])
def index():
    form = forms.MainCustomerUploadFileForm()
    return render_template('index.html', form=form, customerInfo=session.get('customerInfo'))


@main.route('/profession-sub/<int:pid>/<int:subpid>', methods=['GET'])
def profession_sub(pid, subpid):
    template = 'profession-sub/profession-{pid}-sub/profession-{pid}-{subpid}.html'.format(pid=pid, subpid=subpid)
    try:
        return render_template(template)
    except JException.TemplateNotFound, e:
        return render_template('404.html')


@main.route('/profession/<int:pid>', methods=['GET'])
def profession(pid):
    # pid starts from 1
    try:
        content = init_data.professions[pid-1]
    except IndexError, e:
        return render_template('404.html')
    all_professions = init_data.professions_list
    return render_template('profession.html',
                           all_professions=all_professions,
                           current_page=pid,
                           content=content)


@main.route('/production/<int:pid>', methods=['GET'])
def production(pid):
    # pid ranges from 1 to 8
    if pid < 1 or 8 < pid:
        return render_template('404.html')
    template = 'production-{0}.html'.format(pid)
    try:
        return render_template(template)
    except JException.TemplateNotFound, e:
        return render_template('404.html')


@main.route('/qc', methods=['GET'])
def qc():
    return render_template('qc.html')


@main.route('/about', methods=['GET'])
def about():
    form = forms.MainCustomerUploadFileForm()
    return render_template('about-us.html', form=form, customerInfo=session.get('customerInfo'))


@main.route('/promotion/<int:pid>', methods=['GET'])
def promotion(pid):
    template = 'promotion/promotion-{0}.html'.format(pid)
    try:
        return render_template(template)
    except JException.TemplateNotFound, e:
        return render_template('404.html')


@main.route('/upload-file', methods=['GET', 'POST'])
def upload_file():
    form = forms.MainCustomerUploadFileForm()
    if form.validate_on_submit():
        customerName = form.customerName.data
        customerPhoneNumber = form.customerPhoneNumber.data
        customerEmail = form.customerEmail.data
        uploadFile = form.uploadFile.data
        # TODO: save file
        customerInfo = {
            'customerName': customerName,
            'customerPhoneNumber': customerPhoneNumber,
            'customerEmail': customerEmail
        }
        session['customerInfo'] = customerInfo
        return redirect(url_for('main.index'))
    return render_template('index.html', form=form, customerInfo=session.get('customerInfo'))
