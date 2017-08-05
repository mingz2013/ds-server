# -*- coding:utf-8 -*-
"""
"""
__date__ = "30/07/2017"
__author__ = "zhaojm"

from frame.servers.tcp import e


@e.rpc_mark("get_info")
def on_get_info(conn, msg):
    pass


@e.rpc_mark("register")
def on_register(conn, msg):
    pass
