# -*- coding:utf-8 -*-
"""
rpc_server,负责对外提供rpc接口
"""
__date__ = "30/07/2017"
__author__ = "zhaojm"

from frame.entity.base_server import BaseServer


from frame.servers.rpc.msg import Msg
from frame.core import reactor


class TcpAcceptor(BaseServer):
    def __init__(self, entity):
        self._entity = entity

    def on_conn_made(self, conn):
        pass

    def on_conn_lost(self, conn, reason):
        pass

    def on_msg(self, conn, msg):
        # 解析rpc协议, 调用不同的rpc接口
        m = Msg.from_msg(msg)
        self._entity.rpc_handle(conn, msg.cmd, m)

    def init_acceptor(self, ip, port):
        reactor.init_tcp_server(self, ip, port)
