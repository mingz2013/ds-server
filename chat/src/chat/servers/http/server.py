# -*- coding:utf-8 -*-
'''
Created on 26/06/2017

用于提供http服务,

静态页面服务

静态文件服务, 图片, 压缩包等

后台管理功能


@author: zhaojm
'''
from frame.entity.base_server import BaseServer
from flask import Flask
from twisted.internet import reactor

from flask import Flask

app = Flask(__name__)


@app.route('/index')
def index():
    return 'index'


@app.route('/login')
def login():
    pass


@app.route('/register')
def register():
    pass
