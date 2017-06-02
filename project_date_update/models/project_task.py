# -*- coding: utf-8 -*-
# Copyright 2017 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api


class ProjectTask(models.Model):
    _inherit = 'project.task'

    days_project_due = fields.Integer(
        'Days to Project Due',
        help='Standard number of days until the project due date.'
    )
