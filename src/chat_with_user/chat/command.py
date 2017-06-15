# -*- coding:utf-8 -*-
'''
Created on 15/06/2017

@author: zhaojm
'''

from twisted.protocols.basic import LineReceiver


class Command(LineReceiver):
    def connectionMade(self):
        pass

    def lineReceived(self, line):
        pass
