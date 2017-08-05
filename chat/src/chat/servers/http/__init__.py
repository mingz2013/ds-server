# -*- coding:utf-8 -*-
"""
"""
__date__ = "30/07/2017"
__author__ = "zhaojm"

from flask import Flask

app = Flask(__name__)

from frame.core import reactor


# def init_server(ip, port, route):
#     from .rpc import *
#     reactor.init_http_server(app, ip, port, route)


def init_server(cfg):
    from .rpc import *
    reactor.init_http_server(app, cfg['ip'], cfg['port'], cfg['route'])
