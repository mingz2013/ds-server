# -*- coding:utf-8 -*-
"""
"""
__date__ = "05/08/2017"
__author__ = "zhaojm"

from frame.servers.ws.ws_acceptor import WSAcceptor
from frame.servers.rpc.rpc_mixin import RpcMixin


class WSEntity(RpcMixin):
    Acceptor = WSAcceptor

    def __init__(self):
        super(WSEntity, self).__init__()
        self._acceptor = self.Acceptor(self)
        pass

    def init_rpc(self):
        from .rpc import *
        pass

    def init_acceptor(self, ip, port, url):
        self._acceptor.init_acceptor(ip, port, url)
