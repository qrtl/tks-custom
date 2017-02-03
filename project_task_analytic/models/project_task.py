# -*- coding: utf-8 -*-
# Copyright 2016 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import Warning


class ProjectTask(models.Model):
    _inherit = 'project.task'

    budget_ratio = fields.Float(
        string='Budget Ratio (%)',
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
    def create_analytic_line(self):
        self.ensure_one()
        analytic_line_obj = self.env['account.analytic.line']
        analytic_line_id = analytic_line_obj.create(
            {'name': self.name,
             'date': fields.Date.context_today(self),
             'account_id': self.project_id.analytic_account_id.id,
             'project_id': False,  # to not show the record in timesheet
             'task_id': self.id,
             'unit_amount': False,
             'amount': self.budget_amt,
             'partner_id': self.project_id.partner_id.id,
             'user_id': self.user_id.id,
             'product_id': False,
             'product_uom_id': False,
             'general_account_id': False,
             'ref': self.project_id.name,
             }
        )
        self.analytic_line_id = analytic_line_id

    @api.multi
    def action_task_done(self):
        stage_obj = self.env['project.task.type']
        stage_done = stage_obj.search([('stage_state', '=', 'done')])[0]
        for task in self:
            task.stage_id = stage_done
            if task.project_id.analytic_account_id:
                task.create_analytic_line()

    @api.multi
    def action_task_undo(self):
        stage_obj = self.env['project.task.type']
        stage_todo = stage_obj.search([('stage_state', '=', 'to_do')])[0]
        for task in self:
            task.write({'stage_id': stage_todo.id})
            if task.analytic_line_id:
                task.analytic_line_id.unlink()

    @api.multi
    def try_update_stage(self, stage):
        self.ensure_one()
        res = {}
        from_state = self.stage_id.stage_state
        to_state = stage.stage_state
        if not (from_state and to_state):
            res = {'warning': _('Stage State must be set for Stages.')}
        if from_state == 'done' and to_state == 'no_need':
            res = {'warning': _('You are not allowed to move task from "Done"'
                                ' to "No Need".')}
        if from_state == 'no_need' and to_state == 'done':
            res = {'warning': _('You are not allowed to move task from'
                                ' "No Need" to "Done".')}
        if from_state == "to_do" and to_state == "done":
            self.create_analytic_line()
        if from_state == "done" and to_state == "to_do":
            if self.analytic_line_id:
                self.analytic_line_id.unlink()
        # update color
        if to_state == "no_need":
            self.color = 1  # gray color
        elif to_state == "done":
            self.color = 6  # default color
        elif to_state == "to_do":
            self.color = 0  # default color
        return res

    @api.multi
    def write(self, vals):
        if 'stage_id' in vals:
            new_stage = self.env['project.task.type'].browse(vals['stage_id'])
            for task in self:
                message = task.try_update_stage(new_stage)
                if message and message.get('warning'):
                    raise Warning(message.get('warning'))
        res = super(ProjectTask, self).write(vals)
        return res
