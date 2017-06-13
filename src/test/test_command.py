# -*- coding:utf-8 -*-
'''
Created on 13/06/2017

@author: zhaojm
'''

import stackless
from twisted.internet import stdio, reactor
from twisted.protocols import basic


class CommandProtocol(basic.LineReceiver):
    # from os import linesep as delimiter   这一句不能丢
    from os import linesep as delimiter
    def connectionMade(self):
        self.transport.write('>>> ')

    def lineReceived(self, line):
        self.sendLine(line)
        self.transport.write('>>> ')

        # def on_message(self, line):
        #     self.sendLine(line)


stdio.StandardIO(CommandProtocol())
reactor.run()
# stackless.tasklet(reactor.run)()
# reactor.callLater(0, stackless.schedule)
# stackless.run()
