# -*- coding:utf-8 -*-
"""

装饰器, 用于标注rpc接口

"""
__date__ = "30/07/2017"
__author__ = "zhaojm"


class MarkRpc(object):
    def __init__(self):
        self.__rpc_export = {}

    def mark_rpc(self, event, handler=None):

        def decorator(handler):
            if event not in self.__rpc_export:
                self.__rpc_export[event] = handler

        if handler is None:
            return decorator
        decorator(handler)

    def handle_rpc(self, conn, event, args):
        if event in self.__rpc_export:
            return self.__rpc_export[event](conn, args)
        else:
            print "event error", event


mark_rpc = MarkRpc()

__all__ = [mark_rpc]
