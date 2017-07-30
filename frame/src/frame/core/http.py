# # -*- coding:utf-8 -*-
# """
# Created on 26/06/2017
#
# @author: zhaojm
# """
#
# # from twisted.web.resource import Resource
# # from twisted.web.proxy import ReverseProxyResource
# # from twisted.application import internet, service, strports
# # from twisted.web import static, server
# # from twisted.web.resource import Resource
# # from twisted.web.server import Site
# from twisted.web.wsgi import WSGIResource
# from twisted.internet import reactor
#
#
# class HttpApp(object):
#     def __init__(self):
#         pass
#
#     def get_wsgi(self, app):
#         # root = Resource()
#         wsgi_res = WSGIResource(reactor, reactor.getThreadPool(), app)
#         # root.putChild('api', flask_site)
#         # static_file = static.File("webroot")
#         # root.putChild('static', static_file)
#         return wsgi_res
