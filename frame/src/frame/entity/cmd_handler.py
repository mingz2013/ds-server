# -*- coding:utf-8 -*-
"""
Created on 20/06/2017

@author: zhaojm
"""
from frame.core.entity import Entity


class CmdHandler(Entity):


    def on_conn_made(self, conn):
        pass

    def on_conn_lost(self, conn, reason):
        pass

    def on_msg(self, conn, msg):
        pass


if __name__ == '__main__':
    from frame.core import reactor

    c = CmdHandler()
    reactor.init_stdio(c)
    reactor.start_reactor()
