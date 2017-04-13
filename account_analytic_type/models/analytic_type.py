# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from openerp import fields, models


class AnalyticType(models.Model):
    _name = 'analytic.type'
    _order = 'sequence'

    name = fields.Char(
        string="Name",
        required=True
    )
    analytic_type = fields.Selection(selection=[
        ('sales', 'Sales'),
        ('ev_actual', 'EV (Actual)'),
        ('labour', 'Labour'),
        ('material_costs', 'Material Costs'),
        ('overhead', 'Overhead'),
        ('outsourcing', 'Outsourcing')],
        string='Analytic Type',
        required=True,
    )
    sequence = fields.Integer(
        default=10,
        required=True,
    )
