# -*- coding: utf-8 -*-
# from odoo import http


# class C:\users\vimbai\desktop\assessment\part2(http.Controller):
#     @http.route('/c:\users\vimbai\desktop\assessment\part2/c:\users\vimbai\desktop\assessment\part2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/c:\users\vimbai\desktop\assessment\part2/c:\users\vimbai\desktop\assessment\part2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('c:\users\vimbai\desktop\assessment\part2.listing', {
#             'root': '/c:\users\vimbai\desktop\assessment\part2/c:\users\vimbai\desktop\assessment\part2',
#             'objects': http.request.env['c:\users\vimbai\desktop\assessment\part2.c:\users\vimbai\desktop\assessment\part2'].search([]),
#         })

#     @http.route('/c:\users\vimbai\desktop\assessment\part2/c:\users\vimbai\desktop\assessment\part2/objects/<model("c:\users\vimbai\desktop\assessment\part2.c:\users\vimbai\desktop\assessment\part2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('c:\users\vimbai\desktop\assessment\part2.object', {
#             'object': obj
#         })
