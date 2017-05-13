# -*- coding: utf-8 -*-
# Copyright 2017 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "Project Activities",
    "summary": "",
    "version": "10.0.1.3.0",
    "category": "Project",
    "website": "https://www.odoo-asia.com/",
    "author": "Quartile Limited",
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
        "sale_timesheet",
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
