# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Sales Document Print",
    "summary": "",
    "version": "10.0.1.0.0",
    "category": "Sales",
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
        "stock",
        "report_common_tks",
    ],
    "data": [
        'security/ir.model.access.csv',
        'views/product_template_views.xml',
        'views/sale_layout_category_desc_views.xml',
        'views/sale_order_views.xml',
        'report/sale_report_quotation.xml',
    ],
    "demo": [
    ],
    "qweb": [
    ]
}
