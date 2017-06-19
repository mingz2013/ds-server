# -*- coding:utf-8 -*-
'''
Created on 15/06/2017

@author: zhaojm
'''
from twisted.internet.protocol import Factory, ClientFactory
from protocols import TcpClientProtocol, TcpServerProtocol, CmdHandlerProtocol
from twisted.internet import reactor, stdio


class TcpServerFactory(Factory):
    def __init__(self, entity):
        self.entity = entity

    def buildProtocol(self, addr):
        return TcpServerProtocol(self.entity)


class TcpClientFactory(ClientFactory):
    def __init__(self, entity):
        self.entity = entity

    def buildProtocol(self, addr):
        return TcpClientProtocol(self.entity)


def init_server(entity):
    reactor.listenTCP(8888, TcpServerFactory(entity))


def init_cmd_handler(entity):
    stdio.StandardIO(CmdHandlerProtocol(entity))


def conn_to_server(ip, port, entity):
    reactor.connectTCP(ip, port, TcpClientFactory(entity))
