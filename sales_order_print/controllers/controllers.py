# -*- coding: utf-8 -*-
# from odoo import http


# class SalesOrderPrint(http.Controller):
#     @http.route('/sales_order_print/sales_order_print/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales_order_print/sales_order_print/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales_order_print.listing', {
#             'root': '/sales_order_print/sales_order_print',
#             'objects': http.request.env['sales_order_print.sales_order_print'].search([]),
#         })

#     @http.route('/sales_order_print/sales_order_print/objects/<model("sales_order_print.sales_order_print"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales_order_print.object', {
#             'object': obj
#         })
