# -*- coding:utf-8 -*-
"""
"""
__date__ = "05/08/2017"
__author__ = "zhaojm"



from frame.servers.ws.ws_entity import WSEntity

e = WSEntity()


def init_server(ip, port, url):
    e.init_rpc()
    e.init_acceptor(ip, port, url)
