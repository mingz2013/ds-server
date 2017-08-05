# -*- coding:utf-8 -*-
"""
"""
__date__ = "30/07/2017"
__author__ = "zhaojm"

from frame.entity.base_client import BaseClient
from frame.core import reactor


class TcpConnector(BaseClient):
    def __init__(self, entity):
        self._entity = entity
        self.conn = None
        pass

    def on_conn_made(self, conn):
        self.conn = conn
        pass

    def on_conn_lost(self, conn, reason):
        self.conn = None

    def on_msg(self, conn, msg):
        pass

    # def on_cmd(self, msg):
    #     # 从cmd handler传过来的数据
    #     self.conn.sendLine(msg)
    #     pass

    def init_connector(self, ip, port):
        reactor.init_tcp_client(self, ip, port)
        pass
