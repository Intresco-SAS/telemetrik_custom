# -*- coding: utf-8 -*-
# from odoo import http


# class Telemetrik(http.Controller):
#     @http.route('/telemetrik/telemetrik/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/telemetrik/telemetrik/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('telemetrik.listing', {
#             'root': '/telemetrik/telemetrik',
#             'objects': http.request.env['telemetrik.telemetrik'].search([]),
#         })

#     @http.route('/telemetrik/telemetrik/objects/<model("telemetrik.telemetrik"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('telemetrik.object', {
#             'object': obj
#         })
