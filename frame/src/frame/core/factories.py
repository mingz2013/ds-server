# -*- coding:utf-8 -*-
"""
Created on 15/06/2017

@author: zhaojm
"""
from twisted.internet.protocol import Factory, ClientFactory
from twisted.web.http import HTTPFactory
from twisted.web.server import Site
from autobahn.twisted.websocket import WebSocketServerFactory, WebSocketClientFactory

from protocols import BaseProtocol, BaseWebSocketServerProtocol, BaseWebSocketClientProtocol


class BaseFactory(Factory):
    def __init__(self, entity):
        self._entity = entity

    def buildProtocol(self, addr):
        # return self.protocol(self.entity)
        return BaseProtocol(self._entity)


class BaseClientFactory(ClientFactory):
    def __init__(self, entity):
        self._entity = entity

    def buildProtocol(self, addr):
        return BaseProtocol(self._entity)

    def clientConnectionFailed(self, connector, reason):
        # 客户端连接失败
        # connector.connect()  # 一般在连接失败时用于重新连接
        pass

    def clientConnectionLost(self, connector, reason):
        # 连接断开
        # connector.stopConnection()  # 关闭会话
        pass

    def startedConnecting(self, connector):
        # 连接建立成功时
        pass


# class BaseSite(Site):
#     def __init__(self, entity):
#         super(BaseSite, self).__init__()
#         self._entity = entity
#
#     def buildProtocol(self, addr):
#         return BaseProtocol(self._entity)


class BaseWebSocketServerFactory(WebSocketServerFactory):
    def __init__(self, entity, *args, **kwargs):
        super(BaseWebSocketServerFactory).__init__(*args, **kwargs)
        self._entity = entity
        # self.protocol = protocol

    def buildProtocol(self, addr):
        return BaseWebSocketServerProtocol(self._entity)
        pass


class BaseWebSocketClientFactory(WebSocketClientFactory):
    def __init__(self, entity, *args, **kwargs):
        super(BaseWebSocketClientFactory).__init__(*args, **kwargs)
        self._entity = entity
        # self.protocol = protocol

    def buildProtocol(self, addr):
        return BaseWebSocketClientProtocol(self._entity)
        pass
