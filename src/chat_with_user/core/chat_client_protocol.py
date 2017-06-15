# -*- coding:utf-8 -*-
'''
Created on 10/06/2017

@author: zhaojm
'''

import stackless
from twisted.internet import reactor

from twisted.protocols.basic import LineReceiver

from channel import chan_client_to_command, chan_command_to_client


class ChatClientProtocol(LineReceiver):
    def connectionMade(self):
        stackless.tasklet(self.on_message_from_command)()
        reactor.callLater(0, stackless.schedule)

    def lineReceived(self, line):
        stackless.tasklet(self.on_message)(line)
        reactor.callLater(0, stackless.schedule)

    def on_message(self, message):
        chan_client_to_command.send(message)

    def on_message_from_command(self):
        line = chan_command_to_client.receive()
        self.sendLine(line)
        stackless.tasklet(self.on_message_from_command)()
        reactor.callLater(0, stackless.schedule)
