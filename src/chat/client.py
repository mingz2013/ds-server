# -*- coding:utf-8 -*-
'''
Created on 10/06/2017

@author: zhaojm
'''

import stackless
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, ClientFactory
from channel import chan_command_and_client


class ChatClient(Protocol):
    def connectionMade(self):
        chan_command_and_client.send("connet success")

    def dataReceived(self, data):
        stackless.tasklet(self.on_message)(data)
        reactor.callLater(0, stackless.schedule)

    def on_message(self, data):
        chan_command_and_client.send(data)
        reactor.callLater(0, stackless.schedule)

    def on_message_from_chan(self):
        line = chan_command_and_client.receive()
        self.transport.write(line)
        reactor.callLater(0, stackless.schedule)


class ChatClientFactory(ClientFactory):
    def buildProtocol(self, addr):
        return ChatClient()



