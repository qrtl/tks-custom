# -*- coding: utf-8 -*-
# Copyright 2016-2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Project Task Analytic",
    "summary": "",
    "version": "10.0.1.1.0",
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
        "project",
        "project_fields_tks",
    ],
    "data": [
        'views/project_task_type_views.xml',
        'views/project_task_views.xml',
        'views/account_analytic_line_views.xml',
        'wizard/project_task_complete_view.xml',
    ],
    "demo": [
    ],
    "qweb": [
    ]
}
