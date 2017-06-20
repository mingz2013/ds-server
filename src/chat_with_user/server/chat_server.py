# -*- coding:utf-8 -*-
'''
Created on 19/06/2017

@author: zhaojm
'''

from frame.entity.base_server import BaseServer


class ChatServer(BaseServer):
    def __init__(self):
        BaseServer.__init__(self)
        pass

    def on_msg(self, conn, msg):
        conn.sendLine(msg)


if __name__ == '__main__':
    from frame.core.reactor import start_reactor, init_server

    c = ChatServer()
    init_server(c, '0.0.0.0', 8888)
    start_reactor()
