# -*- coding:utf-8 -*-
"""
"""
__date__ = "31/07/2017"
__author__ = "zhaojm"


class WSServerEntity(object):
    def on_connect(self, request):
        # print("Client connecting: {0}".format(request.peer))
        # self._entity.on_connect(request)
        pass

    def on_open(self):
        # print("WebSocket connection open.")
        # self._entity.on_open()
        pass

    def on_message(self, payload, isBinary):
        # if isBinary:
        #     print("Binary message received: {0} bytes".format(len(payload)))
        # else:
        #     print("Text message received: {0}".format(payload.decode('utf8')))
        # self._entity.on_message(payload, isBinary)

        # echo back message verbatim
        # self.sendMessage(payload, isBinary)
        pass

    def on_close(self, wasClean, code, reason):
        # print("WebSocket connection closed: {0}".format(reason))
        # self._entity.on_close(wasClean, code, reason)
        pass


class WSClientEntity(object):
    def on_connect(self, response):
        # print("Server connected: {0}".format(response.peer))
        # self._entity.on_connect(response)
        pass

    def on_open(self):
        print("WebSocket connection open.")

        # def hello():
        #     self.sendMessage(u"Hello, world!".encode('utf8'))
        #     self.sendMessage(b"\x00\x01\x03\x04", isBinary=True)
        #     self.factory.reactor.callLater(1, hello)
        #
        # # start sending messages every second ..
        # hello()
        # self._entity.on_open()
        pass

    def on_message(self, payload, isBinary):
        # if isBinary:
        #     print("Binary message received: {0} bytes".format(len(payload)))
        # else:
        #     print("Text message received: {0}".format(payload.decode('utf8')))
        # self._entity.on_message(payload, isBinary)
        pass

    def on_close(self, wasClean, code, reason):
        # print("WebSocket connection closed: {0}".format(reason))
        # self._entity.on_close(wasClean, code, reason)
        pass
