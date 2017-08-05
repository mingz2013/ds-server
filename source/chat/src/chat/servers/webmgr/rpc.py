# -*- coding:utf-8 -*-
"""
"""
__date__ = "05/08/2017"
__author__ = "zhaojm"

from chat.servers.webmgr import app


@app.route('/')
def index():
    return 'My Twisted Flask Index'
