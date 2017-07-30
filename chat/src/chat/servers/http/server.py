# -*- coding:utf-8 -*-
"""
Created on 26/06/2017

用于提供http服务,

静态页面服务

静态文件服务, 图片, 压缩包等

后台管理功能

@author: zhaojm
"""
from frame.servers.rpc.rpc_server import RpcServer


class Server(RpcServer):
    def on_conn_lost(self, conn, reason):
        pass

    def on_conn_made(self, conn):
        pass

    def on_msg(self, conn, msg):
        conn.sendLine(msg)
        pass
