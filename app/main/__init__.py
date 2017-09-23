# _*_ coding: utf-8 _*_
__author__ = 'maoxie'
__date__ = '2017/9/13 21:30'

from flask import Blueprint

main = Blueprint('main', __name__, static_folder='static')

from . import views, errors
try:
    import cPickle as pickle
except ImportError:
    import pickle



