# -*- coding:utf-8 -*-
"""
"""
__date__ = "05/08/2017"
__author__ = "zhaojm"


def init():
    from frame.entity import log
    log.init_logging()


from frame.servers.ws.ws_entity import WSEntity

e = WSEntity()


def init_server():
    e.init_rpc()
    e.init_acceptor("127.0.0.1", 8000, u"ws://127.0.0.1:8080")
