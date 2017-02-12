# -*- coding: utf-8 -*-

from openerp import fields, models


class AnalyticType(models.Model):
    _name = 'analytic.type'

    name = fields.Char(
        string="Name",
        required=True
    )
    analytic_type = fields.Selection(selection=[
        ('ev_actual', 'EV (Actual)'),
        ('labour', 'Labour'),
        ('sales', 'Sales'),
        ('overhead', 'Overhead'),
        ('material_costs', 'Material Costs'),
        ('outsourcing', 'Outsourcing')],
        string='Analytic Type',
        required=True,
    )
