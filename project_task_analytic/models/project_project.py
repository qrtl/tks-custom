# -*- coding: utf-8 -*-
# Copyright 2016 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class ProjectProject(models.Model):
    _inherit = 'project.project'

    sales_amt = fields.Monetary(
        string='Sales Amount',
    )
    currency_id = fields.Many2one(
        "res.currency",
        string="Currency",
        required=True
    )
    labor_ratio = fields.Float(
        string='Labor Ratio (%)',
        digits=(16, 2),
        default=0.0
    )
    budget_amt = fields.Monetary(
        string='Budget Amount',
        compute='_update_budget_amt',
        store=True,
    )


    @api.multi
    @api.depends('sales_amt', 'labor_ratio')
    def _update_budget_amt(self):
        for pj in self:
            pj.budget_amt = pj.sales_amt * pj.labor_ratio / 100
        return
