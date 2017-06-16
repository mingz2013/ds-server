# -*- coding:utf-8 -*-
'''
Created on 13/06/2017

@author: zhaojm
'''

from os import linesep

import stackless
from twisted.internet import reactor
from twisted.protocols.basic import LineReceiver
from twisted.internet.protocol import ClientFactory
from channel import chan_client_to_command, chan_command_to_client
from chat_client import ChatClient


class CmdHandler(LineReceiver):
    delimiter = linesep

    def __init__(self):
        self.cmd_executer = {
            "connect": self._connect_to_server
        }

    def _connect_to_server(self):
        stackless.tasklet(self.on_message_from_client)()
        reactor.callLater(0, stackless.schedule)
        f = ClientFactory()
        f.protocol = ChatClient
        reactor.connectTCP('localhost', 8888, f)

    def _send_to_client(self, cmd, *argl, **argd):
        msg = {}
        chan_command_to_client.send(msg)
        pass

    def connectionMade(self):
        self._connect_to_server()
        self.transport.write('>>> ')

    def lineReceived(self, line):
        # print "command line received"
        stackless.tasklet(self.parse_cmd)(line)
        reactor.callLater(0, stackless.schedule)

    def parse_cmd(self, line):
        # 这里去解析命令, 然后将命令解析成命令加参数的某种格式, 给客户端执行
        # 这里需要某个解析
        msg = {
            "cmd": line
        }

        self.cmd_execute(msg['cmd'], msg)

        self.transport.write('>>> ')
        pass

    def cmd_execute(self, cmd, *argl, **argd):
        if cmd in self.cmd_executer:
            self.cmd_executer['cmd'](*argl, **argd)
        else:
            self._send_to_client(cmd, *argl, **argd)

    def on_message_from_client(self):
        msg = chan_client_to_command.receive()
        # 这里控制怎么显示,显示样式
        self.sendLine(msg)
        self.transport.write('>>> ')
        stackless.tasklet(self.on_message_from_client)()
        reactor.callLater(0, stackless.schedule)

