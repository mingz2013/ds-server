# -*- coding:utf-8 -*-
"""
Created on 19/06/2017

@author: zhaojm
"""

import os
import sys

# current_path = os.path.dirname(os.path.abspath(__file__))
# source_path = os.path.join(current_path, "../../../")
#
# sys.path.append(os.path.join(source_path, "chat/src/"))
# sys.path.append(os.path.join(source_path, "frame/src/"))

sys.path.append(os.path.dirname("."))

from chat.entity import g

if __name__ == '__main__':
    g.setup_webmgr()
