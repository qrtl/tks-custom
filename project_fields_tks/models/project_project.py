# -*- coding: utf-8 -*-
# Copyright 2016 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models, fields


class ProjectProject(models.Model):
    _inherit = 'project.project'

    budget_amt = fields.Float(
        string='Budget Amount',
        digits=(16,2),
        default=0.0,
    )
