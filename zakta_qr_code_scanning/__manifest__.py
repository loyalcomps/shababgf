# -*- coding: utf-8 -*-
{
    'name': "zakta_qr_code_scanning",

    'summary': """
        Qr code Scanning Using Zakta App
        
        **** Fill Company Vat and invoice timestamp""",

    'description': """
       Qr code Scanning Using Zakta App
    """,

    'author': "Loyal IT Solutions PVT LTD",
    'website': "http://www.loyalitsolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account','arabic_invoice_print'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
