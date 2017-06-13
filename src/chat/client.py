# -*- coding:utf-8 -*-
'''
Created on 10/06/2017

@author: zhaojm
'''

from sys import stdout
from twisted.internet import reactor


from twisted.internet.protocol import Protocol, ClientFactory


class ChatClient(Protocol):
    def connectionMade(self):
        self.transport.write('123')
        self.transport.write('456')

    def dataReceived(self, data):
        print data


class ChatClientFactory(ClientFactory):

    def buildProtocol(self, addr):
        print('Connected.')
        return ChatClient()


reactor.connectTCP('localhost', 8888, ChatClientFactory())
reactor.run()
