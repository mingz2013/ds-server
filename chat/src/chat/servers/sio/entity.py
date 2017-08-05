# -*- coding:utf-8 -*-
"""
Created on 26/06/2017

@author: zhaojm
"""

from frame.servers.tcp.tcp_entity import TcpEntity


class Entity(TcpEntity):
    def __init__(self):
        super(Entity, self).__init__()

    def init_rpc(self):
        from .rpc import *
