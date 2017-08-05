# -*- coding:utf-8 -*-
"""
"""
__date__ = "05/08/2017"
__author__ = "zhaojm"

from frame.core import reactor
from frame.entity.ws_server import WSServer


class WSConnector(WSServer):
    def __init__(self, entity):
        self._entity = entity
        self.conn = None
        pass

    def on_connect(self, request):
        pass

    def on_open(self):
        pass

    def on_message(self, payload, isBinary):
        pass

    def on_close(self, wasClean, code, reason):
        pass

    def init_connector(self, ip, port, url):
        reactor.init_ws_client(self, ip, port, url)
        pass
