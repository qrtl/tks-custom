# -*- coding: utf-8 -*-

from odoo import api, fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    @api.multi
    def action_done(self):
        result = super(StockMove, self).action_done()
        for rec in self:
            if rec.procurement_id.sale_line_id.related_project_id:
                sale_order_line = rec.procurement_id.sale_line_id
                self.create_analytic_entry(sale_order_line)
        return

    @api.multi
    def create_analytic_entry(self, line):
        analytic_line_obj = self.env['account.analytic.line']
        analytic_line_id = analytic_line_obj.create(
            {'name': line.name,
             'account_id': line.related_project_id.id,
             'amount': line.price_unit,
             'date': fields.Date.context_today(self),
             'project_id': line.project_id.id,
             'task_id': False,
             'unit_amount': False,
             'partner_id': False,
             'user_id': False,
             'product_id': line.product_id.id,
             'product_uom_id': False,
             'general_account_id': False,
             'ref': False,
             }
        )
        return
