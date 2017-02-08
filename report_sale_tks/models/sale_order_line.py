# -*- coding: utf-8 -*-
# Copyright 2016 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    category_desc = fields.Char(
        compute='_get_category_desc',
        store=True,
        string='Section Description',
    )


    @api.depends('layout_category_id', 'order_id.category_desc_ids')
    def _get_category_desc(self):
        desc_obj = self.env['sale.layout_category.desc']
        for line in self:
            desc_recs = desc_obj.search([
                ('sale_order_id', '=', line.order_id.id),
                ('layout_category_id', '=', line.layout_category_id.id),
            ])
            if desc_recs:
                line.category_desc = desc_recs[0].name
            else:
                line.category_desc = False
        return
