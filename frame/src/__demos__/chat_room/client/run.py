# -*- coding:utf-8 -*-
'''
Created on 19/06/2017

@author: zhaojm
'''

import os
import sys

current_path = os.path.dirname(os.path.abspath(__file__))
source_path = os.path.join(current_path, "../../../")
sys.path.append(source_path)

from cmd_handler import ChatCmdHandler

from frame.core.reactor import init_stdio, start_reactor

if __name__ == '__main__':
    c = ChatCmdHandler()
    init_stdio(c)
    start_reactor()
