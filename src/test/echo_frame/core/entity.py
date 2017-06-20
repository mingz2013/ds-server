# -*- coding:utf-8 -*-
'''
Created on 19/06/2017

@author: zhaojm
'''


class Entity(object):
    def on_conn_made(self, conn):
        pass

    def on_conn_lost(self, conn):
        pass

    def on_msg(self, conn, msg):
        return NotImplementedError()

    def on_chan(self, conn, msg):
        pass
