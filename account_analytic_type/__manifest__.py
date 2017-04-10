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
        'sale',
        'purchase',
        'hr_timesheet_sheet',
        'project',
        'stock',
        'sale_stock',
        'analytic',
        'hr_timesheet',
        'project_issue_sheet',
        'hr_expense'
        ],
    'data': [
        'data/analytic_type_data.xml',
        'security/ir.model.access.csv',
        'views/analytic_type_view.xml',
        'views/account_account_views.xml',
        'views/account_analytic_line_views.xml',
        'views/hr_timesheet_sheet_views.xml',
        'views/project_timesheet_view.xml',
        'views/project_issue_view.xml',
        'views/hr_expense.xml',
#         'views/purchase.xml',
#         'views/sale_view.xml',
    ],
    "application": False,
    "installable": True,
}
