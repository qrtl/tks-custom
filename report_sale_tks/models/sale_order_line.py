# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    _order = 'order_id, layout_category_id, matl_subtotal desc, sequence, id'

    matl_subtotal = fields.Boolean(
        'Material Subtotal',
    )
    remark = fields.Text(
    )


    @api.multi
    @api.onchange('product_id')
    def product_id_change(self):
        res = super(SaleOrderLine, self).product_id_change()
        if self.product_id:
            matl_subtotal = self.product_id.product_tmpl_id.matl_subtotal
        else:
            matl_subtotal = False
        self.update({'matl_subtotal': matl_subtotal})
        return res
