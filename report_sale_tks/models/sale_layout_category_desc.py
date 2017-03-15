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
    subtotal = fields.Boolean(
        'Add Subtotal',
    )
    pagebreak = fields.Boolean(
        'Add Pagebreak',
    )
    hide_price = fields.Boolean(
        'Hide Price',
    )

    _sql_constraints = [
        ('layout_category_uniq',
         'unique (layout_category_id, sale_order_id)',
         'Multiple entries of a section in an order is not allowed.')
    ]


    @api.multi
    @api.onchange('layout_category_id')
    def onchange_layout_category(self):
        self.ensure_one()
        if self.layout_category_id:
            self.name = self.layout_category_id.name
        else:
            self.name = False
        return

    @api.onchange('hide_price')
    def onchange_hide_price(self):
        if self.hide_price:
            self.subtotal = True
