# -*- coding:utf-8 -*-
'''
Created on 13/06/2017

@author: zhaojm
'''

from os import linesep

import stackless
from twisted.internet import reactor
from twisted.protocols.basic import LineReceiver
from twisted.internet.protocol import ClientFactory
from channel import chan_client_to_command, chan_command_to_client
from chat_client import ChatClient


class CmdHandler(LineReceiver):
    delimiter = linesep

    def _connect_to_server(self):
        stackless.tasklet(self.on_message_from_client)()
        reactor.callLater(0, stackless.schedule)
        f = ClientFactory()
        f.protocol = ChatClient
        reactor.connectTCP('localhost', 8888, f)

    def connectionMade(self):
        self._connect_to_server()
        self.transport.write('>>> ')

    def lineReceived(self, line):
        # print "command line received"
        stackless.tasklet(self.parse_cmd)(line)
        reactor.callLater(0, stackless.schedule)

    def parse_cmd(self, line):
        chan_command_to_client.send(line)
        self.transport.write('>>> ')
        pass


    def on_message_from_client(self):
        line = chan_client_to_command.receive()
        self.sendLine(line)
        self.transport.write('>>> ')
        stackless.tasklet(self.on_message_from_client)()
        reactor.callLater(0, stackless.schedule)

