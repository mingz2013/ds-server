# -*- coding:utf-8 -*-
'''
Created on 10/06/2017

@author: zhaojm
'''

import stackless
from twisted.internet import reactor
from twisted.internet.protocol import Factory
from twisted.internet.protocol import connectionDone
from twisted.protocols.basic import LineReceiver


class ChatServerProtocol(LineReceiver):
    def __init__(self, users):
        self.users = users
        self.name = None
        self.state = "GETNAME"

    def connectionMade(self):
        # print "conn made"
        self.sendLine("What's your name?")

    def connectionLost(self, reason=connectionDone):
        if self.users.has_key(self.name):
            del self.users[self.name]
            print "%s lost chat" % self.name

    def lineReceived(self, line):
        if self.state == "GETNAME":
            stackless.tasklet(self.on_name)(line)
        else:
            stackless.tasklet(self.on_message)(line)
        reactor.callLater(0, stackless.schedule)

    def on_name(self, name):
        if self.users.has_key(name):
            self.sendLine("Name taken, please choose another..")
            return
        self.sendLine("Welcome, %s" % name)
        self.name = name
        self.users[name] = self
        self.state = "CHAT"
        print "%s add to chat" % name

    def on_message(self, message):
        message = "<%s> %s" % (self.name, message)
        for name, protocol in self.users.iteritems():
            if protocol != self:
                protocol.sendLine(message)


class ChatServerFactory(Factory):
    def __init__(self):
        self.users = {}

    def buildProtocol(self, addr):
        # print "build protocol"
        return ChatServerProtocol(self.users)
