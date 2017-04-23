# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "Adjustments to Sales Views",
    "summary": "",
    "version": "10.0.1.0.0",
    "category": "Sales",
    "website": "https://www.odoo-asia.com/",
    "author": "Rooms For (Hong Kong) Limited T/A OSCG",
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "pre_init_hook": "",
    "post_init_hook": "",
    "post_load": "",
    "uninstall_hook": "",
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "sale",
        "account_analytic_line_sale",
    ],
    "data": [
        'views/sale_order_views.xml',
    ],
    "demo": [
    ],
    "qweb": [
    ]
}
