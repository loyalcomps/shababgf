# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SlaorderLine(models.Model):
    _inherit = 'sale.order.line'

    length = fields.Float(string="Length(CM)")
    width = fields.Float(string="Width(CM)")
    pcs = fields.Integer(string="PCS")

    @api.onchange('length','width','pcs')
    def onchange_length_width(self):
        cm_sqr = (self.length*self.width)
        m_sqr = cm_sqr/10000
        total_mtrsqr = m_sqr*self.pcs
        self.product_uom_qty = total_mtrsqr

    def _prepare_invoice_line(self, **optional_values):
        res = super(SlaorderLine, self)._prepare_invoice_line(**optional_values)
        res.update({'length': self.length,
                    'width': self.width,
                    'pcs':self.pcs,
                    'name':self.name
                    })
        return res
    def _prepare_procurement_values(self, group_id=False):
        values = super(SlaorderLine,self)._prepare_procurement_values(group_id)
        values.update({'length':self.length,
                        'width':self.width,
                        'pcs':self.pcs})
        return values
class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    length = fields.Float(string="Length(CM)")
    width = fields.Float(string="Width(CM)")
    pcs = fields.Integer(string="PCS")


class StockMove(models.Model):
    _inherit = 'stock.move'

    length = fields.Float(string="Length(CM)")
    width = fields.Float(string="Width(CM)")
    pcs = fields.Integer(string="PCS")

class StockRule(models.Model):
    _inherit = 'stock.rule'
    length = fields.Float(string="Length(CM)")
    width = fields.Float(string="Width(CM)")
    pcs = fields.Integer(string="PCS")
    def _get_custom_move_fields(self):

        fields = super(StockRule, self)._get_custom_move_fields()
        fields += ['length', 'width','pcs']
        return fields
    # def _get_stock_move_values(
    #         self, product_id, product_qty, product_uom, location_id,
    #         name, origin, company_id, values):
    #     print('self',self)
    #     print('sale_line_id',values.get('sale_line_id'))
    #     # print('sale_line_id',values.get('sale_line_id').dd)
    #     if values.get('sale_line_id', False):
    #         sale_line_id = self.env['sale.order.line'].sudo().browse(
    #             values['sale_line_id'])
    #         self.pcs = sale_line_id.pcs
    #         self.length = sale_line_id.length
    #         self.width = sale_line_id.width
            # if sale_line_id.location_id:
            # else:
            #     self.location_src_id = self.picking_type_id.default_location_src_id.id
        # return super(StockRule, self)._get_stock_move_values(
        #     product_id, product_qty, product_uom, location_id,
        #     name, origin, company_id, values)
