# -*- coding: utf-8 -*-
# Copyright 2017 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'


    destination = fields.Char(
        string='Destination',
        help="The value set in this field will default to the corresponding "
             "field in lines.",
    )
