# -*- coding: utf-8 -*-
# This module and its content is copyright of Technaureus Info Solutions Pvt. Ltd.
# - © Technaureus Info Solutions Pvt. Ltd 2020. All rights reserved.

{
    'name': 'Thermal Invoice',
    'version': '14.0.0.0',
    'category': 'Accounting',
    'summary': 'Print Thermal Invoice',
    'sequence': 1,
    'author': 'Technaureus Info Solutions Pvt. Ltd.',
    'website': "http://www.technaureus.com/",
    'price': 9,
    'currency': 'EUR',
    'license': 'Other proprietary',
    'depends': ['account'],
    'data': [
        'data/paper_format.xml',
        'report/account_report.xml',
        'report/report_invoice.xml',
        'report/invoice_external_layout.xml'
    ],
    'qweb': [],
    'demo': [],
    'images': ['images/main_screenshot.png'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
