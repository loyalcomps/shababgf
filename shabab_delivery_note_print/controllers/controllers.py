# -*- coding: utf-8 -*-
# from odoo import http


# class CustomDeliveryNote(http.Controller):
#     @http.route('/custom_delivery_note/custom_delivery_note/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_delivery_note/custom_delivery_note/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_delivery_note.listing', {
#             'root': '/custom_delivery_note/custom_delivery_note',
#             'objects': http.request.env['custom_delivery_note.custom_delivery_note'].search([]),
#         })

#     @http.route('/custom_delivery_note/custom_delivery_note/objects/<model("custom_delivery_note.custom_delivery_note"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_delivery_note.object', {
#             'object': obj
#         })
