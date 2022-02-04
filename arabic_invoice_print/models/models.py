# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools, _
from num2words import num2words

from datetime import datetime, timedelta
import time
from odoo.tools.misc import formatLang, format_date, get_lang


import logging

class AccountMove(models.Model):
    _inherit = 'account.move'

    dn_no = fields.Char(store='True', string="DN No.")
    po_no = fields.Char(store='True', string="PO No.")
    time_stamp = fields.Datetime(string='Time Stamp of E-invoice', readonly=True, store='True')
    bill_invoice = fields.Selection([
        ('Cash', 'Cash'), ('Credit', 'Credit')],
        string='Invoice', default='Cash', store='True')

    def english_amt2words(self,amount, currency, change, precision):
        change_amt = (amount - int(amount)) * pow(10, precision)
        words = '{main_amt} {main_word}'.format(
            main_amt=num2words(int(amount)),
            main_word=currency,
        )
        change_amt = int(round(change_amt))
        # words = words.title()
        if change_amt > 0:
            words += ' and {change_amt} {change_word}'.format(
                change_amt=num2words(change_amt),
                change_word=change,
            )
        words=words.title()
        words = words.replace('And', 'and')
        words = words.replace(',', '')
        return words

    def amount_to_text_arabic(self, amount):
        self.ensure_one()
        def _num2words(number, lang):
            try:
                return num2words(number, lang=lang).title()
            except NotImplementedError:
                return num2words(number, lang='en').title()

        if num2words is None:
            logging.getLogger(__name__).warning("The library 'num2words' is missing, cannot render textual amounts.")
            return ""

        formatted = "%.{0}f".format(self.currency_id.decimal_places) % amount
        parts = formatted.partition('.')
        integer_value = int(parts[0])
        fractional_value = int(parts[2] or 0)

        lang = self.env['res.lang'].with_context(active_test=False).search([('code', '=', 'ar_001')])
        amount_words = tools.ustr('{amt_value} {amt_word}').format(
                        amt_value=_num2words(integer_value, lang=lang.iso_code),
                        amt_word='ريال',
                        )
        if not self.currency_id.is_zero(amount - integer_value):
            amount_words += ' ' + _('و') + tools.ustr(' {amt_value} {amt_word}').format(
                        amt_value=_num2words(fractional_value, lang=lang.iso_code),
                        amt_word='هللة',
                        )
        amount_words = _('فقط') + ' ' + amount_words
        return amount_words

    def _get_bill_invoice_arabic(self):
        for line in self:
            if line.bill_invoice=="Cash":
                return "السيولة النقدية"
            elif line.bill_invoice=="credit":
                return "تنسب إليه"
            else:
                return ""

    def _get_username(self):
        value=self.env.user.name

        return value

    def _get_Bank(self):
        value1 = self.env.company
        _Bankid = self.env['res.partner.bank'].search([('company_id', '=', value1.id),('bring_in_invoice_print','=','true'),('partner_id','=',value1.partner_id.id)])

        return _Bankid

    @api.onchange('invoice_date')
    def set_timestamp(self):
        time_stamp_field = ''
        time_stamp_field_org = ''
        for move in self:
            if move.invoice_date:
                move.time_stamp = move.invoice_date
                date_time = fields.datetime.now()
                time_stamp_field = time_stamp_field + str(date_time.hour) + ":" + str(date_time.minute) + ":" + str(
                    date_time.second)

                time_stamp_field_org = str(move.invoice_date.year) + "-" + str(move.invoice_date.month) + "-" + str(
                    move.invoice_date.day) + " " + time_stamp_field

                update_date = datetime.strptime(time_stamp_field_org, '%Y-%m-%d %H:%M:%S')

                move.time_stamp = update_date

        return

    def action_post(self):
        res = super(AccountMove, self).action_post()
        for move in self:
            if not move.time_stamp:
                move.time_stamp = fields.datetime.now()
        return res

class account_move_line(models.Model):
    _inherit = 'account.move.line'


    def _calc_subtotal(self):
        for line in self:
            subtotal_amount=0
            for l in self.move_id.invoice_line_ids:
                subtotal_amount =subtotal_amount+ ((l.quantity) * (l.price_unit))

            return subtotal_amount

class AccountPaymentTerm(models.Model):

    _inherit = "account.payment.term"

    payment_term_arabic = fields.Char(string="Payment Terms (Arabic)")



class AccountMoveReversal(models.TransientModel):
    _inherit= 'account.move.reversal'
    _description = 'Account Move Reversal'

    def _prepare_default_reversal(self, move):
        res = super(AccountMoveReversal, self)._prepare_default_reversal(move)
        inv_date=move.is_invoice(include_receipts=True) and (self.date or move.date) or False
        time_stamp_field = ''
        time_stamp_field_org = ''

        date_time = fields.datetime.now()
        time_stamp_field = time_stamp_field + str(date_time.hour) + ":" + str(date_time.minute) + ":" + str(
            date_time.second)
        time_stamp_field_org = str(inv_date.year) + "-" + str(inv_date.month) + "-" + str(
            inv_date.day) + " " + time_stamp_field
        update_date = datetime.strptime(time_stamp_field_org, '%Y-%m-%d %H:%M:%S')

        return {
            'ref': _('Reversal of: %s, %s') % (move.name, self.reason) if self.reason else _('Reversal of: %s') % (
                move.name),
            'date': self.date or move.date,
            'invoice_date': move.is_invoice(include_receipts=True) and (self.date or move.date) or False,
            'journal_id': self.journal_id and self.journal_id.id or move.journal_id.id,
            'invoice_payment_term_id': None,
            'auto_post': True if self.date > fields.Date.context_today(self) else False,
            'invoice_user_id': move.invoice_user_id.id,

            'time_stamp': update_date,

        }


