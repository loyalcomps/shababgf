# -*- coding: utf-8 -*-
{
    'name': "shabab_sales_order_print",

    'summary': """
       """,

    'description': """
        
    """,

    'author': "LOYAL IT SOLUTIONS",
    'website': "https://www.loyalitsolutions.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale', 'web','arabic_invoice_print','sales_order_print','shabab_advertising'],

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
