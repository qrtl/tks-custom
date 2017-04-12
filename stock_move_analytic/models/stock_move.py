# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    related_project_id = fields.Many2one(
        'account.analytic.account',
        string='Analytic Account',
        help="Analytic account related to stock move.")
