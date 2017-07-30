# -*- coding:utf-8 -*-
"""
Created on 17/06/2017

@author: zhaojm
"""

from os import linesep

import stackless
from twisted.internet import reactor
from twisted.internet.protocol import connectionDone
from twisted.protocols.basic import LineReceiver

class BaseProtocol(LineReceiver):
    def __init__(self, entity):
        self._entity = entity  # 实体业务逻辑
        self.tag = None  # 做个标记, 可在外部用于区分和索引protocol
        pass

    def rawDataReceived(self, data):
        """
        Override this for when raw data is received.
        """


    def connectionMade(self):
        stackless.tasklet(self.on_conn_made)()
        reactor.callLater(0, stackless.schedule)

    def connectionLost(self, reason=connectionDone):
        stackless.tasklet(self.on_conn_lost)(reason)
        reactor.callLater(0, stackless.schedule)

    def lineReceived(self, line):
        stackless.tasklet(self.on_msg)(line)
        reactor.callLater(0, stackless.schedule)

    def on_conn_made(self):
        self._entity.on_conn_made(self)

    def on_conn_lost(self, reason):
        self._entity.on_conn_lost(self, reason)

    def on_msg(self, msg):
        self._entity.on_msg(self, msg)


class StandardIOProtocol(BaseProtocol):
    delimiter = linesep


from autobahn.twisted.websocket import WebSocketServerProtocol, WebSocketClientProtocol


class BaseWebSocketServerProtocol(WebSocketServerProtocol):
    def __init__(self, entity):
        self._entity = entity
        super(BaseWebSocketServerProtocol).__init__()

    def onConnect(self, request):
        # print("Client connecting: {0}".format(request.peer))
        self._entity.on_connect(request)

    def onOpen(self):
        # print("WebSocket connection open.")
        self._entity.on_open()

    def onMessage(self, payload, isBinary):
        # if isBinary:
        #     print("Binary message received: {0} bytes".format(len(payload)))
        # else:
        #     print("Text message received: {0}".format(payload.decode('utf8')))
        self._entity.on_message(payload, isBinary)

        # echo back message verbatim
        # self.sendMessage(payload, isBinary)

    def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed: {0}".format(reason))
        self._entity.on_close(wasClean, code, reason)


class BaseWebSocketClientProtocol(WebSocketClientProtocol):
    def __init__(self, entity):
        self._entity = entity
        super(WebSocketClientProtocol, self).__init__()

    def onConnect(self, response):
        # print("Server connected: {0}".format(response.peer))
        self._entity.on_connect(response)

    def onOpen(self):
        print("WebSocket connection open.")

        # def hello():
        #     self.sendMessage(u"Hello, world!".encode('utf8'))
        #     self.sendMessage(b"\x00\x01\x03\x04", isBinary=True)
        #     self.factory.reactor.callLater(1, hello)
        #
        # # start sending messages every second ..
        # hello()
        self._entity.on_open()

    def onMessage(self, payload, isBinary):
        # if isBinary:
        #     print("Binary message received: {0} bytes".format(len(payload)))
        # else:
        #     print("Text message received: {0}".format(payload.decode('utf8')))
        self._entity.on_message(payload, isBinary)

    def onClose(self, wasClean, code, reason):
        # print("WebSocket connection closed: {0}".format(reason))
        self._entity.on_close(wasClean, code, reason)
