# -*- coding:utf-8 -*-
'''
Created on 19/06/2017

@author: zhaojm
'''

import stackless
from twisted.internet import reactor, stdio
# from twisted.web.resource import Resource
# from twisted.web.proxy import ReverseProxyResource
# from twisted.application import internet, service, strports
# from twisted.web import static, server
# from twisted.web.resource import Resource
# from twisted.web.server import Site
from twisted.web.wsgi import WSGIResource
from factories import BaseFactory, BaseClientFactory
from protocols import StandardIOProtocol


def init_server(entity, ip, port):
    reactor.listenTCP(port, BaseFactory(entity))


def init_http_server(app):
    # root = Resource()
    flask_site = WSGIResource(reactor, reactor.getThreadPool(), app)
    # root.putChild('api', flask_site)
    # static_file = static.File("webroot")
    # root.putChild('static', static_file)
    reactor.listenTCP(80, flask_site)


def init_ws_server():
    pass


def init_sio_server():
    pass


def init_http_client():
    pass


def init_ws_client():
    pass


def init_sio_client():
    pass


def init_stdio(entity):
    stdio.StandardIO(StandardIOProtocol(entity))


def init_client(entity, ip, port):
    reactor.connectTCP(ip, port, BaseClientFactory(entity))


def start_reactor():
    stackless.tasklet(reactor.run)()
    reactor.callLater(0, stackless.schedule)
    stackless.run()
