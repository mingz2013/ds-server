# -*- coding:utf-8 -*-
'''
Created on 19/06/2017

@author: zhaojm
'''

import account
from core.entity import Entity


class ChatServer(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.__login_map = {}
        self.__room_map = {}
        self.__account_mgr = account
        pass

    @property
    def account_mgr(self):
        return self.__account_mgr

    def get_user(self, user_id):
        return self.__login_map.get(user_id)

    def get_room(self, room_id):
        return self.__room_map.get(room_id)

    def on_conn_lost(self, conn):
        if conn.user_id and conn.user_id in self.__login_map:
            del self.__login_map[conn.user_id]

    def on_msg(self, conn, msg):
        print msg
        conn.sendLine(msg)
