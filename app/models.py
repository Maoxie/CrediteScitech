# _*_ coding: utf-8 _*_
__author__ = 'maoxie'
__date__ = '2017/9/13 21:31'

from app import db
from sqlalchemy.sql import func


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

