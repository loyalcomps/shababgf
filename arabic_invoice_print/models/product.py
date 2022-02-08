from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    name_arabic = fields.Text(store='True')