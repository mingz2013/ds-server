# -*- coding:utf-8 -*-
"""
"""
__date__ = "30/07/2017"
__author__ = "zhaojm"

from rpc.rpc_mark import mark_rpc
from entity import entity


@mark_rpc.mark_rpc("get_info")
def on_get_info(conn, args):
    entity.do_some_thing()
    pass


@mark_rpc.mark_rpc("register")
def on_register(conn, args):
    pass
