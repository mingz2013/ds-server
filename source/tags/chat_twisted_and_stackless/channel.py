# -*- coding:utf-8 -*-
"""
Created on 13/06/2017

@author: zhaojm
"""
import stackless

chan_command_to_client = stackless.channel()
chan_client_to_command = stackless.channel()
