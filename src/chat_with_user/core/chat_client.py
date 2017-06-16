# -*- coding:utf-8 -*-
'''
Created on 10/06/2017

@author: zhaojm
'''

import stackless
from twisted.internet import reactor

from twisted.protocols.basic import LineReceiver

from channel import chan_client_to_command, chan_command_to_client


class ChatClient(LineReceiver):
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
