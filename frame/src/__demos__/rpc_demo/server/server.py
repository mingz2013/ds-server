# -*- coding:utf-8 -*-
"""
"""
__date__ = "30/07/2017"
__author__ = "zhaojm"

from frame.servers.rpc.rpc_server import RpcServer


class Server(RpcServer):
    pass


if __name__ == '__main__':
    from frame.core import reactor
    from frame.servers.rpc.rpc import *

    s = Server()
    reactor.init_server(s, '0.0.0.0', 8888)
    reactor.start_reactor()
    pass
