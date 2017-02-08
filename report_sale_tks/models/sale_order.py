# -*- coding: utf-8 -*-
# Copyright 2016 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    category_desc_ids = fields.One2many(
        comodel_name='sale.layout_category.desc',
        inverse_name='sale_order_id',
        string='Section Description',
    )
