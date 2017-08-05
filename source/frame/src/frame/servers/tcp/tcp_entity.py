# -*- coding:utf-8 -*-
"""
"""
__date__ = "05/08/2017"
__author__ = "zhaojm"

from frame.servers.tcp.tcp_acceptor import TcpAcceptor
from frame.entity.rpc_mixin import RpcMixin


class TcpEntity(RpcMixin):
    Acceptor = TcpAcceptor

    def __init__(self):
        super(TcpEntity, self).__init__()
        self._acceptor = self.Acceptor(self)
        pass

    def init_rpc(self):
        from rpc import *
        pass

    def init_acceptor(self, ip, port):
        self._acceptor.init_acceptor(ip, port)
