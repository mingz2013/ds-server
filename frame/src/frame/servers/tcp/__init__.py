# -*- coding:utf-8 -*-
"""
"""
__date__ = "30/07/2017"
__author__ = "zhaojm"

from frame.servers.tcp.tcp_entity import TcpEntity

e = TcpEntity()


def init_server():
    e.init_rpc()
    e.init_acceptor("127.0.0.1", 8000)
