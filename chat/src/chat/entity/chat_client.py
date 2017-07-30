# -*- coding:utf-8 -*-
'''
Created on 19/06/2017

@author: zhaojm
'''

from frame.entity.base_client import BaseClient


class ChatClient(BaseClient):
    def __init__(self, cmd_handler):
        BaseClient.__init__(self)
        self.cmd_handler = cmd_handler
        self.conn = None
        pass

    def on_conn_made(self, conn):
        self.conn = conn
        pass

    def on_conn_lost(self, conn, reason):
        self.conn = None

    def on_msg(self, conn, msg):
        self.cmd_handler.on_client_msg(self, msg)
        pass

    def on_cmd(self, msg):
        # 从cmd handler传过来的数据
        self.conn.sendLine(msg)
        pass
