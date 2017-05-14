# -*- coding: utf-8 -*-
# Copyright 2016-2017 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'account.invoice'

    doc_title = fields.Char(
        string="Doc Title",
    )
