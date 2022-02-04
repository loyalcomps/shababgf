# -*- coding: utf-8 -*-
# from odoo import http


# class StitchingSaleReport(http.Controller):
#     @http.route('/stitching_sale_report/stitching_sale_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/stitching_sale_report/stitching_sale_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('stitching_sale_report.listing', {
#             'root': '/stitching_sale_report/stitching_sale_report',
#             'objects': http.request.env['stitching_sale_report.stitching_sale_report'].search([]),
#         })

#     @http.route('/stitching_sale_report/stitching_sale_report/objects/<model("stitching_sale_report.stitching_sale_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('stitching_sale_report.object', {
#             'object': obj
#         })
