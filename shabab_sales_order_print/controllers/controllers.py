# -*- coding: utf-8 -*-
# from odoo import http


# class CustomSalesOrderPrint(http.Controller):
#     @http.route('/custom_sales_order_print/custom_sales_order_print/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_sales_order_print/custom_sales_order_print/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_sales_order_print.listing', {
#             'root': '/custom_sales_order_print/custom_sales_order_print',
#             'objects': http.request.env['custom_sales_order_print.custom_sales_order_print'].search([]),
#         })

#     @http.route('/custom_sales_order_print/custom_sales_order_print/objects/<model("custom_sales_order_print.custom_sales_order_print"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_sales_order_print.object', {
#             'object': obj
#         })
