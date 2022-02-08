from odoo import models, fields, api


class PartnerTemplate(models.Model):
    _inherit = 'res.partner'

    name_arabic = fields.Char(store='True', string="Arabic Name")
    vat_name_arabic = fields.Char(store='True', string="Tax ID Arabic")
    phone_name_arabic = fields.Char(store='True', string="Phone Arabic")
    mobile_name_arabic = fields.Char(store='True', string="Mobile Arabic")
    street1_arabic = fields.Char(store='True')
    street2_arabic = fields.Char(store='True')
    condition = fields.Char(string="Conditions", store='True')
    condition_arabic = fields.Char(string="Conditions Arabic", store='True')
    city_arabic = fields.Char(string="City in Arabic", store='True')
    country_arabic = fields.Char(string="Country in Arabic", store='True')



class ResBank(models.Model):

    _inherit = 'res.partner.bank'

    bank_name_arabic = fields.Char(store='True', string="Bank Name Arabic")
    bank_acc_arabic = fields.Char(store='True', string="Account Number Arabic")
    bring_in_invoice_print = fields.Boolean(store='True', string="Bring in Invoice Print")


class PartnerBankTemplate(models.Model):
    _inherit = 'res.bank'

    bank_bic_arabic = fields.Char(store='True', string="Bank Identifier Code Arabic")
    bank_swift_code = fields.Char(store='True', string="Swift Code")
    bank_swift_code_arabic = fields.Char(store='True', string="Swift Code Arabic")








