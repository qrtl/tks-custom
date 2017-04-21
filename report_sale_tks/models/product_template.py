# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    matl_subtotal = fields.Boolean(
        'Material Subtotal',
    )
    discount_product = fields.Boolean(
        'Discount Product',
        help='If selected, the amount of the quotation line will be deducted '
             'from the total amount to calculate "gross amount"',
    )
