# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Project Activities",
    "summary": "",
    "version": "10.0.1.2.0",
    "category": "Project",
    "website": "https://www.odoo-asia.com/",
    "author": "Rooms For (Hong Kong) Limited T/A OSCG",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "pre_init_hook": "",
    "post_init_hook": "",
    "post_load": "",
    "uninstall_hook": "",
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "project_fields_tks",
        "project_task_analytic",
    ],
    "data": [
        'security/ir.model.access.csv',
        'views/project_activity_views.xml',
        'views/project_task_views.xml',
        'wizard/project_activity_confirm_view.xml',
    ],
    "demo": [
    ],
    "qweb": [
    ]
}
