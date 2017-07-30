# -*- coding:utf-8 -*-
"""
Created on 13/06/2017

@author: zhaojm
"""

import stackless
from twisted.internet import reactor


class Channel(object):
    def __init__(self, entity1, entity2):
        self.first_chan = stackless.channel()
        self.second_chan = stackless.channel()
        self.start_first_chan()
        self.start_sencond_chan()
        pass

    def start_first_chan(self):
        stackless.tasklet(self.on_first_chan)()
        reactor.callLater(0, stackless.schedule)

    def start_sencond_chan(self):
        stackless.tasklet(self.on_sencond_chan)()
        reactor.callLater(0, stackless.schedule)

    def on_first_chan(self):
        line = self.first_chan.receive()
        self.start_first_chan()
        pass

    def on_sencond_chan(self):
        line = self.second_chan.receive()
        self.start_sencond_chan()
