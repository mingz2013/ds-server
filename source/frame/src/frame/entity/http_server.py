# -*- coding:utf-8 -*-
"""
"""
__date__ = "31/07/2017"
__author__ = "zhaojm"

from flask import Flask

app = Flask(__name__)


@app.route('/example1')
def index():
    return 'My Twisted Flask'
