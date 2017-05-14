# -*- coding: utf-8 -*-
# Copyright 2017 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "Adjustments to Project Views",
    "summary": "",
    "version": "10.0.1.3.0",
    "category": "Project",
    "website": "https://www.odoo-asia.com/",
    "author": "Quartile Limited",
    "license": "LGPL-3",
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
        "project_date_update",
        "sale_project_create",
        "account_analytic_line_project",
        "project_purchase_create",
    ],
    "data": [
        'views/project_task_views.xml',
        'views/project_project_views.xml',
    ],
    "demo": [
    ],
    "qweb": [
    ]
}
