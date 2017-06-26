# -*- coding:utf-8 -*-
'''
Created on 26/06/2017

http服务, 客户端首先登陆这个地址, 简单验证client_id, 然后连接数据库, 选择一个login server发送给客户端


@author: zhaojm
'''

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
