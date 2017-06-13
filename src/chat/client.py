# -*- coding:utf-8 -*-
'''
Created on 10/06/2017

@author: zhaojm
'''

import stackless
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, ClientFactory


class ChatClient(Protocol):
    def connectionMade(self):
        self.transport.write('123')

    def dataReceived(self, data):
        stackless.tasklet(self.on_message)(data)
        reactor.callLater(0, stackless.schedule)

    def on_message(self, data):
        self.transport.write(data)
        pass


class ChatClientFactory(ClientFactory):
    def buildProtocol(self, addr):
        return ChatClient()


reactor.connectTCP('localhost', 8888, ChatClientFactory())

stackless.tasklet(reactor.run)()
reactor.callLater(0, stackless.schedule)
stackless.run()
