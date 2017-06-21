# -*- coding:utf-8 -*-
'''
Created on 19/06/2017

@author: zhaojm
'''

import os
import sys

current_path = os.path.dirname(os.path.abspath(__file__))
source_path = os.path.join(current_path, "../../../../")
sys.path.append(os.path.join(source_path, "chat/src/"))
sys.path.append(os.path.join(source_path, "frame/src/"))

from chat_server import ChatServer
from frame.core.reactor import start_reactor
from frame.core.reactor import init_server

if __name__ == '__main__':
    s = ChatServer()
    init_server(s, '0.0.0.0', 8888)
    start_reactor()
