# -*- coding:utf-8 -*-
'''
Created on 13/06/2017

@author: zhaojm
'''

from os import linesep

import stackless
from twisted.internet import reactor
from twisted.protocols import basic

from channel import chan_command_and_client
from client import ChatClientFactory


class CommandProtocol(basic.LineReceiver):
    delimiter = linesep

    def connectionMade(self):
        stackless.tasklet(self.on_message_from_chan)()
        reactor.callLater(0, stackless.schedule)
        reactor.connectTCP('localhost', 8888, ChatClientFactory())
        self.transport.write('>>> ')

    def lineReceived(self, line):
        print "command linereceived"
        stackless.tasklet(self.on_message)(line)
        reactor.callLater(0, stackless.schedule)

    def on_message(self, line):
        print "on message"
        chan_command_and_client.send(line)

    def on_message_from_chan(self):
        print "on message from chan"
        line = chan_command_and_client.receive()
        self.sendLine('Echo:' + line + '\n')
        self.transport.write('>>> ')
