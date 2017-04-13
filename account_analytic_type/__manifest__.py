# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    'name': "Analytic Type",
    'version': "10.0.1.0.0",
    'author': "Rooms For (Hong Kong) Limited T/A OSCG",
    'website': "https://www.odoo-asia.com/",
    'category': "Accounting",
    'license': "LGPL-3",
    'depends': [
        'account',
        'hr_timesheet_sheet',
        'project',
        'stock_account',
        'hr_expense'
        ],
    'data': [
        'data/analytic_type_data.xml',
        'security/ir.model.access.csv',
        'views/analytic_type_views.xml',
        'views/account_account_views.xml',
        'views/account_analytic_line_views.xml',
        'views/hr_timesheet_sheet_views.xml',
        'views/project_timesheet_view.xml',
        'views/hr_expense_views.xml',
    ],
    "application": False,
    "installable": True,
}
