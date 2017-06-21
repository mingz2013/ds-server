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

    def set_name(self, name):
        self.name = name

