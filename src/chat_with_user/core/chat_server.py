# -*- coding:utf-8 -*-
'''
Created on 10/06/2017

@author: zhaojm
'''

import stackless
from twisted.internet import reactor
from twisted.internet.protocol import connectionDone
from twisted.protocols.basic import LineReceiver


class ChatServer(LineReceiver):
    def __init__(self, chat):
        self.chat = chat

    def connectionMade(self):
        pass

    def connectionLost(self, reason=connectionDone):
        pass

    def lineReceived(self, line):
        stackless.tasklet(self.parse_msg)(line)
        reactor.callLater(0, stackless.schedule)

    def parse_msg(self, line):
        pass



