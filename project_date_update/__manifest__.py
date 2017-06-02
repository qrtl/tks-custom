# -*- coding: utf-8 -*-
# Copyright 2017 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    'name': "Wizard to Update Project Dates",
    'version': "10.0.1.0.1",
    'author': "Quartile Limited T/A OSCG",
    'website': "https://www.odoo-asia.com/",
    'category': "Project",
    'license': "LGPL-3",
    'depends': [
        'project_fields_tks',
    ],
    'data': [
        'wizard/project_date_update_wizard.xml',
    ],
    "application": False,
    "installable": True,
}
