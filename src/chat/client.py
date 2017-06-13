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
        stackless.tasklet(self.on_message_from_chan)()
        reactor.callLater(0, stackless.schedule)
        chan_command_and_client.send("connet success")

    def dataReceived(self, data):
        print "client data received"
        stackless.tasklet(self.on_message)(data)
        reactor.callLater(0, stackless.schedule)

    def on_message(self, data):
        print "client on message"
        chan_command_and_client.send(data)
        # reactor.callLater(0, stackless.schedule)

    def on_message_from_chan(self):
        print "on message from chan in client"
        line = chan_command_and_client.receive()
        print "on message from chan in client"
        self.transport.write(line)
        # reactor.callLater(0, stackless.schedule)


class ChatClientFactory(ClientFactory):
    def buildProtocol(self, addr):
        return ChatClient()



