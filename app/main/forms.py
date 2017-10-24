# _*_ coding: utf-8 _*_
__author__ = 'maoxie'
__date__ = '2017/9/13 21:30'

from flask_wtf import Form
from wtforms import StringField, FileField, SubmitField
from wtforms.validators import DataRequired, Regexp, Email


class MainCustomerUploadFileForm(Form):
    customerName = StringField(u'您的姓名', validators=[DataRequired()])
    customerPhoneNumber = StringField(u'联系电话', validators=[Regexp(r'[-0-9 ]')])
    customerEmail = StringField(u'联系邮箱', validators=[Email()])
    uploadFile = FileField(u'上传文件')
    submit = SubmitField(u'提交')
