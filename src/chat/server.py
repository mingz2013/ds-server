# -*- coding:utf-8 -*-
'''
Created on 14/06/2017

@author: zhaojm
'''
import stackless
from twisted.internet import protocol, reactor

from chat_server_protocol import ChatServerFactory

reactor.listenTCP(8888, ChatServerFactory())

stackless.tasklet(reactor.run)()
reactor.callLater(0, stackless.schedule)
stackless.run()
