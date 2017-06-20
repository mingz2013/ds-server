# -*- coding:utf-8 -*-
'''
Created on 19/06/2017

@author: zhaojm
'''

from frame.entity.base_client import BaseClient


class EchoClient(BaseClient):
    def __init__(self, cmd_handler):
        BaseClient.__init__(self)
        self.cmd_handler = cmd_handler
        self.conn = None
        pass

    def on_conn_made(self, conn):
        # print 'conn made in client'
        self.conn = conn
        pass

    def on_conn_lost(self, conn, reason):
        self.conn = None

    def on_msg(self, conn, msg):
        # print 'on msg on client'
        self.cmd_handler.on_client_msg(self, msg)
        pass

    def sendLine(self, msg):
        # print 'send line in client'
        self.conn.sendLine(msg)
