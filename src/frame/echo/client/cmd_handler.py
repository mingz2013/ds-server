# -*- coding:utf-8 -*-
'''
Created on 19/06/2017

@author: zhaojm
'''

from frame.entity.cmd_handler import CmdHandler
from echo_client import EchoClient
from frame.core.reactor import init_client


class EchoCmdHandler(CmdHandler):
    def __init__(self):
        CmdHandler.__init__(self)
        self.echo_client = EchoClient(self)
        self.conn = None
        pass

    def __conn_to_server(self, ip, port):
        init_client(self.echo_client, ip, port)

    def on_conn_made(self, conn):
        self.conn = conn
        self.__conn_to_server('localhost', 8888)
        pass

    def on_conn_lost(self, conn, reason):
        self.conn = None

    def on_msg(self, conn, msg):
        # print 'on msg on cmd handler'
        self.echo_client.sendLine(msg)
        pass

    def on_client_msg(self, client, msg):
        self.conn.sendLine(msg)
        pass
