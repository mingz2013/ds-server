# -*- coding:utf-8 -*-
"""
"""
__date__ = "05/08/2017"
__author__ = "zhaojm"

from frame.servers.rpc.rpc_entity import RpcEntity


class Entity(RpcEntity):
    def __init__(self):
        super(Entity, self).__init__()


if __name__ == '__main__':
    e = Entity()
    e.init_rpc()
    e.start_server("127.0.0.1", 8000)
