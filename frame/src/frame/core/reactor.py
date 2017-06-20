# -*- coding:utf-8 -*-
'''
Created on 19/06/2017

@author: zhaojm
'''

import stackless
from twisted.internet import reactor, stdio

from factories import BaseFactory, BaseClientFactory
from protocols import StandardIOProtocol


def init_server(entity, ip, port):
    reactor.listenTCP(port, BaseFactory(entity))


def init_stdio(entity):
    stdio.StandardIO(StandardIOProtocol(entity))


def init_client(entity, ip, port):
    reactor.connectTCP(ip, port, BaseClientFactory(entity))


def start_reactor():
    stackless.tasklet(reactor.run)()
    reactor.callLater(0, stackless.schedule)
    stackless.run()
