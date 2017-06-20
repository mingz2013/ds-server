# -*- coding:utf-8 -*-
'''
Created on 20/06/2017

@author: zhaojm
'''

from frame.core.entity import Entity


class BaseServer(Entity):
    def __init__(self):
        pass

    def on_conn_made(self, conn):
        pass

    def on_conn_lost(self, conn, reason):
        pass

    def on_msg(self, conn, msg):
        pass
