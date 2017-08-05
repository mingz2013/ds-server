# # -*- coding:utf-8 -*-
# """
# """
# __date__ = "30/07/2017"
# __author__ = "zhaojm"
#
# from frame.servers.rpc.rpc_server import RpcServer
#
# s = RpcServer()





def init():
    from frame.entity import log
    log.init_logging()


from frame.servers.rpc.rpc_entity import RpcEntity

s = RpcEntity()
s.init_rpc()
s.start_server("127.0.0.1", 8000)
