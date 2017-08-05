# -*- coding:utf-8 -*-
"""
"""
__date__ = "05/08/2017"
__author__ = "zhaojm"

from frame.servers.tcp.tcp_entity import TcpEntity


class Entity(TcpEntity):
    def __init__(self):
        super(Entity, self).__init__()

    def init_rpc(self):
        from . import rpc
