# -*- coding:utf-8 -*-
"""
"""
__date__ = "30/07/2017"
__author__ = "zhaojm"

from frame.entity.base_client import BaseClient


class RpcConnector(BaseClient):
    def __init__(self):
        BaseClient.__init__(self)
        self.conn = None
        pass

    def on_conn_made(self, conn):
        self.conn = conn
        pass

    def on_conn_lost(self, conn, reason):
        self.conn = None

    def on_msg(self, conn, msg):
        pass

    def on_cmd(self, msg):
        # 从cmd handler传过来的数据
        self.conn.sendLine(msg)
        pass
