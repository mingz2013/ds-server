# -*- coding:utf-8 -*-
"""

rpc_server,负责对外提供rpc接口

"""
__date__ = "30/07/2017"
__author__ = "zhaojm"

from frame.entity.base_server import BaseServer


from frame.rpc.msg import Msg
from frame.rpc.rpc_mark import RpcMark


class RpcServer(BaseServer):
    def __init__(self):
        BaseServer.__init__(self)
        self.__rpc_mark = RpcMark()
        self.register_rpc()
        pass

    def on_conn_made(self, conn):
        pass

    def on_conn_lost(self, conn, reason):
        pass

    def on_msg(self, conn, msg):
        # 解析rpc协议, 调用不同的rpc接口

        msg = Msg.from_msg(msg)
        self.__rpc_mark.handle_rpc(conn, msg.cmd, msg)

        pass

    def rpc_mark(self):
        return self.__rpc_mark

    def register_rpc(self):
        from frame.rpc.rpc_export import *
