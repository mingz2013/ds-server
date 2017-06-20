# -*- coding:utf-8 -*-
'''
Created on 15/06/2017

@author: zhaojm
'''
from twisted.internet import reactor, stdio
from twisted.internet.protocol import Factory, ClientFactory

from protocols import BaseProtocol, CmdHandlerProtocol


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
    reactor.listenTCP(8888, BaseClientFactory(entity))


def init_cmd_handler(entity):
    stdio.StandardIO(CmdHandlerProtocol(entity))


def conn_to_server(ip, port, entity):
    reactor.connectTCP(ip, port, BaseClientFactory(entity))
