# -*- coding:utf-8 -*-
"""
Created on 19/06/2017

@author: zhaojm
"""

import stackless
from twisted.internet import reactor, stdio

from factories import BaseFactory, BaseClientFactory, BaseWebSocketServerFactory, BaseWebSocketClientFactory
from protocols import StandardIOProtocol



def init_server(entity, ip, port):
    reactor.listenTCP(port, BaseFactory(entity), interface=ip)


def init_client(entity, ip, port):
    reactor.connectTCP(ip, port, BaseClientFactory(entity))


def init_ws_server(entity, ip, port, url):
    reactor.listenTCP(port, BaseWebSocketServerFactory(entity, url=url), interface=ip)

    pass


def init_ws_client(entity, ip, port, url):
    reactor.connectTCP(ip, port, BaseWebSocketClientFactory(entity, url=url))
    pass


def init_sio_server(entity, ip, port, url):
    pass


def init_sio_client():
    pass


def init_http_server(entity, ip, port):
    # reactor.listenTCP(port, BaseHTTPFactory(entity), interface=ip)
    pass

def init_http_client():
    pass


def init_stdio(entity):
    stdio.StandardIO(StandardIOProtocol(entity))


def start_reactor():
    stackless.tasklet(reactor.run)()
    reactor.callLater(0, stackless.schedule)
    stackless.run()
