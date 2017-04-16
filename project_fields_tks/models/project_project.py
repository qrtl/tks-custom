# -*- coding: utf-8 -*-
# Copyright 2016-2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models, fields


class ProjectProject(models.Model):
    _inherit = 'project.project'

    type = fields.Selection(
        [('stairs', 'Stairs'),
         ('handrail', 'Handrail')],
        required=True,
    )
    stairs = fields.Integer(
        string='Stairs (sets)',
    )
    handrail = fields.Float(
        string='Handrail (m)',
        help='Length of the handrails in meters.'
    )
    weight = fields.Float(
        string='Weight (kg)',
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
        default='quotation',
        store=True
    )
    purchase_line_ids = fields.One2many(
        comodel_name='purchase.order.line',
        inverse_name='project_id',
        string='Purchase Order Lines',
    )
