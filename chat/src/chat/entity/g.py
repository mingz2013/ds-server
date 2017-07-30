# -*- coding:utf-8 -*-
'''
Created on 21/06/2017

本模块存储全局的一些数据, 方便随时随地引用

@author: zhaojm
'''

s = {}


def register_server(s_str):
    exec_str = "from chat.servers.%s.server import Server; s['%s'] = Server()" % s_str
    exec exec_str


def main():
    s_list_str = ["db", "gate", "http", "master", "net", "room", "sdk", "sio", "ws"]
    for s_str in s_list_str: register_server(s_str)
