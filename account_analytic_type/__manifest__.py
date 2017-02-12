# -*- coding: utf-8 -*-
# Copyright 2016 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': "Analytic Type Entries",
    'version': "10.0.1.0.0",
    'author': "Rooms For (Hong Kong) Limited T/A OSCG",
    'website': "https://www.odoo-asia.com/",
    'category': "Accounting",
    'license': "AGPL-3",
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
        'data/analytic_type_demo_data.xml',
        'security/ir.model.access.csv',
        'views/analytic_type_view.xml',
        'views/account_view.xml',
        'views/analytic_view.xml',
        'views/hr_timesheet_sheet_views.xml',
        'views/project_timesheet_view.xml',
        'views/project_issue_view.xml',
        'views/account_invoice.xml',
        'views/account_move.xml',
        'views/hr_expense.xml',
#         'views/purchase.xml',
#         'views/sale_view.xml',
    ],
    "application": False,
    "installable": True,
}
