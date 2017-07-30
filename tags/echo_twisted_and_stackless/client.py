# -*- coding:utf-8 -*-
"""
Created on 10/06/2017

@author: zhaojm
"""

import stackless
from twisted.internet import reactor
from twisted.internet.protocol import ClientFactory
from twisted.protocols.basic import LineReceiver

from channel import chan_client_to_command, chan_command_to_client


class ChatClient(LineReceiver):
    def connectionMade(self):
        stackless.tasklet(self.on_message_from_chan)()
        reactor.callLater(0, stackless.schedule)
        chan_client_to_command.send("connet success")

    def lineReceived(self, line):
        stackless.tasklet(self.on_message)(line)
        reactor.callLater(0, stackless.schedule)

    def on_message(self, data):
        chan_client_to_command.send(data)

    def on_message_from_chan(self):
        line = chan_command_to_client.receive()
        self.sendLine(line)
        stackless.tasklet(self.on_message_from_chan)()
        reactor.callLater(0, stackless.schedule)


class ChatClientFactory(ClientFactory):
    def buildProtocol(self, addr):
        return ChatClient()
