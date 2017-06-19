# -*- coding:utf-8 -*-
'''
Created on 19/06/2017

@author: zhaojm
'''


class Entity(object):
    def __init__(self):
        pass

    def on_conn_made(self, conn):
        return NotImplementedError()

    def on_conn_lost(self, conn):
        return NotImplementedError()

    def on_msg(self, msg):
        return NotImplementedError()
