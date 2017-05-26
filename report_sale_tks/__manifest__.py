# -*- coding: utf-8 -*-
# Copyright 2017 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "Sales Document Print",
    "summary": "",
    "version": "10.0.1.3.1",
    "category": "Sales",
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
