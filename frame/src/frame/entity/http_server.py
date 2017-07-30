# -*- coding:utf-8 -*-
"""
"""
__date__ = "31/07/2017"
__author__ = "zhaojm"

from flask import Flask
from twisted.web.server import Site
from twisted.web.wsgi import WSGIResource
from twisted.internet import reactor
from twisted.web.proxy import ReverseProxyResource
from twisted.web.resource import Resource

app = Flask(__name__)


@app.route('/example1')
def index():
    return 'My Twisted Flask'
