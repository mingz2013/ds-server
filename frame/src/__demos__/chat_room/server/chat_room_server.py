# -*- coding:utf-8 -*-
"""
Created on 19/06/2017

@author: zhaojm
"""

from frame.entity.base_server import BaseServer


class ChatRoomServer(BaseServer):
    def __init__(self):
        self.__conn_set = set()
        pass

    def on_conn_lost(self, conn, reason):
        if conn in self.__conn_set:
            self.__conn_set.remove(conn)

    def on_conn_made(self, conn):
        self.__conn_set.add(conn)

    def on_msg(self, conn, msg):
        print 'on msg', msg
        for m in self.__conn_set:
            if m != conn:
                m.sendLine(msg)


if __name__ == '__main__':
    from frame.core import reactor

    c = ChatRoomServer()
    reactor.init_server(c, '0.0.0.0', 8888)
    reactor.start_reactor()
