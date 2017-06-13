# -*- coding:utf-8 -*-
'''
Created on 13/06/2017

@author: zhaojm
'''

import stackless
from twisted.internet import stdio, reactor
from twisted.protocols import basic


class CommandProtocol(basic.LineReceiver):
    def connectionMade(self):
        self.transport.write('>>> ')

    def lineReceived(self, line):
        stackless.tasklet(self.on_message)(line)
        reactor.callLater(0, stackless.schedule)

    def on_message(self, line):
        self.sendLine('Echo:' + line + '\n')
        self.transport.write('>>> ')


stdio.StandardIO(CommandProtocol())
stackless.tasklet(reactor.run)()
reactor.callLater(0, stackless.schedule)
stackless.run()
