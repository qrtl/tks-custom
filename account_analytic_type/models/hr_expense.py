# -*- coding: utf-8 -*-

from openerp import fields, models


class HrExpense(models.Model):
    _inherit = "hr.expense"

    analytic_type_id = fields.Many2one(
        'analytic.type',
        string='Analytic Type'
    )
