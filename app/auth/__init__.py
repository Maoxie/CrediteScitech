# _*_ coding: utf-8 _*_
__author__ = 'maoxie'
__date__ = '2017/11/22 23:59'

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views