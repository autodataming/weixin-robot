# -*- coding: utf-8 -*-
# coding=utf-8
__author__ = 'ruidong.wang@tsingdata.com'

from app import db
from datetime import datetime

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ToUserName = db.Column(db.String(128))
    FromUserName = db.Column(db.VARCHAR(64))
    CreateTime = db.Column(db.DateTime,default=datetime.now)
    MsgType = db.Column(db.String(32))
    Content = db.Column(db.VARCHAR(512))
    PicUrl = db.Column(db.Text)  #图片链接（由系统生成）
    MediaId = db.Column(db.VARCHAR(128)) #图片消息媒体id，可以调用多媒体文件下载接口拉取数据。
    Format = db.Column(db.String(16))#语音格式，如amr，speex等
    Title = db.Column(db.VARCHAR(32)) #消息标题
    Description = db.Column(db.VARCHAR(512)) #消息描述
    Url = db.Column(db.Text) #消息链接
    MsgId =  db.Column(db.VARCHAR(64))

    def __repr__(self):
        return self.MsgType


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    avatar = db.Column(db.String(512))
    password = db.Column(db.String(30), index=True)
    last_seen = db.Column(db.DateTime)
    active = db.Column(db.Boolean(), default=True)

    @property
    def is_authenticated(self):
        return self.active

    @property
    def is_active(self):
        return self.active

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def get_auth_token(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):  # pragma: no cover
        return '<User %r>' % (self.username)

class Trained(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    conversation = db.Column(db.String(512), index=True)
    add_time = db.Column(db.DateTime,default=datetime.now)

    def __repr__(self):  # pragma: no cover
        return self.conversation


class AimlData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    create_time = db.Column(db.DateTime)
    is_deleted = db.Column(db.Integer,default=0)
    last_modify_time = db.Column(db.DateTime)
    question = db.Column(db.String(512))
    replay = db.Column(db.String(512))
    label =  db.Column(db.String(256))


    @staticmethod


    def __repr__(self):  # pragma: no cover
        return self.question

