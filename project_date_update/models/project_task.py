# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models, api


class ProjectTask(models.Model):
    _inherit = 'project.task'

    days_project_due = fields.Integer(
        'Days to Project Due',
        help='Standard number of days until the project due date.'
    )
