# -*- coding:utf-8 -*-
"""
"""
__date__ = "30/07/2017"
__author__ = "zhaojm"

from frame.servers.rpc.g import s
from entity import entity


@s.rpc_mark("get_info")
def on_get_info(conn, args):
    entity.do_some_thing()
    pass


@s.rpc_mark("register")
def on_register(conn, args):
    pass
