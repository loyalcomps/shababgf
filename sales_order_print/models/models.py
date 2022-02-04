# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools, _
from num2words import num2words


import logging

class SaleOrder(models.Model):
    _inherit = "sale.order"

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

    class sale_order_line(models.Model):
        _inherit = 'sale.order.line'

        def _calc_subtotal(self):
            for line in self:
                subtotal_amount = 0
                for l in self.order_id.order_line:
                    subtotal_amount = subtotal_amount + ((l.product_uom_qty) * (l.price_unit))

                return subtotal_amount



