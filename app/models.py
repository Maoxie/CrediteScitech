# _*_ coding: utf-8 _*_
__author__ = 'maoxie'
__date__ = '2017/9/13 21:31'

from app import db
from sqlalchemy.sql import func
from flask_login import UserMixin
from . import login_manager
from werkzeug.security import generate_password_hash, check_password_hash


class MainCustomerUploadFile(db.Model):
    __tablename__ = 'customer_upload_files'
    id = db.Column(db.Integer, primary_key=True)
    customerName = db.Column(db.String(20))
    customerPhoneNumber = db.Column(db.String(20), nullable=True)
    customerEmail = db.Column(db.String(50), nullable=True)
    uploadFileName = db.Column(db.String(256))
    storageFileName = db.Column(db.String(256))
    # 条目的更新时间。每次更新条目的时候，本字段会自动更新时间戳
    updateTime = db.Column(db.TIMESTAMP(True), nullable=False)
    # 条目的创建时间。每次更新条目的时候，本字段不会自动更新时间戳
    createTime = db.Column(db.TIMESTAMP(True), nullable=False, server_default=func.now())

    def __repr__(self):
        return "<姓名: {name}>\n<联系电话: {phone}>\n<联系邮箱: {email}>\n<上传文件: {filename}>\n<上传时间: {time}>".format(
            name=self.customerName,
            phone=self.customerPhoneNumber,
            email=self.customerEmail,
            filename=self.uploadFileName,
            time=self.updateTime
        )


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(64))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __init__(self, username, email, password, role):
        super(User, self).__init__()
        self.username = username
        self.email = email
        self.password = password
        if role is None:
            self.role_id = Role.query.filter_by(defualt=True).first().id
        else:
            self.role_id = Role.query.filter_by(name=role).first().id

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {0}>'.format(self.username)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    @staticmethod
    def insert_roles():
        roles = {
            'User': (0x00, True),
            'Administrator': (0xff, False)  # 具有全部权限
        }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()

    def __repr__(self):
        return '<Role {0}>'.format(self.name)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
