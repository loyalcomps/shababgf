# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError,ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    cutting_user = fields.Many2one('res.users', string="Cutting User")
    cutting_completed = fields.Boolean('Cutting Completed',default=False)
    stitching_user = fields.Many2one('res.users', string="Stitching User")
    stitching_completed = fields.Boolean("Stitching Completed",default=False)

    def cutting_completion(self):
        for i in self:
            if not i.cutting_user:
                raise UserError(_('Please enter The Cutting User'))
            else:
                i.cutting_completed = True

    def stitching_completion(self):
        for i in self:
            if not i.stitching_user:
                raise UserError(_('Please enter The Stitching User'))
            else:
                i.stitching_completed = True


class Picking(models.Model):
    _inherit = "stock.picking"


    def button_validate(self):
        res = super(Picking, self).button_validate()
        for i in self:
            if i.sale_id and i.picking_type_code == "outgoing":
                if i.sale_id.stitching_completed != True:
                    raise ValidationError(_('Stitch in Progress.'))

        return res

