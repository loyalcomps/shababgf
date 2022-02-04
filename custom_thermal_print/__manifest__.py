# -*- coding: utf-8 -*-
{
    'name': "custom_thermal_print",

    'summary': """
        Thermal Print""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Loyal It Solutiond PVT LTD",
    'website': "http://www.loyalitsolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product','account','thermal_invoice','arabic_invoice_print','account_operating_unit'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'report/account_report.xml',
        'report/report_invoice.xml',
        'report/invoice_external_layout.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
