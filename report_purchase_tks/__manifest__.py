# -*- coding: utf-8 -*-
# Copyright 2017 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "Purchase Document Print",
    "summary": "",
    "version": "10.0.1.0.0",
    "category": "Purchases",
    "website": "https://www.odoo-asia.com/",
    "author": "Quartile Limited",
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "purchase",
        "report_common_tks",
    ],
    "data": [
        'views/purchase_order_views.xml',
        'report/purchase_report_order.xml',
    ],
}
