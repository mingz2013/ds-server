# -*- coding:utf-8 -*-
"""
Created on 19/06/2017

@author: zhaojm
"""

from core.entity import Entity


class CmdHandler(Entity):
    def __init__(self, client):
        self.client = client
        self.conn = None
        pass

    def __conn_to_server(self, ip, port):
        self.client.conn_to_server(ip, port)
        pass

    def on_conn_made(self, conn):
        self.conn = conn
        self.__conn_to_server('localhost', 8888)
        pass

    def on_conn_lost(self, conn):
        self.conn = None

    def on_chan(self, conn, msg):
        conn.sendLine(msg)

    def on_msg(self, conn, msg):
        # print msg
        conn.send_to_chan(msg)
