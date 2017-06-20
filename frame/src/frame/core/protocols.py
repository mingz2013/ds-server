# -*- coding:utf-8 -*-
'''
Created on 17/06/2017

@author: zhaojm
'''

from os import linesep

import stackless
from twisted.internet import reactor
from twisted.internet.protocol import connectionDone
from twisted.protocols.basic import LineReceiver


class BaseProtocol(LineReceiver):
    def __init__(self, entity):
        self.entity = entity  # 实体业务逻辑
        self.tag = None  # 做个标记
        pass

    def connectionMade(self):
        stackless.tasklet(self.on_conn_made)()
        reactor.callLater(0, stackless.schedule)

    def connectionLost(self, reason=connectionDone):
        stackless.tasklet(self.on_conn_lost)(reason)
        reactor.callLater(0, stackless.schedule)

    def lineReceived(self, line):
        stackless.tasklet(self.on_msg)(line)
        reactor.callLater(0, stackless.schedule)

    def on_conn_made(self):
        self.entity.on_conn_made(self)

    def on_conn_lost(self, reason):
        self.entity.on_conn_lost(self, reason)

    def on_msg(self, msg):
        self.entity.on_msg(self, msg)


class StandardIOProtocol(BaseProtocol):
    delimiter = linesep

    def __init__(self, entity):
        BaseProtocol.__init__(self, entity)
