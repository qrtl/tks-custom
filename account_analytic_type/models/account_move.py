# -*- coding: utf-8 -*-

from openerp import fields, models, api


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    analytic_type_id = fields.Many2one(
        'analytic.type',
        string='Analytic Type'
    )
