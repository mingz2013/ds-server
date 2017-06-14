# -*- coding:utf-8 -*-
'''
Created on 10/06/2017

@author: zhaojm
'''

import stackless
from twisted.internet import protocol, reactor


class ChatServerProtocol(protocol.Protocol):
    def connectionMade(self):
        print "made"
        pass

    def dataReceived(self, data):
        stackless.tasklet(self.on_message)(data)
        reactor.callLater(0, stackless.schedule)

    def on_message(self, data):
        print "on message..."
        print data
        self.transport.write(data)
        print 'after write'


class ChatServerFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return ChatServerProtocol()
