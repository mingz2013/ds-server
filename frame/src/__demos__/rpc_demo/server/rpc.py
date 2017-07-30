# -*- coding:utf-8 -*-
"""
"""
__date__ = "30/07/2017"
__author__ = "zhaojm"

import g
from entity import entity


@g.s.rpc_mark("get_info")
def on_get_info(conn, args):
    entity.do_some_thing()
    pass


@g.s.rpc_mark("register")
def on_register(conn, args):
    pass
