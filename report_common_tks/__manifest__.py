# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Report Common",
    "summary": "",
    "version": "10.0.1.0.0",
    "category": "Uncategorized",
    "website": "https://www.odoo-asia.com/",
    "author": "Rooms For (Hong Kong) Limited T/A OSCG",
    "license": "AGPL-3",
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
    ],
    "data": [
        'data/paperformat_data.xml',
        'data/res_partner_data.xml',
        'views/res_company_views.xml',
        'views/res_partner_views.xml',
        'views/sale_order_views.xml',
        'views/account_invoice_views.xml',
        'report/common_template.xml',
    ],
    "demo": [
    ],
    "qweb": [
    ]
}
