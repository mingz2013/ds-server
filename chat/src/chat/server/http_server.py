# -*- coding:utf-8 -*-
'''
Created on 26/06/2017

用于提供http服务,

静态页面服务
静态文件服务, 图片, 压缩包等
后台管理功能


@author: zhaojm
'''
from frame.entity.base_server import BaseServer
from flask import Flask
from twisted.internet import reactor


class HttpServer(BaseServer):
    def __init__(self):
        BaseServer.__init__(self)

    def on_conn_lost(self, conn, reason):
        pass

    def on_conn_made(self, conn):
        pass

    def on_msg(self, conn, msg):
        conn.sendLine(msg)
        pass
