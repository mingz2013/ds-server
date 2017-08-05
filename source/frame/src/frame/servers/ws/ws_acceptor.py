# -*- coding:utf-8 -*-
"""
"""
__date__ = "05/08/2017"
__author__ = "zhaojm"

from frame.core import reactor
from frame.entity.ws_server import WSServer


class WSAcceptor(WSServer):
    def __init__(self, entity):
        self._entity = entity

    def on_connect(self, request):
        pass

    def on_open(self):
        pass

    def on_message(self, payload, isBinary):
        # m = Msg.from_msg(msg)
        # self._entity.rpc_handle(conn, msg.cmd, m)
        pass

    def on_close(self, wasClean, code, reason):
        pass

    def init_acceptor(self, ip, port, url):
        reactor.init_ws_server(self, ip, port, url)
