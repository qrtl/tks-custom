# -*- coding: utf-8 -*-
# Copyright 2016-2017 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "Project Fields",
    "summary": "",
    "version": "10.0.1.4.1",
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
        "project",
        "purchase",
        "hr_timesheet",
    ],
    "data": [
        'security/ir.model.access.csv',
        'views/res_partner_views.xml',
        'views/project_task_category_views.xml',
        'data/project_task_category_data.xml',
    ],
    "demo": [
    ],
    "qweb": [
    ]
}
