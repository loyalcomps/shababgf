# -*- coding: utf-8 -*-
# from odoo import http


# class ArabicInvoicePrint(http.Controller):
#     @http.route('/arabic_invoice_print/arabic_invoice_print/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/arabic_invoice_print/arabic_invoice_print/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('arabic_invoice_print.listing', {
#             'root': '/arabic_invoice_print/arabic_invoice_print',
#             'objects': http.request.env['arabic_invoice_print.arabic_invoice_print'].search([]),
#         })

#     @http.route('/arabic_invoice_print/arabic_invoice_print/objects/<model("arabic_invoice_print.arabic_invoice_print"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('arabic_invoice_print.object', {
#             'object': obj
#         })
