# -*- coding:utf-8 -*-
'''
Created on 15/06/2017

@author: zhaojm
'''


class Room(object):
    def __init__(self):
        self.__members = {}
        pass

    def __send_to_all(self, msg):
        for m in self.__members:
            m.send_to_protocol(msg)
            pass

    def on_msg(self, user_id, msg):
        if 'all' in msg:
            self.__send_to_all(msg)
