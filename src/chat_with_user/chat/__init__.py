# -*- coding:utf-8 -*-
'''
Created on 15/06/2017

@author: zhaojm
'''
import account


class Chat(object):
    def __init__(self):
        self.__login_map = {}
        self.__account_mgr = account
        pass

    def handle_msg(self, msg):
        pass
