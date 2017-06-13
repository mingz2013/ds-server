# -*- coding:utf-8 -*-
'''
Created on 13/06/2017

@author: zhaojm
'''

from sys import stdin

import stackless


def echo_msg(msg):
    print msg


def get_msg():
    print 'get_msg...1'
    stackless.schedule()
    print 'get_msg...2'
    stackless.schedule()
    print 'get_msg...3'
    # print msg


stackless.tasklet(echo_msg)(1)

stackless.tasklet(get_msg)()

stackless.tasklet(echo_msg)(2)

stackless.run()
