# -*- coding: utf-8 -*-
# Copyright 2016 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models, fields


class ProjectTask(models.Model):
    _inherit = 'project.task'

    budget_ratio = fields.Float(
        string='Budget Ratio',
        digits=(16, 2),
        default=0.0
    )
    budget_amt = fields.Monetary(
        compute='_update_budget_amt',
        store=True,
        string='Budget Amount',
    )
    currency_id = fields.Many2one(
        related='project_id.currency_id',
        store=True,
        string='Currency',
        readonly=True)


    @api.onchange('budget_ratio')
    def onchange_budget_ratio(self):
        for task in self:
            task.budget_amt = task.project_id.budget_amt * task.budget_ratio \
                              / 100

    @api.depends('project_id.budget_amt')
    def _update_budget_amt(self):
        for task in self:
            task.budget_amt = task.project_id.budget_amt * task.budget_ratio \
                              / 100
