# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models, api


class ProjectActivity(models.Model):
    _name = 'project.activity'
    _description = 'Project Activity'
    _order = 'date desc, id desc'


    task_id = fields.Many2one(
        comodel_name='project.task',
        string='Task',
        required=True,
    )
    task_state = fields.Selection(
        related='task_id.state',
        string='Task State',
        store=True,
        readonly=True,
    )
    project_id = fields.Many2one(
        comodel_name='project.project',
        related='task_id.project_id',
        string='project',
        store=True,
    )
    date = fields.Date(
        required=True,
        default=fields.Date.context_today,
    )
    note = fields.Text(
    )
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='User',
        required=True,
    )
    plan_stairs = fields.Integer(
        string='Stairs (Plan)',
    )
    plan_weight_stairs = fields.Float(
        string='Weight (Plan)',
        compute='_update_plan_vals',
        store=True,
        readonly=True,
    )
    plan_output_amt = fields.Monetary(
        string='Output Amount (Plan)',
        compute='_update_plan_vals',
        store=True,
        readonly=True,
    )
    actual_stairs = fields.Integer(
        string='Stairs (Actual)',
    )
    actual_weight_stairs = fields.Float(
        string='Weight (Actual)',
        compute='_update_actual_vals',
        store=True,
        readonly=True,
    )
    actual_output_amt = fields.Monetary(
        string='Output Amount (Actual)',
        compute='_update_actual_vals',
        store=True,
        readonly=True,
    )
    currency_id = fields.Many2one(
        related='task_id.currency_id',
        store=True,
        string='Currency',
        readonly=True,
    )


    @api.multi
    @api.depends('task_id', 'task_id.budget_amt', 'plan_stairs')
    def _update_plan_vals(self):
        for act in self:
            if act.task_id and act.task_id.stairs:
                ratio = float(act.plan_stairs) / float(act.task_id.stairs)
                act.plan_weight_stairs = act.task_id.weight_stairs * ratio
                act.plan_output_amt = act.task_id.budget_amt * ratio

    @api.multi
    @api.depends('task_id.budget_amt', 'actual_stairs')
    def _update_actual_vals(self):
        for act in self:
            if act.task_id and act.task_id.stairs:
                ratio = float(act.actual_stairs) / float(act.task_id.stairs)
                act.actual_weight_stairs = act.task_id.weight_stairs * ratio
                act.actual_output_amt = act.task_id.budget_amt * ratio
