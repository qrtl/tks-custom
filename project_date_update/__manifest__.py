# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': "Wizard to Update Project Dates",
    'version': "10.0.1.0.0",
    'author': "Rooms For (Hong Kong) Limited T/A OSCG",
    'website': "https://www.odoo-asia.com/",
    'category': "Project",
    'license': "AGPL-3",
    'depends': [
        'project_fields_tks',
    ],
    'data': [
        'wizard/project_date_update_wizard.xml',
    ],
    "application": False,
    "installable": True,
}
