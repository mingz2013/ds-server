# -*- coding:utf-8 -*-
"""
"""
__date__ = "05/08/2017"
__author__ = "zhaojm"

from frame.servers.ws.ws_entity import WSEntity


class Entity(WSEntity):

    def init_rpc(self):
        from . import rpc
        pass
