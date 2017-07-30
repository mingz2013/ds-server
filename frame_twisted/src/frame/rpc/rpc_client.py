# -*- coding:utf-8 -*-
"""

负责调用外部的rpc接口


"""

__date__ = "30/07/2017"
__author__ = "zhaojm"

from frame.entity.base_client import BaseClient


class RpcClient(BaseClient):
    def __init__(self):
        BaseClient.__init__(self)
        pass

    def get_info(self, id, url, args):
        pass
