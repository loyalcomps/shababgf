# -*- coding: utf-8 -*-
# from odoo import http


# class SaleStichingCutting(http.Controller):
#     @http.route('/sale_stitching_cutting/sale_stitching_cutting/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_stitching_cutting/sale_stitching_cutting/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_stitching_cutting.listing', {
#             'root': '/sale_stitching_cutting/sale_stitching_cutting',
#             'objects': http.request.env['sale_stitching_cutting.sale_stitching_cutting'].search([]),
#         })

#     @http.route('/sale_stitching_cutting/sale_stitching_cutting/objects/<model("sale_stitching_cutting.sale_stitching_cutting"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_stitching_cutting.object', {
#             'object': obj
#         })
