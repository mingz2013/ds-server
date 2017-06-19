# -*- coding:utf-8 -*-
'''
Created on 15/06/2017

@author: zhaojm
'''
import account


class Chat(object):
    def __init__(self):
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

    def create_user(self, name, password):
        pass

    def login(self, user_id, password):
        pass

    def on_lost(self, protocol):
        pass

    def on_msg(self, protocol, msg):

        if "create_user" in msg:
            name = msg['name']
            password = msg['password']
            user_id = self.account_mgr.account_create(name, password)
            if user_id:
                self.__login_map.update({
                    user_id: protocol
                })
                pass
        elif "login" in msg:
            pass
        elif "create_room" in msg:
            pass
        elif "join_room" in msg:
            pass
        elif "room_id" in msg:
            self.get_room(msg['room_id']).on_msg(msg)
        else:
            pass
