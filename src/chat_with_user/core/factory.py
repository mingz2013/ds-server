# -*- coding:utf-8 -*-
'''
Created on 15/06/2017

@author: zhaojm
'''
from twisted.internet.protocol import Factory

from chat_server import ChatServer


class ChatServerFactory(Factory):
    def __init__(self, chat):
        self.chat = chat

    def buildProtocol(self, addr):
        return ChatServer(self.chat)
