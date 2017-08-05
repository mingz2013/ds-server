# -*- coding:utf-8 -*-
"""
Created on 26/06/2017

用于接收ws连接, 并转换到其他服务器

@author: zhaojm
"""
from frame.entity.ws_server import WSServer


class Server(WSServer):
    def __init__(self):
        super(Server, self).__init__()

    def on_connect(self, request):
        pass

    def on_open(self):
        pass

    def on_message(self, payload, isBinary):
        pass

    def on_close(self, wasClean, code, reason):
        pass
