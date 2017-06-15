# -*- coding:utf-8 -*-
'''
Created on 15/06/2017

@author: zhaojm
'''

import db


class Account(object):
    def __init__(self):
        pass

    def account_create(self, name, password):
        user_id = db.get_one_user_id()
        user_info = {
            "name": name,
            "password": password,
            "user_id": user_id
        }
        db.insert_user_info(user_id, user_info)
        return user_id

    def account_login(self, user_id, password):
        user_info = db.get_user_info(user_id)
        if user_info:
            if user_info['password'] == password:
                return user_info
        return None
