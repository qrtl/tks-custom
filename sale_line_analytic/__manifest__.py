# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': "Sale Line Analytic",
    'version': "10.0.1.0.0",
    'author': "Rooms For (Hong Kong) Limited T/A OSCG",
    'website': "https://www.odoo-asia.com/",
    'category': "Sales",
    'license': "AGPL-3",
    'depends': [
        'sale',
        'project',
        'report_sale_tks',
    ],
    'data': [
        'views/sale_layout_category_desc_views.xml',
        'views/sale_order_line_views.xml',
        'views/sale_order_views.xml',
    ],
    "application": False,
    "installable": True,
}
