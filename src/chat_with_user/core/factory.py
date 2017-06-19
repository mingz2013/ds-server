# -*- coding:utf-8 -*-
'''
Created on 15/06/2017

@author: zhaojm
'''
from twisted.internet.protocol import Factory
from protocols import TcpClientProtocol, TcpServerProtocol, CmdHandlerProtocol
from twisted.internet import reactor, stdio


class TcpServerFactory(Factory):
    def __init__(self, entity):
        self.entity = entity

    def buildProtocol(self, addr):
        return TcpServerProtocol(self.entity)


def init_server(entity):
    reactor.listenTCP(8888, TcpServerFactory(entity))


def init_cmd_handler(entity):
    stdio.StandardIO(CmdHandlerProtocol(entity))


def init_client(entity):
    pass
