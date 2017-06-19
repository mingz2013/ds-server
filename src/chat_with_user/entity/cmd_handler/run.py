# -*- coding:utf-8 -*-
'''
Created on 19/06/2017

@author: zhaojm
'''

from .cmd_handler import CmdHandler
from core.factory import init_cmd_handler
from core.reactor import start_reactor

c = CmdHandler()
init_cmd_handler(c)
start_reactor()
