# -*- coding:utf-8 -*-
"""
"""
__date__ = "05/08/2017"
__author__ = "zhaojm"
from .entity import Entity

e = Entity()


# def init_server(ip, port):
#     e.init_rpc()
#     e.init_acceptor(ip, port)

def init_server(cfg):
    e.init_rpc()
    e.init_acceptor(cfg['ip'], cfg['port'])
