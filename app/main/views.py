# _*_ coding: utf-8 _*_
__author__ = 'maoxie'
__date__ = '2017/9/13 21:30'

from datetime import datetime
import os

from flask import render_template, session, redirect, url_for, request, current_app, send_from_directory
from jinja2 import exceptions as JException
from flask_wtf import Form
from werkzeug.utils import secure_filename
from sqlalchemy import desc

from . import main
from . import init_data
from . import forms
from .. import models
from .. import db


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
    if request.method == 'POST':
        if form.validate_on_submit():
            customerName = form.customerName.data
            customerPhoneNumber = form.customerPhoneNumber.data
            customerEmail = form.customerEmail.data

            uploadFile = form.uploadFile.data
            filename = uploadFile.filename
            filename_for_storage = secure_filename(str(datetime.utcnow()) + '_' + filename)
            full_path = os.path.join(current_app.config.get('UPLOAD_FILES_PATH'), filename_for_storage)
            uploadFile.save(full_path)
            # add to database
            newUpload = models.MainCustomerUploadFile(
                customerName=customerName,
                customerPhoneNumber=customerPhoneNumber,
                customerEmail=customerEmail,
                uploadFileName=filename,
                storageFileName=filename_for_storage,
            )
            db.session.add(newUpload)
            db.session.commit()
            customerInfo = {
                'customerName': customerName,
                'customerPhoneNumber': customerPhoneNumber,
                'customerEmail': customerEmail
            }
            session['customerInfo'] = customerInfo
            # TODO: return a flash message to notify users
            return redirect(url_for('main.index'))
    return render_template('index.html', form=form, customerInfo=session.get('customerInfo'))


@main.route('/examples/<int:pid>', methods=['GET'])
def examples(pid):
    template = 'examples-{0}.html'.format(pid)
    try:
        return render_template(template)
    except JException.TemplateNotFound, e:
        return render_template('404.html')


@main.route('/qixinadmin', methods=['GET'])
def admin():
    customer_upload_files = models.MainCustomerUploadFile()
    all_files_model = customer_upload_files.query.order_by(desc(models.MainCustomerUploadFile.updateTime)).all()
    all_files = [{
        'Name': file_model.customerName,
        'PhoneNumber': file_model.customerPhoneNumber,
        'Email': file_model.customerEmail,
        'FileName': file_model.uploadFileName,
        'downloadLink': url_for('main.admin_download', type='customer-uploaded-file', filename=file_model.storageFileName),
        'uploadTime': file_model.updateTime
    } for file_model in all_files_model]
    return render_template('admin.html', all_files=all_files)


@main.route('/admin-download/<string:type>/<string:filename>', methods=['GET'])
def admin_download(type, filename):
    if type == 'customer-uploaded-file':
        if os.path.isfile(os.path.join(current_app.config.get('UPLOAD_FILES_PATH'), filename)):
            return send_from_directory(current_app.config.get('UPLOAD_FILES_PATH'), filename, as_attachment=True)
