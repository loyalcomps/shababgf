# -*- coding: utf-8 -*-
# from odoo import http


# class ShababEinvoice(http.Controller):
#     @http.route('/shabab_einvoice/shabab_einvoice/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/shabab_einvoice/shabab_einvoice/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('shabab_einvoice.listing', {
#             'root': '/shabab_einvoice/shabab_einvoice',
#             'objects': http.request.env['shabab_einvoice.shabab_einvoice'].search([]),
#         })

#     @http.route('/shabab_einvoice/shabab_einvoice/objects/<model("shabab_einvoice.shabab_einvoice"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('shabab_einvoice.object', {
#             'object': obj
#         })
