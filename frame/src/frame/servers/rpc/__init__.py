# -*- coding:utf-8 -*-
"""
"""
__date__ = "30/07/2017"
__author__ = "zhaojm"


def init():
    from frame.entity import log
    log.init_logging()


from frame.servers.rpc.rpc_entity import RpcEntity

s = RpcEntity()
s.init_rpc()
s.init_server("127.0.0.1", 8000)
