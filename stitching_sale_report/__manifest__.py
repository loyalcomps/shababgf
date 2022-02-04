# -*- coding: utf-8 -*-
{
    'name': "stitching_sale_report",

    'summary': """
        stitching_sale_report""",

    'description': """
       stitching_sale_report
    """,

    'author': "Loyal It Solutions PVT LTD",
    'website': "http://www.loyalitsolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/wizard_sale.xml',
        'views/templates.xml',
        'views/views.xml',
        'views/sale_report.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
