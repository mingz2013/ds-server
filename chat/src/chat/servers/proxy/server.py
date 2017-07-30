# -*- coding:utf-8 -*-
"""
Created on 26/06/2017

代理server, 用于转发ws, sio, http协议到系统内部

@author: zhaojm
"""

from frame.servers.rpc.rpc_server import RpcServer


class Server(RpcServer):
    def __init__(self):
        RpcServer.__init__(self)

    def on_conn_lost(self, conn, reason):
        pass

    def on_conn_made(self, conn):
        pass

    def on_msg(self, conn, msg):
        conn.sendLine(msg)
        pass
