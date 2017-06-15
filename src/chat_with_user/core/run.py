# -*- coding:utf-8 -*-
'''
Created on 14/06/2017

@author: zhaojm
'''

import stackless
from twisted.internet import reactor


def start_reactor():
    stackless.tasklet(reactor.run)()
    reactor.callLater(0, stackless.schedule)
    stackless.run()
