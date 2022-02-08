# -*- coding: utf-8 -*-
{
    'name': "E-INVOICE",

    'summary': """
        """,

    'description': """
        This module is arabic version of sales invoice print
    """,

    'author': "LOYAL IT SOLUTIONS",
    'website': "https://www.loyalitsolutions.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account','sale','product', 'web'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/invoice_menu.xml',
        'views/arabic_invoices_temp.xml',
        'views/product.xml',
        'views/res_partner.xml',
        'views/uom.xml',
        'views/res_company_view.xml',
        'views/layout.xml',

        'wizard/base_document_layout_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
