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
    task_category_id = fields.Many2one(
        related='task_id.category_id',
        string='Task Category',
        store=True,
        readonly=True,
    )
    task_state = fields.Selection(
        related='task_id.state',
        string='Task State',
        store=True,
        readonly=True,
    )
    task_qty = fields.Float(
        compute='_compute_task_qty',
        string='Task Qty',
        store=True,
        readonly=True,
    )
    """ avoid making this field required at model level to avoid error at
    creation through task form view """
    project_id = fields.Many2one(
        comodel_name='project.project',
        related='task_id.project_id',
        string='project',
        store=True,
        # required=True,
    )
    project_type = fields.Selection(
        related='project_id.type',
        store=True,
        string='Project Type',
        readonly=True,
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
    plan_qty = fields.Float(
        string='Qty (Plan)',
    )
    plan_weight = fields.Float(
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
    actual_qty = fields.Float(
        string='Qty (Actual)',
    )
    actual_weight = fields.Float(
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
    analytic_line_ids = fields.One2many(
        comodel_name='account.analytic.line',
        inverse_name='activity_id',
        string="Analytic Line",
    )
    hours = fields.Float(
        default=0.0
    )


    @api.multi
    @api.depends('task_id', 'task_id.stairs', 'task_id.handrail')
    def _compute_task_qty(self):
        for act in self:
            if act.task_id and act.project_type == 'stairs':
                act.task_qty = float(act.task_id.stairs)
            elif act.task_id and act.project_type == 'handrail':
                act.task_qty = act.task_id.handrail
            else:
                act.task_qty = 0.0

    @api.multi
    @api.depends('task_id', 'task_qty', 'task_id.budget_amt', 'plan_qty')
    def _update_plan_vals(self):
        for act in self:
            if act.task_id and act.task_qty:
                ratio = act.plan_qty / act.task_qty
                act.plan_weight = act.task_id.weight * ratio
                act.plan_output_amt = act.task_id.budget_amt * ratio

    @api.multi
    @api.depends('task_qty', 'task_id.budget_amt', 'actual_qty')
    def _update_actual_vals(self):
        for act in self:
            if act.task_id and act.task_qty:
                ratio = act.actual_qty / act.task_qty
                act.actual_weight = act.task_id.weight * ratio
                act.actual_output_amt = act.task_id.budget_amt * ratio

    @api.multi
    def write(self, vals):
        self.ensure_one()
        if 'hours' in vals or 'note' in vals:
            if self.analytic_line_ids:
                self.analytic_line_ids.unlink()
            if vals['hours']:  # no action if 'hours' has been changed to zero
                self.create_analytic_line(vals)
        res = super(ProjectActivity, self).write(vals)
        return res

    @api.multi
    def create_analytic_line(self, vals):
        self.ensure_one()
        """
        'analytic_type_id' gets proposed by account_analytic_type
        'amount' gets calculated with standard logic
        """
        analytic_line_vals = {
            'name': 'note' in vals and vals['note'] or self.note or '-',
            'date': fields.Date.context_today(self),
            'account_id': self.project_id.analytic_account_id.id,
            'project_id': self.project_id.id,
            'task_id': self.task_id.id,
            'activity_id': self.id,
            'unit_amount': 'hours' in vals and vals['hours'] or self.hours,
            'partner_id': self.project_id.partner_id.id,
            'user_id': self.user_id.id,
            'product_id': False,
            'product_uom_id': False,
            'general_account_id': False,
            'ref': self.project_id.name,
        }
        self.env['account.analytic.line'].create(analytic_line_vals)
