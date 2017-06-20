# -*- coding:utf-8 -*-
'''
Created on 19/06/2017

@author: zhaojm
'''

from frame.entity.base_server import BaseServer


class ChatRoomServer(BaseServer):
    def __init__(self):
        BaseServer.__init__(self)
        self.__conn_list = []
        pass

    def on_conn_lost(self, conn, reason):
        if conn in self.__conn_list:
            self.__conn_list.remove(conn)

    def on_conn_made(self, conn):
        self.__conn_list.append(conn)

    def on_msg(self, conn, msg):
        print 'on msg', msg
        for m in self.__conn_list:
            if m != conn:
                m.sendLine(msg)


if __name__ == '__main__':
    from frame.core.reactor import start_reactor, init_server

    c = ChatRoomServer()
    init_server(c, '0.0.0.0', 8888)
    start_reactor()
