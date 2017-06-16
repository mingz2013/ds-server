# -*- coding:utf-8 -*-
'''
Created on 14/06/2017

@author: zhaojm
'''

from twisted.internet import reactor
from ..chat import Chat

def init_server():
    from factory import ChatServerFactory
    c = Chat()
    reactor.listenTCP(8888, ChatServerFactory(c))


if __name__ == '__main__':
    init_server()
    from run import start_reactor

    start_reactor()
