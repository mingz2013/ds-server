# -*- coding:utf-8 -*-
"""
Created on 15/06/2017
数据库 dao
@author: zhaojm
"""

__db = {
    "user_list_map": {
        "1000": {
            "user_id": 1000,
            "name": "",
            "password": "123"
        }
    },

    "cur_user_id": 1001

}


def get_user_info(user_id):
    return __db["user_list_map"].get(user_id, None)


def insert_user_info(user_id, user_info):
    __db["user_list_map"].update({
        user_id: user_info
    })


def user_count():
    return len(__db["cur_user_id"])


def get_one_user_id():
    __db["cur_user_id"] += __db["cur_user_id"]
    return __db["cur_user_id"]
