# -*- coding:utf-8 -*-
'''
Created on 13/06/2017

@author: zhaojm
'''

import stackless
from twisted.internet import stdio, reactor
from twisted.protocols import basic
from channel import chan_command_and_client
from client import ChatClientFactory


class CommandProtocol(basic.LineReceiver):
    def connectionMade(self):
        stackless.tasklet(self.on_message_from_chan)()
        reactor.connectTCP('localhost', 8888, ChatClientFactory())
        self.transport.write('>>> ')

    def lineReceived(self, line):
        stackless.tasklet(self.on_message)(line)
        reactor.callLater(0, stackless.schedule)

    def on_message(self, line):
        chan_command_and_client.send(line)
        reactor.callLater(0, stackless.schedule)

    def on_message_from_chan(self):
        line = chan_command_and_client.receive()
        self.sendLine('Echo:' + line + '\n')
        self.transport.write('>>> ')
        reactor.callLater(0, stackless.schedule)
