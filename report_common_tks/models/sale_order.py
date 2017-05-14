# -*- coding: utf-8 -*-
# Copyright 2016-2017 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    transaction_method = fields.Char(
        string="Transaction Method",
    )
    doc_title = fields.Char(
        string="Doc Title",
    )


    @api.multi
    def _prepare_invoice(self):
        res = super(SaleOrder, self)._prepare_invoice()
        res.update({'doc_title': self.doc_title})
        return res
