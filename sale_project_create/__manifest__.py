# -*- coding: utf-8 -*-
# Copyright 2017 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    'name': "Create Project from Sales",
    'version': "10.0.1.0.2",
    'author': "Quartile Limited",
    'website': "https://www.odoo-asia.com/",
    'category': "Sales",
    'license': "LGPL-3",
    'depends': [
        'sales_team',
        'sale_line_analytic',
        'project_task_analytic',
    ],
    'data': [
        'wizard/sale_order_project_wizard.xml',
        'views/sale_order_views.xml',
    ],
    "application": False,
    "installable": True,
}
