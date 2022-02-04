# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime

from datetime import datetime, timedelta, time

class ProductTemplate(models.Model):
    _inherit = 'product.product'

    name_arabic = fields.Text(store=True,related='product_tmpl_id.name_arabic')