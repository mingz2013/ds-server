# -*- coding:utf-8 -*-
"""
Created on 19/06/2017

@author: zhaojm
"""

from chat_room_client import ChatRoomClient
from frame.core.reactor import init_client
from frame.entity.cmd_handler import CmdHandler


class ChatCmdHandler(CmdHandler):
    def __init__(self):
        CmdHandler.__init__(self)
        self.chat_client = ChatRoomClient(self)
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
        self.chat_client.send_line(msg)
        pass

    def on_client_msg(self, client, msg):
        self.conn.sendLine(msg)
        pass
