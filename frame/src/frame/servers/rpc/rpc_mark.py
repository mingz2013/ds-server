# -*- coding:utf-8 -*-
"""

装饰器, 用于标注rpc接口

"""
__date__ = "30/07/2017"
__author__ = "zhaojm"


class RpcMark(object):
    def __init__(self):
        self.__rpc_export = {}
        # TODO 注册接口

    def rpc_mark(self, event, handler=None):

        def decorator(handle):
            if event not in self.__rpc_export:
                self.__rpc_export[event] = handle

        if handler is None:
            return decorator
        decorator(handler)

    def rpc_handle(self, conn, event, args):
        if event in self.__rpc_export:
            return self.__rpc_export[event](conn, args)
        else:
            print "event error", event