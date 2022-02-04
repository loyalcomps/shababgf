from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'uom.uom'

    name_arabic = fields.Char(store='True',string="Arabic Name")
    name_print = fields.Char(store='True', string="UOM in Print")