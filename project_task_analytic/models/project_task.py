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
    state = fields.Selection(
        string='State',
        related='stage_id.stage_state',
        readonly=True,
    )
    analytic_line_id = fields.Many2one(
        comodel_name='account.analytic.line',
        string='Analytic Line',
    )


    @api.depends('budget_ratio', 'project_id.budget_amt')
    def _update_budget_amt(self):
        for task in self:
            task.budget_amt = task.project_id.budget_amt * task.budget_ratio \
                              / 100

    @api.multi
    def action_task_done(self):
        stage_obj = self.env['project.task.type']
        stage_done = stage_obj.search([('stage_state', '=', 'done')])[0]
        analytic_line_obj = self.env['account.analytic.line']
        for task in self:
            task.write({'stage_id': stage_done.id})
            if task.project_id.analytic_account_id:
                analytic_line_id = analytic_line_obj.create(
                    {'name': task.name,
                     'date': fields.Date.context_today(self),
                     'account_id': task.project_id.analytic_account_id.id,
                     'task_id': task.id,
                     'unit_amount': False,
                     'amount': task.budget_amt,
                     'partner_id': task.project_id.partner_id.id,
                     'product_id': False,
                     'product_uom_id': False,
                     'general_account_id': False,
                     'ref': task.project_id.name,
                     }
                )
                task.analytic_line_id = analytic_line_id

    @api.multi
    def action_task_undo(self):
        stage_obj = self.env['project.task.type']
        stage_todo = stage_obj.search([('stage_state', '=', 'to_do')])[0]
        for task in self:
            task.write({'stage_id': stage_todo.id})
            if task.analytic_line_id:
                task.analytic_line_id.unlink()
