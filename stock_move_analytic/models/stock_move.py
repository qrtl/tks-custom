# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    related_project_id = fields.Many2one(
        'account.analytic.account',
        string='Analytic Account',
        help="Analytic account related to stock move."
    )
    need_analytic = fields.Boolean(
        string='Need Analytic Account',
        compute='_compute_need_analytic',
        store=True,
    )

    @api.multi
    @api.depends('location_id', 'location_dest_id')
    def _compute_need_analytic(self):
        for move in self:
            if move.location_id.usage == 'customer' or \
                            move.location_dest_id.usage == 'customer':
                move.need_analytic = True
            else:
                move.need_analytic = False
