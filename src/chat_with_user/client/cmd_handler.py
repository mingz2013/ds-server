# -*- coding:utf-8 -*-
'''
Created on 19/06/2017

@author: zhaojm
'''

from frame.entity.cmd_handler import CmdHandler
from chat_client import ChatClient
from frame.core.reactor import init_client


class ChatCmdHandler(CmdHandler):
    def __init__(self):
        CmdHandler.__init__(self)
        self.chat_client = ChatClient(self)
        self.conn = None
        pass

    def __conn_to_server(self, ip, port):
        init_client(self.chat_client, ip, port)

    def on_conn_made(self, conn):
        self.conn = conn
        self.__conn_to_server('localhost', 8888)
        pass

    def on_conn_lost(self, conn, reason):
        self.conn = None

    def on_msg(self, conn, msg):
        pass

    def on_client_msg(self, client, msg):
        self.conn.sendLine(msg)
        pass
