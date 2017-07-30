# -*- coding:utf-8 -*-
"""
Created on 19/06/2017

业务逻辑 基类

当然, 由于python的鸭子对象类型, 只要有如下三个方法的, 都可以, 无论是对象, 模块, 还是什么的也好

@author: zhaojm
"""


class Entity(object):

    def on_conn_made(self, conn):
        pass

    def on_conn_lost(self, conn, reason):
        pass

    def on_msg(self, conn, msg):
        return NotImplementedError()

