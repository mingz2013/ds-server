# -*- coding:utf-8 -*-
'''
Created on 15/06/2017

@author: zhaojm
'''

import stackless
from twisted.internet import reactor
from twisted.internet import stdio

from cmd_handler import CmdHandler
from chat import Chat


def init_client():
    c = Chat()
    stdio.StandardIO(CmdHandler(c))


def start_reactor():
    stackless.tasklet(reactor.run)()
    reactor.callLater(0, stackless.schedule)
    stackless.run()


if __name__ == "__main__":
    init_client()
    start_reactor()
