# -*- coding:utf-8 -*-
'''
Created on 15/06/2017

@author: zhaojm
'''
from twisted.internet.protocol import Factory, ClientFactory

from protocols import BaseProtocol


class BaseFactory(Factory):
    def __init__(self, entity):
        self.entity = entity

    def buildProtocol(self, addr):
        # return self.protocol(self.entity)
        return BaseProtocol(self.entity)


class BaseClientFactory(ClientFactory):
    def __init__(self, entity):
        self.entity = entity

    def buildProtocol(self, addr):
        return BaseProtocol(self.entity)

    def clientConnectionFailed(self, connector, reason):
        # 客户端连接失败
        connector.connect()  # 一般在连接失败时用于重新连接
        pass

    def clientConnectionLost(self, connector, reason):
        # 连接断开
        connector.stopConnection()  # 关闭会话
        pass

    def startedConnecting(self, connector):
        # 连接建立成功时
        pass
