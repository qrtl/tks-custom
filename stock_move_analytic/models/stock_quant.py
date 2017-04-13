# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from collections import defaultdict
from odoo import api, fields, models


class StockQuant(models.Model):
    _inherit = "stock.quant"

    # override the standard method  # oscg
    def _create_account_move_line(
            self, move, credit_account_id, debit_account_id, journal_id):
        # group quants by cost
        quant_cost_qty = defaultdict(lambda: 0.0)
        for quant in self:
            quant_cost_qty[quant.cost] += quant.qty

        AccountMove = self.env['account.move']
        for cost, qty in quant_cost_qty.iteritems():
            move_lines = move._prepare_account_move_line(
                qty, cost, credit_account_id, debit_account_id)
            if move_lines:
                date = self._context.get(
                    'force_period_date', fields.Date.context_today(self))
                new_account_move = AccountMove.create({
                    'journal_id': journal_id,
                    'line_ids': move_lines,
                    'date': date,
                    'ref': move.picking_id.name})
                new_account_move.post()

            # additional steps  # oscg
            if move.location_id.usage == 'internal' and \
                            move.location_dest_id.usage == 'customer':
                self.create_analytic_line(move, qty, -cost)
            if move.location_id.usage == 'customer' and \
                            move.location_dest_id.usage == 'internal':
                self.create_analytic_line(move, -qty, -cost)

    def create_analytic_line(self, move, qty, cost):
        analytic_line_obj = self.env['account.analytic.line']
        analytic_line_obj.create({
            'name': move.name,
            'date': fields.Date.context_today(self),
            'account_id': move.related_project_id and
                          move.related_project_id.id or False,
            'amount': qty * cost,
            'analytic_type_id': self.env['analytic.type'].search([
                ('analytic_type', '=', 'material_costs')])[0].id,
            'unit_amount': qty,
            'partner_id': False,
            'user_id': self._context.get('uid', False),
            'product_id': move.product_id.id,
            'product_uom_id': False,
            'general_account_id': False,
            'ref': move.picking_id and move.picking_id.name or False,
        })
        return
