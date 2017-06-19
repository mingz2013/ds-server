# -*- coding:utf-8 -*-
'''
Created on 19/06/2017

@author: zhaojm
'''


class ChatClient(object):
    def __init__(self):
        self.conn = None
        pass

    def on_made(self, conn):
        self.conn = conn
        pass

    def on_msg(self, conn, msg):
        pass

    def on_chan(self, chan, msg):
        pass
