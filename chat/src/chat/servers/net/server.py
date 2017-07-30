# -*- coding:utf-8 -*-
'''
Created on 26/06/2017

网关服务器, 用于接收客户端连接

客户端从 login_server 拿到session和地址, 连接过来

从db_server验证session, 验证成功则登陆成功

@author: zhaojm
'''
from frame.rpc.rpc_server import RpcServer


class NetServer(RpcServer):
    def __init__(self):
        RpcServer.__init__(self)

    def on_conn_lost(self, conn, reason):
        pass

    def on_conn_made(self, conn):
        pass

    def on_msg(self, conn, msg):
        conn.sendLine(msg)
        pass
