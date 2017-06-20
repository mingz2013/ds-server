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
        return BaseProtocol(self.entity)


class BaseClientFactory(ClientFactory):
    def __init__(self, entity):
        self.entity = entity

    def buildProtocol(self, addr):
        return BaseProtocol(self.entity)
