# -*- coding:utf-8 -*-
'''
Created on 13/06/2017

@author: zhaojm
'''

import stackless
from twisted.internet import reactor


class Channel(object):
    def __init__(self, entity1, entity2):
        self.first_chan = stackless.channel()
        self.second_chan = stackless.channel()
        pass

    def start(self):
        stackless.tasklet(self.on_first_chan)()
        reactor.callLater(0, stackless.schedule)

    def on_first_chan(self):
        line = self.first_chan.receive()
        pass

    def on_sencond_chan(self):
        line = self.second_chan.receive()
