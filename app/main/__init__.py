# _*_ coding: utf-8 _*_
__author__ = 'maoxie'
__date__ = '2017/9/13 21:30'

from flask import Blueprint
from config import Config

main = Blueprint('main', __name__, static_folder=Config.STATIC_FOLDER)

from . import views, errors




