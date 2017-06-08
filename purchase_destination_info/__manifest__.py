# -*- coding: utf-8 -*-
# Copyright 2017 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "Destination Info in Purchase Order",
    "summary": """
    """,
    "description": """
This module depends on project_purchase_create to for the purpose of
maintaining the context "project_id" for order_line.
    """,
    "version": "10.0.1.0.1",
    "category": "Purchase",
    "website": "https://www.odoo-asia.com/",
    "author": "Quartile Limited",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        "purchase",
        "project_purchase_create",
    ],
    "data": [
        'views/purchase_order_views.xml',
    ],
}
