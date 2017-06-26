# -*- coding:utf-8 -*-
'''
Created on 26/06/2017

用于接收ws连接, 并转换到其他服务器

@author: zhaojm
'''
from frame.entity.base_server import BaseServer
import g


class WSServer(BaseServer):
    def __init__(self):
        BaseServer.__init__(self)

    def on_conn_lost(self, conn, reason):
        pass

    def on_conn_made(self, conn):
        pass

    def on_msg(self, conn, msg):
        conn.sendLine(msg)
        pass
