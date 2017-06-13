# -*- coding:utf-8 -*-
'''
Created on 13/06/2017

@author: zhaojm
'''
import stackless
from twisted.internet import stdio, reactor

from command import CommandProtocol

stdio.StandardIO(CommandProtocol())

stackless.tasklet(reactor.run)()
reactor.callLater(0, stackless.schedule)
stackless.run()
