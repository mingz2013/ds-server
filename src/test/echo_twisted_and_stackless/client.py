# -*- coding:utf-8 -*-
'''
Created on 10/06/2017

@author: zhaojm
'''

import stackless
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, ClientFactory

from channel import chan_client_to_command, chan_command_to_client


class ChatClient(Protocol):
    def connectionMade(self):
        stackless.tasklet(self.on_message_from_chan)()
        reactor.callLater(0, stackless.schedule)
        chan_client_to_command.send("connet success")

    def dataReceived(self, data):
        stackless.tasklet(self.on_message)(data)
        reactor.callLater(0, stackless.schedule)

    def on_message(self, data):
        chan_client_to_command.send(data)

    def on_message_from_chan(self):
        line = chan_command_to_client.receive()
        self.transport.write(line)
        stackless.tasklet(self.on_message_from_chan)()
        reactor.callLater(0, stackless.schedule)


class ChatClientFactory(ClientFactory):
    def buildProtocol(self, addr):
        return ChatClient()
