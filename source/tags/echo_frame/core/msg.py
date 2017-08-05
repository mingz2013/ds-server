# -*- coding:utf-8 -*-
"""
Created on 15/06/2017

@author: zhaojm
"""


class Msg(object):
    def __init__(self, cmd=None):
        self.cmd = cmd
        self.result = {}

    def set_cmd(self, cmd):
        self.cmd = cmd

    def set_result(self, result):
        self.result = result

    def update_result(self, result):
        self.result.update(result)
