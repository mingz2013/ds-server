# -*- coding:utf-8 -*-
'''
Created on 10/06/2017

@author: zhaojm
'''

from twisted.internet.protocol import Protocol


class BaseProtocol(Protocol):
    def dataReceived(self, data):
        self.transport.write(data)
