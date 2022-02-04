# -*- coding: utf-8 -*-
{
    'name': "Shabab Advertising",

    'summary': """
        """,

    'description': """
        Shabab Advertising
    """,

    'author': "Shabab",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sale',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','sale_management','account','arabic_invoice_print','stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/sale_print.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
