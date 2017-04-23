# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models, fields


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    so_id = fields.Many2one(
        comodel_name='sale.order',
        related='pj_id.so_id',
        store=True,
        string='Sales Order',
    )
