# -*- coding: utf-8 -*-
# Copyright 2016 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models, fields


class ProjectProject(models.Model):
    _inherit = 'project.project'

    budget_amt = fields.Monetary(
        string='Budget Amount',
    )
    currency_id = fields.Many2one(
        "res.currency",
        string="Currency",
        required=True
    )
