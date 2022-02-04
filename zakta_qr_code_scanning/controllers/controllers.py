# -*- coding: utf-8 -*-
# from odoo import http


# class ZaktaQrCodeScanning(http.Controller):
#     @http.route('/zakta_qr_code_scanning/zakta_qr_code_scanning/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/zakta_qr_code_scanning/zakta_qr_code_scanning/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('zakta_qr_code_scanning.listing', {
#             'root': '/zakta_qr_code_scanning/zakta_qr_code_scanning',
#             'objects': http.request.env['zakta_qr_code_scanning.zakta_qr_code_scanning'].search([]),
#         })

#     @http.route('/zakta_qr_code_scanning/zakta_qr_code_scanning/objects/<model("zakta_qr_code_scanning.zakta_qr_code_scanning"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('zakta_qr_code_scanning.object', {
#             'object': obj
#         })
