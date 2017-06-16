# -*- coding:utf-8 -*-
'''
Created on 10/06/2017

@author: zhaojm
'''

import stackless
from twisted.internet import reactor
from twisted.internet.protocol import connectionDone
from twisted.protocols.basic import LineReceiver


class ChatServerProtocol(LineReceiver):
    def __init__(self, chat):
        self.chat = chat

    def connectionMade(self):
        pass

    def connectionLost(self, reason=connectionDone):
        pass

    def lineReceived(self, line):
        stackless.tasklet(self.parse_msg)(line)
        reactor.callLater(0, stackless.schedule)

    def parse_msg(self, msg):

        if "create_user" in msg:
            name = msg['name']
            password = msg['password']

            user_id = self.chat.account_mgr.account_create(name, password)
            if user_id:
                pass
        elif "login" in msg:
            pass
        else:
            user_id = msg['user_id']
            self.chat.on_msg(user_id, msg)
        pass

    def send_to_client(self, msg):
        self.sendLine(msg)
