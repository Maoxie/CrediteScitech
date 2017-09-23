# _*_ coding: utf-8 _*_
__author__ = 'maoxie'
__date__ = '2017/9/13 21:31'

from app import db


class ProfessionField(db.Model):
    __tablename__ = 'profession_fields'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    introduction = db.Column(db.text)
    items = db.Column(db.relationship)

    def __repr__(self):
        return '<Profession field: %r>' % self.name

