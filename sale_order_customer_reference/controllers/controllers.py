# -*- coding: utf-8 -*-
# from odoo import http


# class SaleOrderCustomerReference(http.Controller):
#     @http.route('/sale_order_customer_reference/sale_order_customer_reference/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_order_customer_reference/sale_order_customer_reference/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_order_customer_reference.listing', {
#             'root': '/sale_order_customer_reference/sale_order_customer_reference',
#             'objects': http.request.env['sale_order_customer_reference.sale_order_customer_reference'].search([]),
#         })

#     @http.route('/sale_order_customer_reference/sale_order_customer_reference/objects/<model("sale_order_customer_reference.sale_order_customer_reference"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_order_customer_reference.object', {
#             'object': obj
#         })
