# -*- coding:utf-8 -*-
"""
"""
__date__ = "30/07/2017"
__author__ = "zhaojm"

from frame.servers.tcp.tcp_entity import TcpEntity

e = TcpEntity()


def init_server(ip, port):
    e.init_rpc()
    e.init_acceptor(ip, port)
