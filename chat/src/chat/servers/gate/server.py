# -*- coding:utf-8 -*-
'''
Created on 26/06/2017

http服务, 客户端首先登陆这个地址, 简单验证client_id, 然后连接数据库, 选择一个login server发送给客户端


@author: zhaojm
'''

from frame.rpc.rpc_server import RpcServer


class GateServer(RpcServer):
    def __init__(self):
        RpcServer.__init__(self)

    def on_conn_lost(self, conn, reason):
        pass

    def on_conn_made(self, conn):
        pass

    def on_msg(self, conn, msg):
        conn.sendLine(msg)
        pass
