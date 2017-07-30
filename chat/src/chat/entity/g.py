# -*- coding:utf-8 -*-
"""
Created on 21/06/2017

本模块存储全局的一些数据, 方便随时随地引用

@author: zhaojm
"""

s = {}  # 存储server对象列表, 限制了每个进程最多一个相同的server对象


def init_servers():
    s_list_str = ["db", "gate", "http", "manager", "proxy", "sdk", "sio", "ws"]
    for s_str in s_list_str:
        # register server
        exec "from chat.servers.%s.server import Server; s['%s'] = Server()" % s_str
        # register rpc
        exec "from chat.servers.%s.rpc import *" % s_str


def start_servers():
    from frame.core import reactor
    for (k, v) in s.items():
        if k in ["db", "gate", "manager", "proxy"]:
            reactor.init_server(v, "127.0.0.1", 8888)
        elif k in ["http", "sdk"]:
            reactor.init_http_server(v, "127.0.0.1", 80)
        elif k in ["sio"]:
            reactor.init_sio_server(v, "127.0.0.1", 8002)
        elif k in ["ws"]:
            reactor.init_ws_server(v, "127.0.0.1", 8003)
        else:
            pass
