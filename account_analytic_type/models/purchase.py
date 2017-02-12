# -*- coding: utf-8 -*-

from openerp import fields, models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    analytic_type_id = fields.Many2one(
        'analytic.type',
        string='Analytic Type'
    )
