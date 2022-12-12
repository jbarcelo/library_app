# -*- coding: utf-8 -*-
{
    'name': "Library Management",

    'summary': """
        Manage library catalog and book lending
        """,

    'author': "Jaume Barcelo",
    'license': "AGPL-3",
    'website': "http://www.jaumebarcelo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '15.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    'application': True,

    'category': "Services/Library",

    'data':[
        "security/library_security.xml",
        "security/ir.model.access.csv",
        "views/book_view.xml",
        "views/library_menu.xml",
        ],
}
