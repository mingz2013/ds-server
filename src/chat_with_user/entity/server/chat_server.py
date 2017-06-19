# -*- coding:utf-8 -*-
'''
Created on 19/06/2017

@author: zhaojm
'''

import account


class ChatServer(object):
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

    def on_lost(self, conn):
        del self.__login_map[conn.user_id]
        pass

    def on_msg(self, conn, msg):

        if "create_user" in msg:
            # 创建用户, 注册用户, 作用, 数据库里有你的信息,可用于登陆
            name = msg['name']
            password = msg['password']
            user_id = self.account_mgr.account_create(name, password)
            if user_id:
                self.__login_map.update({
                    user_id: conn
                })
                conn.sendLine({"user_id": user_id, "result": "success"})
        elif "login" in msg:
            # 登陆, 检查登陆信息, 将conn和用户保存起来, 返回登陆成功与否的信息
            user_id = msg['user_id']
            password = msg['password']
            is_login = self.account_mgr.account_login(user_id, password)
            if is_login:
                self.__login_map.update({
                    user_id: conn
                })
                conn.sendLine({"user_id": user_id, "result": "success"})
            else:
                pass

        elif "create_room" in msg:
            pass
        elif "join_room" in msg:
            pass
        elif "room" in msg:
            self.on_room_msg(conn, msg)
        else:
            pass

    def on_room_msg(self, conn, msg):
        self.get_room(msg['room_id']).on_msg(conn, msg)
        pass
