# -*- coding:utf-8 -*-
'''
Created on 26/06/2017

@author: zhaojm
'''

from flask import Flask

app = Flask(__name__)


@app.route('/example')
def index():
    return 'My Twisted Flask'
