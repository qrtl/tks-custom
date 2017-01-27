# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': "Create Project from Sales",
    'version': "10.0.1.0.0",
    'author': "Rooms For (Hong Kong) Limited T/A OSCG",
    'website': "https://www.odoo-asia.com/",
    'category': "Sales",
    'license': "AGPL-3",
    'depends': [
        'sales_team',
        'project_task_analytic',
    ],
    'data': [
        'wizard/sale_order_project_wizard.xml',
        'views/sale_order_view.xml',
        'views/project_view.xml',
    ],
    "application": False,
    "installable": True,
}
