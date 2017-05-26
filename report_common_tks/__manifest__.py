# -*- coding: utf-8 -*-
# Copyright 2016-2017 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "Report Common",
    "summary": "",
    "version": "10.0.1.1.1",
    "category": "Uncategorized",
    "website": "https://www.odoo-asia.com/",
    "author": "Quartile Limited",
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
