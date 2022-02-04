# -*- coding: utf-8 -*-
# from odoo import http


# class ShababAdvertising(http.Controller):
#     @http.route('/shabab_advertising/shabab_advertising/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/shabab_advertising/shabab_advertising/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('shabab_advertising.listing', {
#             'root': '/shabab_advertising/shabab_advertising',
#             'objects': http.request.env['shabab_advertising.shabab_advertising'].search([]),
#         })

#     @http.route('/shabab_advertising/shabab_advertising/objects/<model("shabab_advertising.shabab_advertising"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('shabab_advertising.object', {
#             'object': obj
#         })
