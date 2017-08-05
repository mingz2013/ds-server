# -*- coding:utf-8 -*-
"""
"""
__date__ = "05/08/2017"
__author__ = "zhaojm"

from frame.servers.rpc.rpc_entity import RpcEntity
from chat.servers.gate.connector import Connector

class Entity(RpcEntity):
    def __init__(self):
        super(Entity, self).__init__()
        self._connector = Connector(self)

    def init_rpc(self):
        from .rpc import *
