# -*- coding: utf-8 -*-
# from odoo import http


# class CustomThermalPrint(http.Controller):
#     @http.route('/custom_thermal_print/custom_thermal_print/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_thermal_print/custom_thermal_print/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_thermal_print.listing', {
#             'root': '/custom_thermal_print/custom_thermal_print',
#             'objects': http.request.env['custom_thermal_print.custom_thermal_print'].search([]),
#         })

#     @http.route('/custom_thermal_print/custom_thermal_print/objects/<model("custom_thermal_print.custom_thermal_print"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_thermal_print.object', {
#             'object': obj
#         })
