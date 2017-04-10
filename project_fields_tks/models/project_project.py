# -*- coding: utf-8 -*-
# Copyright 2016-2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models, fields


class ProjectProject(models.Model):
    _inherit = 'project.project'

    stairs = fields.Integer(
        string='Stairs',
    )
    weight_stairs = fields.Float(
        string='Weight',
    )
    handrail = fields.Float(
        string='Handrail',
        help='Length of the handrails in meters.'
    )
    weight_handrail = fields.Float(
        string='Weight',
    )
    cad_partner_id = fields.Many2one(
        "res.partner",
        domain=[('cad_partner', '=', True)],
        string="CAD Partner",
    )
    state = fields.Selection([
        ('quotation', 'Quotation'),
        ('sales_order', 'Sales Order'),
        ('wip', 'In Progress'),
        ('invoiced', 'Invoiced'),
        ('done', 'Done')], 'Status',
        # compute='_update_project_state',
        default='quotation',
        store=True
    )
    purchase_line_ids = fields.One2many(
        comodel_name='purchase.order.line',
        inverse_name='project_id',
        string='Purchase Order Lines',
    )


    # below logic needs to be updated!!!
    @api.one
    @api.depends('task_ids.stage_id')
    def _update_project_state(self):
        for task in self.task_ids:
            # if task.stage_id.name == 'In Progress':
            if task.stage_id.sequence == 10:
                self.state = 'wip'
