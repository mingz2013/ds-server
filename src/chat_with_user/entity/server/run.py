# -*- coding:utf-8 -*-
'''
Created on 19/06/2017

@author: zhaojm
'''

import os
import sys

current_path = os.path.dirname(os.path.abspath(__file__))
source_path = os.path.join(current_path, "../../")
sys.path.append(source_path)

from chat_server import ChatServer
from core.reactor import start_reactor
from core.factory import init_server

s = ChatServer()
init_server(s)
start_reactor()
