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

first_chan = stackless.channel()
second_chan = stackless.channel()


class BaseProtocol(LineReceiver):
    def __init__(self, entity):
        self.entity = entity
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
        self.entity.on_conn_lost(self)

    def on_msg(self, msg):
        # print msg
        self.entity.on_msg(self, msg)


class TcpServerProtocol(BaseProtocol):
    def __init__(self, entity):
        BaseProtocol.__init__(self, entity)
        self.__user_id = -1  # 定义一个user_id变量, 能够通过user_id索引protocol, 效率高一些

    def set_user_id(self, user_id):
        self.__user_id = user_id

    @property
    def user_id(self):
        return self.__user_id


class ChannelProtocol(BaseProtocol):
    def __init__(self, entity):
        BaseProtocol.__init__(self, entity)
        self.start_listen_chan()

    def start_listen_chan(self):
        stackless.tasklet(self.on_chan)()
        reactor.callLater(0, stackless.schedule)

    def on_chan(self):
        pass

    def send_to_chan(self, msg):
        pass


class TcpClientProtocol(ChannelProtocol):
    def __init__(self, entity):
        ChannelProtocol.__init__(self, entity)

    def send_to_chan(self, msg):
        first_chan.send(msg)
        pass

    def on_chan(self):
        # print "tcp client on chan"
        msg = second_chan.receive()
        # print "tcp client on chan:", msg
        self.entity.on_chan(self, msg)
        self.start_listen_chan()


class CmdHandlerProtocol(ChannelProtocol):
    delimiter = linesep

    def __init__(self, entity):
        ChannelProtocol.__init__(self, entity)

    def send_to_chan(self, msg):
        second_chan.send(msg)
        pass

    def on_chan(self):
        msg = first_chan.receive()
        self.entity.on_chan(self, msg)
        self.start_listen_chan()
