# -*- coding:utf-8 -*-
'''
Created on 26/06/2017


账号服务器, 用于登陆

客户端连接过来, 通过账号密码登陆或注册

注册登陆成功, 从在线的gate_server中选择一个, 并传给客户端gate_server 地址 和 session

@author: zhaojm
'''
from frame.entity.base_server import BaseServer


class AccountServer(BaseServer):
    def __init__(self):
        BaseServer.__init__(self)

    def on_conn_lost(self, conn, reason):
        pass

    def on_conn_made(self, conn):
        pass

    def on_msg(self, conn, msg):
        conn.sendLine(msg)
        pass
