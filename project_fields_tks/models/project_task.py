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
        string='Budget Amount',
        # default=0.0,
    )
    currency_id = fields.Many2one(
        related='project_id.currency_id',
        store=True,
        string='Currency',
        readonly=True)

    # @api.onchange('budget_ratio', 'project_id.budget_amt')
    # def onchange_partner(self):
    #     for invoice in self:
    #         invoice.delivery_note = invoice.partner_id.delivery_note
