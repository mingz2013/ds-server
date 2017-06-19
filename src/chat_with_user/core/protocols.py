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

chan_command_to_client = stackless.channel()
chan_client_to_command = stackless.channel()


class BaseProtocol(LineReceiver):
    def __init__(self, entity):
        self.__entity = entity
        pass

    def connectionMade(self):
        self.__entity.on_conn_made(self)

    def connectionLost(self, reason=connectionDone):
        self.__entity.on_conn_lost(self)

    def lineReceived(self, line):
        stackless.tasklet(self.on_msg)(line)
        reactor.callLater(0, stackless.schedule)

    def on_msg(self, msg):
        self.__entity.on_msg(self, msg)

    def on_chan(self):
        pass

    def send_to_chan(self, msg):
        pass


class TcpServerProtocol(BaseProtocol):
    def __init__(self, entity):
        BaseProtocol.__init__(self, entity)
        self.__user_id = -1  # 定义一个user_id变量, 能够通过user_id索引protocol, 效率高一些

    def set_user_id(self, user_id):
        self.__user_id = user_id

    @property
    def user_id(self):
        return self.__user_id


class TcpClientProtocol(BaseProtocol):
    def __init__(self, entity):
        BaseProtocol.__init__(self, entity)

    def send_to_chan(self, msg):
        chan_command_to_client.send(msg)

    def on_chan(self):
        msg = chan_command_to_client.receive()
        self.on_msg_from_chan(msg)
        stackless.tasklet(self.on_chan)()
        reactor.callLater(0, stackless.schedule)

    def on_msg_from_chan(self, msg):
        pass


class CmdHandlerProtocol(BaseProtocol):
    delimiter = linesep

    def __init__(self, entity):
        BaseProtocol.__init__(self, entity)

    def send_to_chan(self, msg):
        chan_command_to_client.send(msg)

    def on_chan(self):
        msg = chan_client_to_command.receive()
        self.on_msg_from_chan(msg)
        stackless.tasklet(self.on_chan)()
        reactor.callLater(0, stackless.schedule)

    def on_msg_from_chan(self, msg):
        pass
