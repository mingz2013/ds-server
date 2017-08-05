# -*- coding:utf-8 -*-
"""
Created on 19/06/2017

@author: zhaojm
"""

import stackless
from twisted.internet import stdio

from factories import BaseFactory, BaseClientFactory, BaseWebSocketServerFactory, BaseWebSocketClientFactory
from protocols import StandardIOProtocol

from flask import Flask
from twisted.web.server import Site
from twisted.web.wsgi import WSGIResource
from twisted.internet import reactor
from twisted.web.proxy import ReverseProxyResource
from twisted.web.resource import Resource
from twisted.web.static import File


def init_tcp_server(entity, ip, port):
    reactor.listenTCP(port, BaseFactory(entity), interface=ip)


def init_tcp_client(entity, ip, port):
    reactor.connectTCP(ip, port, BaseClientFactory(entity))


def init_udp_server(entity, ip, port):
    pass


def init_udp_client(entity, ip, port):
    pass


def init_ws_server(entity, ip, port, url):
    # print ip, port, url
    reactor.listenTCP(port, BaseWebSocketServerFactory(entity, url), interface=ip)

    pass


def init_ws_client(entity, ip, port, url):
    reactor.connectTCP(ip, port, BaseWebSocketClientFactory(entity, url=url))
    pass


def init_sio_server(entity, ip, port, url):
    pass


def init_sio_client():
    pass


def init_http_server(app, ip, port, route, static_path=None):
    # reactor.listenTCP(port, BaseHTTPFactory(entity), interface=ip)

    print ip, port, route

    flask_site = WSGIResource(reactor, reactor.getThreadPool(), app)

    root = Resource()
    root.putChild(route, flask_site)
    if static_path:
        root.putChild('static', File(static_path))

    # site_example = ReverseProxyResource('www.example.com', 80, ''.encode('utf-8'))
    # root.putChild('example1', site_example)


    # site_example = ReverseProxyResource('www.example.com', 80, '/')
    # root.putChild('example', site_example)

    reactor.listenTCP(port, Site(root), interface=ip)
    pass

def init_http_client():
    pass


def init_stdio(entity):
    stdio.StandardIO(StandardIOProtocol(entity))


def start_reactor():
    stackless.tasklet(reactor.run)()
    reactor.callLater(0, stackless.schedule)
    stackless.run()
