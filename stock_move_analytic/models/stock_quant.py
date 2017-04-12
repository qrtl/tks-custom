# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from collections import defaultdict
from odoo import api, fields, models


class StockQuant(models.Model):
    _inherit = "stock.quant"

    def _create_account_move_line(self, move, credit_account_id, debit_account_id, journal_id):
        # group quants by cost
        quant_cost_qty = defaultdict(lambda: 0.0)
        for quant in self:
            quant_cost_qty[quant.cost] += quant.qty

        AccountMove = self.env['account.move']
        for cost, qty in quant_cost_qty.iteritems():
            move_lines = move._prepare_account_move_line(qty, cost, credit_account_id, debit_account_id)
            if move_lines:
                date = self._context.get('force_period_date', fields.Date.context_today(self))
                new_account_move = AccountMove.create({
                    'journal_id': journal_id,
                    'line_ids': move_lines,
                    'date': date,
                    'ref': move.picking_id.name})
                new_account_move.post()

            if move.location_id.usage == 'internal' and \
                            move.location_dest_id.usage == 'customer':
                self.create_analytic_entry(move, qty, cost)
            if move.location_id.usage == 'customer' and \
                            move.location_dest_id.usage == 'internal':
                self.create_analytic_entry(move, -qty, cost)

    def create_analytic_entry(self, move, qty, cost):
        analytic_line_obj = self.env['account.analytic.line']
        analytic_line_obj.create({
            'name': move.name,
            'date': fields.Date.context_today(self),
            'account_id': move.related_project_id and move.related_project_id.id or False,
            'amount': qty * cost,
            'analytic_type_id': self.env['analytic.type'].search([
                ('analytic_type', '=', 'material_costs')])[0].id,
            'unit_amount': False,
            'partner_id': False,
            'user_id': False,
            'product_id': move.product_id.id,
            'product_uom_id': False,
            'general_account_id': False,
            'ref': move.picking_id and move.picking_id.name or False,
        })
        return



            # @api.multi
    # def action_done(self):
    #     res = super(StockMove, self).action_done()
    #     for move in self:
    #         # if move.procurement_id.sale_line_id.related_project_id:
    #         #     sale_order_line = move.procurement_id.sale_line_id
    #         # elif move.related_project_id:
    #
    #         move.create_analytic_entry()
    #     return res
    #
    # @api.one
    # def create_analytic_entry(self):
    #     analytic_line_obj = self.env['account.analytic.line']
    #     analytic_line_id = analytic_line_obj.create(
    #         {'name': self.name,
    #          'date': fields.Date.context_today(self),
    #          'account_id': self.related_project_id and self.related_project_id.id or False,
    #          'amount': self.price_unit,
    #          'analytic_type_id': self.env['analytic.type'].search([
    #              ('analytic_type', '=', 'material_costs')])[0].id,
    #          'unit_amount': False,
    #          'partner_id': False,
    #          'user_id': False,
    #          'product_id': self.product_id.id,
    #          'product_uom_id': False,
    #          'general_account_id': False,
    #          'ref': False,
    #          }
    #     )
    #     return
