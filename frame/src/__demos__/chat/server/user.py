# -*- coding:utf-8 -*-
"""
Created on 15/06/2017

@author: zhaojm
"""


class User(object):
    def __init__(self, user_id):
        self.user_id = user_id
        self.name = str(user_id)
        self.__protocol = None
        pass

    @property
    def protocol(self):
        return self.__protocol

    def set_name(self, name):
        self.name = name
