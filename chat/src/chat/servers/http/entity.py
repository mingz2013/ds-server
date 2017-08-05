# -*- coding:utf-8 -*-
"""
Created on 26/06/2017

用于提供http服务,

静态页面服务

静态文件服务, 图片, 压缩包等

后台管理功能

@author: zhaojm
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'My Twisted Flask Index'
