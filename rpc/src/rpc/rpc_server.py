# -*- coding:utf-8 -*-
"""

rpc_server,负责对外提供rpc接口

"""
__date__ = "30/07/2017"
__author__ = "zhaojm"

from frame.entity.base_server import BaseServer

from rpc.rpc_mark import mark_rpc
from rpc.msg import Msg


class RpcServer(BaseServer):
    def __init__(self):
        BaseServer.__init__(self)
        pass

    def on_conn_made(self, conn):
        pass

    def on_conn_lost(self, conn, reason):
        pass

    def on_msg(self, conn, msg):
        # 解析rpc协议, 调用不同的rpc接口

        msg = Msg.from_msg(msg)
        mark_rpc.handle_rpc(conn, msg.cmd, msg)

        pass
