# -*- coding: utf-8 -*-
# Copyright 2017 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api, _
from odoo.exceptions import UserError


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

    @api.multi
    def _prepare_invoice_line(self, qty):
        res = super(SaleOrderLine, self)._prepare_invoice_line(qty)
        res.update({'remark': self.remark})
        return res

    # not allow multiple units of measure for one section + matl_subtotal
    @api.constrains('product_uom', 'matl_subtotal', 'layout_category_id')
    def _check_uom(self):
        if self.layout_category_id and self.matl_subtotal:
            if self.order_id.order_line.filtered(
                    lambda x: x.layout_category_id == self.layout_category_id
                    and x.matl_subtotal == True
                    and x.product_uom != self.product_uom
            ):
                raise UserError(_(
                    'Only one UoM should be used per section for lines with '
                    'material subtotal selection.'))
