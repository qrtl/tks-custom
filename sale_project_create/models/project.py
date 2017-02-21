# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models, api


class Project(models.Model):
    _inherit = 'project.project'

    sales_amt = fields.Monetary(
        string='Sales Amount',
        compute='_compute_sales_amt',
    )
    is_template = fields.Boolean(
        string="Template Project",
    )
    so_id = fields.Many2one(
        comodel_name='sale.order',
        string='Sales Order',
    )


    @api.multi
    @api.depends('so_id.order_line.project_id', 'so_id.order_line.price_subtotal')
    def _compute_sales_amt(self):
        self.ensure_one()
        amt = 0.0
        for line in self.so_id.order_line:
            if line.project_id == self:
                amt += line.price_subtotal
        self.sales_amt = amt
