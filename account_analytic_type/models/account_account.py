# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from openerp import fields, models


class AccountAccount(models.Model):
    _inherit = "account.account"

    analytic_type_id = fields.Many2one(
        'analytic.type',
        string='Analytic Type'
    )
