# -*- coding:utf-8 -*-
'''
Created on 10/06/2017

@author: zhaojm
'''

from sys import stdout

from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet import reactor


class Echo(Protocol):
    def connectionMade(self):
        self.transport.write('hello')

    def dataReceived(self, data):
        print '.....'
        print data
        # stdout.write(data)


class EchoClientFactory(ClientFactory):
    def startedConnecting(self, connector):
        print('Started to connect.')

    def buildProtocol(self, addr):
        print('Connected.')
        return Echo()

    def clientConnectionLost(self, connector, reason):
        print('Lost connection.  Reason:', reason)

    def clientConnectionFailed(self, connector, reason):
        print('Connection failed. Reason:', reason)


reactor.connectTCP('localhost', 8888, EchoClientFactory())
reactor.run()
