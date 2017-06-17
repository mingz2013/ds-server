# -*- coding:utf-8 -*-
'''
Created on 15/06/2017

@author: zhaojm
'''
from twisted.internet.protocol import Factory

from chat_server import ChatServerProtocol


class TcpServerFactory(Factory):
    def __init__(self, entity):
        self.entity = entity

    def buildProtocol(self, addr):
        return ChatServerProtocol(self.entity)
