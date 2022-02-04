# -*- coding: utf-8 -*-
# from odoo import http


# class DeliveryNotePrint(http.Controller):
#     @http.route('/delivery_note_print/delivery_note_print/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/delivery_note_print/delivery_note_print/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('delivery_note_print.listing', {
#             'root': '/delivery_note_print/delivery_note_print',
#             'objects': http.request.env['delivery_note_print.delivery_note_print'].search([]),
#         })

#     @http.route('/delivery_note_print/delivery_note_print/objects/<model("delivery_note_print.delivery_note_print"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('delivery_note_print.object', {
#             'object': obj
#         })
