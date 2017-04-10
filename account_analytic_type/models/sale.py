# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from openerp import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    analytic_type_id = fields.Many2one(
        'analytic.type',
        string='Analytic Type'
    )


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    analytic_type_id = fields.Many2one(
        'analytic.type',
        string='Analytic Type',
    )

    @api.multi
    def _prepare_invoice_line(self, qty):
        res = super(SaleOrderLine, self)._prepare_invoice_line(qty=qty)
        res.update({'analytic_type_id': self.analytic_type_id.id})
        return res