# -*- coding: utf-8 -*-
# coding=utf-8
__author__ = 'ruidong.wang@tsingdata.com'

import hashlib
import xml.etree.ElementTree as ET
import logging
import time
from app import app
from flask import request,render_template

class Rec_Msg(object):
    def __init__(self, xmlData):
        self.ToUserName = xmlData.find('ToUserName').text
        self.FromUserName = xmlData.find('FromUserName').text
        self.CreateTime = xmlData.find('CreateTime').text
        self.MsgType = xmlData.find('MsgType').text
        self.MsgId = xmlData.find('MsgId').text

class Rec_TextMsg(Rec_Msg):
    def __init__(self, xmlData):
        Rec_Msg.__init__(self, xmlData)
        self.Content = xmlData.find('Content').text.encode("utf-8")

class Rec_ImageMsg(Rec_Msg):
    def __init__(self, xmlData):
        Rec_Msg.__init__(self, xmlData)
        self.PicUrl = xmlData.find('PicUrl').text


class Reply_Msg(object):
    def __init__(self):
        pass

    def send(self):
        return "success"


class Reply_TextMsg(Reply_Msg):
    def __init__(self, toUserName, fromUserName, content):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Content'] = content

    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{Content}]]></Content>
        </xml>
        """
        return XmlForm.format(**self.__dict)


class Reply_ImageMsg(Reply_Msg):
    def __init__(self, toUserName, fromUserName, mediaId):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['MediaId'] = mediaId

    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[image]]></MsgType>
        <Image>
        <MediaId><![CDATA[{MediaId}]]></MediaId>
        </Image>
        </xml>
        """


@app.route("/")
def home():
    return render_template('home.html')


'''获取token只用于验证开发者服务器'''
@app.route('/wx', methods=['GET','POST'])
def verify_server():
    if request.method == 'GET':
        signature = request.args.get('signature' , "")
        timestamp = request.args.get("timestamp" , "")
        nonce = request.args.get("nonce" , "")
        echostr = request.args.get("echostr" , "")
        token = "wangruidong940853815"
        list = [token , timestamp , nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update , list)
        hashcode = sha1.hexdigest()

        if hashcode == signature:
            return echostr
        else:
            return ""
    if request.method == 'POST':
        web_data = request.data
        rec_msg = parse_xml(web_data)
        '''接受文本消息&被动回复文本消息'''
        if isinstance(rec_msg, Rec_Msg) and rec_msg.MsgType == 'text':
            to_user = rec_msg.FromUserName
            from_user = rec_msg.ToUserName
            content = rec_msg.Content
            replyMsg = Reply_TextMsg(to_user, from_user, content)
            return replyMsg.send()



def parse_xml(web_data):
    if len(web_data) == 0:
        return None
    xmlData = ET.fromstring(web_data)
    msg_type = xmlData.find('MsgType').text
    if msg_type == 'text':
        return Rec_TextMsg(xmlData)
    elif msg_type == 'image':
        return Rec_ImageMsg(xmlData)

        return XmlForm.format(**self.__dict)