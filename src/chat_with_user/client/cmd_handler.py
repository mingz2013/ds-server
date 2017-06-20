# -*- coding:utf-8 -*-
'''
Created on 19/06/2017

@author: zhaojm
'''

from core.entity import Entity
from entity.client.chat_client import ChatClient


class CmdHandler(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.client = ChatClient(self)
        self.conn = None
        pass

    def __conn_to_server(self, ip, port):
        self.client.conn_to_server(ip, port)
        pass

    def on_conn_made(self, conn):
        self.conn = conn
        self.__conn_to_server('localhost', 8888)
        pass

    def on_conn_lost(self, conn, reason):
        self.conn = None

    def on_msg(self, conn, msg):
        self.client.sendLine(self, msg)

    def on_client_msg(self, client, msg):
        self.conn.sendLine(msg)
        pass
