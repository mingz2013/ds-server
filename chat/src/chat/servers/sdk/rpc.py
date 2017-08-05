# -*- coding:utf-8 -*-
"""
"""
__date__ = "05/08/2017"
__author__ = "zhaojm"

from chat.servers.sdk import app


@app.route('/')
def index():
    return 'index'


@app.route('/login')
def login():
    return "login"


@app.route('/register')
def register():
    return "register"
