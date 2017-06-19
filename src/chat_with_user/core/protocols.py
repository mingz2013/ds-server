# -*- coding:utf-8 -*-
'''
Created on 17/06/2017

@author: zhaojm
'''

import stackless
from twisted.internet import reactor
from twisted.internet.protocol import connectionDone
from twisted.protocols.basic import LineReceiver
import stackless
from twisted.internet import reactor

from twisted.protocols.basic import LineReceiver

from channel import chan_client_to_command, chan_command_to_client


class TcpServerProtocol(LineReceiver):
    def __init__(self, entity):
        self.entity = entity
        self.__user_id = -1

    def set_user_id(self, user_id):
        self.__user_id = user_id

    @property
    def user_id(self):
        return self.__user_id

    def connectionMade(self):
        pass

    def connectionLost(self, reason=connectionDone):
        self.entity.on_lost(self)
        pass

    def lineReceived(self, line):
        stackless.tasklet(self.on_msg)(line)
        reactor.callLater(0, stackless.schedule)

    def on_msg(self, msg):
        self.entity.on_msg(self, msg)

        # def send_to_client(self, msg):
        #     self.sendLine(msg)


class TcpClientProtocol(LineReceiver):
    def connectionMade(self):
        stackless.tasklet(self.on_message_from_command)()
        reactor.callLater(0, stackless.schedule)

    def lineReceived(self, line):
        stackless.tasklet(self.parse_msg)(line)
        reactor.callLater(0, stackless.schedule)

    def parse_msg(self, msg):
        # 这里解析服务器传来的消息, 并封装用户显示数据给cmd

        self.send_to_cmd(msg)
        pass

    def send_to_cmd(self, message):
        chan_client_to_command.send(message)

    def on_message_from_command(self):
        msg = chan_command_to_client.receive()
        self.cmd_execute(msg['cmd'], msg)
        stackless.tasklet(self.on_message_from_command)()
        reactor.callLater(0, stackless.schedule)

    def cmd_execute(self, cmd, *argl, **argd):
        # 执行cmd发过来的命令

        pass
