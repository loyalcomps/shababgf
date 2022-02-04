from odoo import api, fields, models

class Company(models.Model):

    _inherit = "res.company"

    header_image = fields.Binary(string="Header Image")
    footer_image = fields.Binary(string="Footer Image")
    company_arabic_name = fields.Char(string="Company Arabic Name", store="True")
    # header_center_image = fields.Binary(string="Header Center Image")
    # header_right_image = fields.Binary(string="Header Right Image")

