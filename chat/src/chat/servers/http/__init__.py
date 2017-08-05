# -*- coding:utf-8 -*-
"""
"""
__date__ = "30/07/2017"
__author__ = "zhaojm"

from flask import Flask

app = Flask(__name__)


def init_server():
    from .rpc import *
