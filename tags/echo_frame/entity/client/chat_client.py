# -*- coding:utf-8 -*-
'''
Created on 19/06/2017

@author: zhaojm
'''

from core.entity import Entity
from core.factory import conn_to_server


class ChatClient(Entity):
    def __init__(self):
        self.conn = None
        pass

    def conn_to_server(self, ip, port):
        conn_to_server(ip, port, self)

    def on_conn_made(self, conn):
        self.conn = conn
        pass

    def on_conn_lost(self, conn):
        self.conn = None

    def on_msg(self, conn, msg):
        conn.send_to_chan(msg)
        pass

    def on_chan(self, conn, msg):
        # print msg
        conn.sendLine(msg)
