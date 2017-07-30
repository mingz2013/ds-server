# -*- coding:utf-8 -*-
"""
"""
__date__ = "30/07/2017"
__author__ = "zhaojm"

from frame.servers.rpc import g


@g.s.rpc_mark.mark_rpc("get_info")
def on_get_info(conn, args):
    pass


@g.s.rpc_mark.mark_rpc("register")
def on_register(conn, args):
    pass
