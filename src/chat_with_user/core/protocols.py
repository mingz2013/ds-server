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


class TcpServerProtocol(LineReceiver):
    def __init__(self, entity):
        self.entity = entity
        self.__user_id = -1  # 定义一个user_id变量, 能够通过user_id索引protocol, 效率高一些

    def set_user_id(self, user_id):
        self.__user_id = user_id

    @property
    def user_id(self):
        return self.__user_id

    def connectionMade(self):
        self.entity.on_made(self)
        pass

    def connectionLost(self, reason=connectionDone):
        self.entity.on_lost(self)
        pass

    def lineReceived(self, line):
        stackless.tasklet(self.on_msg)(line)
        reactor.callLater(0, stackless.schedule)

    def on_msg(self, msg):
        self.entity.on_msg(self, msg)


class TcpClientProtocol(LineReceiver):
    def __init__(self, entity):
        self.entity = entity
        pass

    def connectionMade(self):
        self.entity.on_made(self)
        pass

    def connectionLost(self, reason=connectionDone):
        self.entity.on_lost(self)

    def lineReceived(self, line):
        stackless.tasklet(self.on_msg)(line)
        reactor.callLater(0, stackless.schedule)

    def on_msg(self, msg):
        self.entity.on_msg(self, msg)
        pass

    def on_chan(self):
        msg = chan_command_to_client.receive()
        self.cmd_execute(msg['cmd'], msg)
        stackless.tasklet(self.on_message_from_command)()
        reactor.callLater(0, stackless.schedule)


class CmdHandlerProtocol(LineReceiver):
    delimiter = linesep

    def __init__(self, entity):
        self.entity = entity
        self.cmd_executer = {
            "connect": self._connect_to_server
        }

    def send_to_chan(self, cmd, *argl, **argd):
        msg = {}
        chan_command_to_client.send(msg)
        pass

    def connectionMade(self):
        self.entity.on_made(self)
        pass

    def connectionLost(self, reason=connectionDone):
        self.entity.on_lost(self)

    def lineReceived(self, line):
        stackless.tasklet(self.on_msg)(line)
        reactor.callLater(0, stackless.schedule)

    def on_msg(self, msg):
        self.entity.on_msg(self, msg)

    def on_chan(self):
        msg = chan_client_to_command.receive()
        # 这里控制怎么显示,显示样式
        self.sendLine(msg)
        self.transport.write('>>> ')
        stackless.tasklet(self.on_message_from_client)()
        reactor.callLater(0, stackless.schedule)
