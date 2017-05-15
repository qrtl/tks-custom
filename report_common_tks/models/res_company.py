# -*- coding: utf-8 -*-
# Copyright 2016-2017 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class Company(models.Model):
    _inherit = 'res.company'

    chop = fields.Binary(
        "Company Chop Image",
        attachment=True,
    )
    bank_details = fields.Text(
        string="Bank Details",
        translate=True,
    )
