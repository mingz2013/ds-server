# -*- coding:utf-8 -*-
"""
Created on 13/06/2017

@author: zhaojm
"""

from os import linesep

import stackless
from twisted.internet import reactor
from twisted.protocols.basic import LineReceiver

from channel import chan_client_to_command, chan_command_to_client
from client import ChatClientFactory


class CommandProtocol(LineReceiver):
    delimiter = linesep

    def connectionMade(self):
        stackless.tasklet(self.on_message_from_chan)()
        reactor.callLater(0, stackless.schedule)
        reactor.connectTCP('localhost', 8888, ChatClientFactory())
        self.transport.write('>>> ')

    def lineReceived(self, line):
        stackless.tasklet(self.on_message)(line)
        reactor.callLater(0, stackless.schedule)

    def on_message(self, line):
        chan_command_to_client.send(line)
        self.transport.write('>>> ')

    def on_message_from_chan(self):
        line = chan_client_to_command.receive()
        self.sendLine('Echo:' + line)
        self.transport.write('>>> ')
        stackless.tasklet(self.on_message_from_chan)()
        reactor.callLater(0, stackless.schedule)
