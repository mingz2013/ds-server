# -*- coding:utf-8 -*-
"""
"""
__date__ = "30/07/2017"
__author__ = "zhaojm"

from chat.servers.gate.entity import Entity

e = Entity()


def init_server(ip, port):
    e.init_rpc()
    e.start_acceptor(ip, port)
