# -*- coding:utf-8 -*-
'''
Created on 15/06/2017

@author: zhaojm
'''


class User(object):
    def __init__(self, userId):
        self.userId = userId
        self.name = str(userId)
        self.__protocol = None
        pass

    @property
    def protocol(self):
        return self.__protocol

    def set_protocol(self, protocol):
        self.__protocol = protocol

    def set_name(self, name):
        self.name = name

    def send_to_client(self, msg):
        self.__protocol.send_to_client(msg)
        pass
