# -*- coding:utf-8 -*-
'''
Created on 09/06/2017

@author: zhaojm
'''

from sys import stdout

from twisted.internet.protocol import Protocol, ClientFactory


class Echo(Protocol):
    def dataReceived(self, data):
        stdout.write(data)


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
