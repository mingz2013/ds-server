# -*- coding:utf-8 -*-
'''
Created on 09/06/2017

@author: zhaojm
'''

import stackless
import sys

from twisted.internet import reactor

stackless.tasklet(reactor.run)()
reactor.callLater(0, stackless.schedule)
stackless.run()
