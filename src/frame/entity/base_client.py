# -*- coding:utf-8 -*-
'''
Created on 20/06/2017

@author: zhaojm
'''

from core.entity import Entity
from core.factory import conn_to_server


class BaseClient(Entity):
    def __init__(self, server):
        self.server = server
        self.conn = None
        pass

    def conn_to_server(self, ip, port):
        conn_to_server(self, ip, port)

    def on_conn_made(self, conn):
        self.conn = conn
        pass

    def on_conn_lost(self, conn, reason):
        self.conn = None

    def on_msg(self, conn, msg):
        self.server.on_client_msg(self, msg)
        pass

    def sendLine(self, server, msg):
        self.conn.sendLine(msg)
