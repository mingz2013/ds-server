# -*- coding:utf-8 -*-
"""
服务调用之间传输协议结构的描述

"""
__date__ = "30/07/2017"
__author__ = "zhaojm"
import json


class Msg(object):
    def __init__(self):
        self.__msg = {}
        pass

    def set_cmd(self, cmd):
        self.__msg['cmd'] = cmd

    def append_result(self, k, v):
        if "result" not in self.__msg:
            self.__msg['result'] = {}
        self.__msg['result'][k] = v

    def update_result(self, d):
        if "result" not in self.__msg:
            self.__msg['result'] = {}
        self.__msg['result'].update(d)

    def append_params(self, k, v):
        if "params" not in self.__msg:
            self.__msg['params'] = {}
        self.__msg['params'][k] = v

    def update_params(self, d):
        if "params" not in self.__msg:
            self.__msg['params'] = {}
        self.__msg['params'].update(d)

    @property
    def msg(self):
        return self.__msg

    @property
    def json_str(self):
        return json.dumps(self.__msg)

    @classmethod
    def from_msg(cls, msg):
        m = Msg()
        m.__msg = json.loads(msg)
        return m
