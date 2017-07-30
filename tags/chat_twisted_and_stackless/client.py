# -*- coding:utf-8 -*-
"""
Created on 13/06/2017

@author: zhaojm
"""
from twisted.internet import stdio


def init_client():
    from command_protocol import CommandProtocol
    stdio.StandardIO(CommandProtocol())


if __name__ == '__main__':
    init_client()
    from run import start_reactor

    start_reactor()
