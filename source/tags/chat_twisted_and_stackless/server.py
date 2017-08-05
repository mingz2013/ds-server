# -*- coding:utf-8 -*-
"""
Created on 14/06/2017

@author: zhaojm
"""

from twisted.internet import reactor


def init_server():
    from chat_server_protocol import ChatServerFactory
    reactor.listenTCP(8888, ChatServerFactory())


if __name__ == '__main__':
    init_server()
    from run import start_reactor

    start_reactor()
