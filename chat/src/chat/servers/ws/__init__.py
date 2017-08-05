# -*- coding:utf-8 -*-
"""
"""
__date__ = "30/07/2017"
__author__ = "zhaojm"

from chat.servers.ws.entity import Entity

e = Entity()


def init_server():
    e.init_rpc()
    e.init_acceptor("127.0.0.1", 8000, u"ws://127.0.0.1:8080")
