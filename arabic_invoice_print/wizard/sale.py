# from odoo import api, fields, models
#
#
# class SaleAdvancePaymentInv(models.TransientModel):
#
#     _inherit = "sale.advance.payment.inv"
#     picking_id = None
#
#     def create_invoices(self):
#         res = super(SaleAdvancePaymentInv, self).create_invoices()
#         print(self.give_picking_id(), 'cre inv')
#         stock_obj = self.env['stock.picking'].search([("id", '=', self.give_picking_id())])
#         invoice_id = self.env['account.move'].search(['|', ('id', '=', res['res_id']), ('id', '!=', res['res_id'])])
#         print('res_id', res['res_id'])
#         invoice_id.write({"dn_no": stock_obj.name})
#         return res
#
#     def default_get(self, values):
#         result = super(SaleAdvancePaymentInv, self).default_get(values)
#         active_id = self.env.context.get('active_id')  # current sale order
#         sale_order_obj = self.env['sale.order'].search([('id', '=', active_id)])  # sale order obj
#         sale_name = sale_order_obj.name  # sale order name
#         picking_obj = self.env['stock.picking'].search([('origin', '=', sale_name)])  # picking object
#         self.copy_picking_id(picking_obj.id)
#         print(self.env.context, "context")
#         return result
#
#     def copy_picking_id(self, pick_id):
#         SaleAdvancePaymentInv.picking_id = pick_id
#
#     def give_picking_id(self):
#         return SaleAdvancePaymentInv.picking_id
