# -*- coding:utf-8 -*-
"""
"""
__date__ = "05/08/2017"
__author__ = "zhaojm"

from frame.servers.rpc.rpc_acceptor import RpcAcceptor


from frame.servers.rpc.rpc_mixin import RpcMixin


class RpcEntity(RpcMixin):
    Acceptor = RpcAcceptor

    def __init__(self):
        super(RpcEntity).__init__()
        self._acceptor = RpcAcceptor(self)
        pass

    def init_rpc(self):
        from rpc import *
        pass

    def start_acceptor(self, ip, port):
        self._acceptor.init_acceptor(ip, port)
