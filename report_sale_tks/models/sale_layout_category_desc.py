# -*- coding: utf-8 -*-
# Copyright 2016 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class SaleLayoutCategoryDesc(models.Model):
    _name = 'sale.layout_category.desc'
    _description = 'Sales Layout Category Description'

    layout_category_id = fields.Many2one(
        comodel_name='sale.layout_category',
        string='Layout Category',
        required=True,
    )
    sale_order_id = fields.Many2one(
        comodel_name='sale.order',
        string='Sales Order',
        readonly=True,
    )
    name = fields.Char(
        string='Description',
    )


    @api.multi
    @api.onchange('layout_category_id')
    def onchange_layout_category(self):
        self.ensure_one()
        self.name = self.layout_category_id.name
        return
