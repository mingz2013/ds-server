# -*- coding:utf-8 -*-
'''
Created on 15/06/2017

@author: zhaojm
'''
from twisted.internet import reactor, stdio
from twisted.internet.protocol import Factory, ClientFactory

from protocols import BaseProtocol, StandardIOProtocol


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


def init_server(entity):
    reactor.listenTCP(8888, BaseFactory(entity))


def init_stdio(entity):
    stdio.StandardIO(StandardIOProtocol(entity))


def conn_to_server(entity, ip, port):
    reactor.connectTCP(ip, port, BaseClientFactory(entity))
