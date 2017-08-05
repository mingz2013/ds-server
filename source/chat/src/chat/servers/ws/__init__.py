# -*- coding:utf-8 -*-
"""
"""
__date__ = "30/07/2017"
__author__ = "zhaojm"

from chat.servers.ws.entity import Entity

e = Entity()


# def init_server(ip, port, url):
#     e.init_rpc()
#     e.init_acceptor(ip, port, url)


def init_server(cfg):
    e.init_rpc()
    e.init_acceptor(cfg['ip'], cfg['port'], cfg['url'])
