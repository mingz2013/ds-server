# -*- coding:utf-8 -*-
'''
Created on 19/06/2017

@author: zhaojm
'''

from chat_server import ChatServer
from core.reactor import start_reactor
from core.factory import init_server

s = ChatServer()

init_server(s)
start_reactor()
