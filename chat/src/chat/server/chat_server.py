# -*- coding:utf-8 -*-
'''
Created on 19/06/2017

本模块用于接收用户连接, 和用户直接通信, 连接管理

@author: zhaojm
'''

from frame.entity.base_server import BaseServer
import g


class ChatServer(BaseServer):
    def __init__(self):
        BaseServer.__init__(self)

    def on_conn_lost(self, conn, reason):
        pass

    def on_conn_made(self, conn):
        pass

    def on_msg(self, conn, msg):
        conn.sendLine(msg)
        pass

