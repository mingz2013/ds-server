# -*- coding:utf-8 -*-
"""
Created on 21/06/2017

本模块存储全局的一些数据, 方便随时随地引用

@author: zhaojm
"""

s = {}  # 存储server对象列表, 这里限制了每个进程最多一个相同的server对象, 否则会有key冲突


def init_servers():
    s_list_str = ["db", "gate", "manager", "robot", "proxy", "sio", "ws"]
    for s_str in s_list_str:
        # register server
        exec "from chat.servers.%s.server import Server; s['%s'] = Server()" % s_str

    s_list_str = ['http', 'sdk']
    for s_str in s_list_str:
        # register web app
        exec "from chat.servers.%s.server import app; s['%s'] = app" % s_str

    s_list_str = ["db", "gate", "manager", "proxy"]
    for s_str in s_list_str:
        # register rpc
        exec "from chat.servers.%s.rpc import *" % s_str


def start_servers():
    from frame.core import reactor
    index = 0
    for (k, v) in s.items():

        port = 8000 + index
        ip = "127.0.0.1"

        if k in ["db", "gate", "manager", "robot", "proxy"]:
            reactor.init_server(v, ip, port)
        elif k in ["http", "sdk"]:
            reactor.init_http_server(v, ip, port)
        elif k in ["sio"]:
            reactor.init_sio_server(v, ip, port, u"ws://%s:%s" % (ip, port))
        elif k in ["ws"]:
            reactor.init_ws_server(v, ip, port, u"ws://%s:%s" % (ip, port))
        else:
            print "unknown k", k
