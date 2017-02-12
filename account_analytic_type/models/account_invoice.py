# -*- coding: utf-8 -*-

from openerp import fields, models, api


class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    analytic_type_id = fields.Many2one(
        'analytic.type',
        related='account_id.analytic_type_id',
        string='Analytic Type'
    )
