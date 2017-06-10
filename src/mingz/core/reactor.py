# -*- coding:utf-8 -*-
'''
Created on 10/06/2017

@author: zhaojm
'''

import stackless

from twisted.internet import reactor


def mainloop():
    stackless.tasklet(reactor.run)()
    reactor.callLater(0, stackless.schedule)
    stackless.run()
