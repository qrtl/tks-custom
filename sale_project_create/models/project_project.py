# -*- coding: utf-8 -*-
# Copyright 2017 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api


class Project(models.Model):
    _inherit = 'project.project'

    sales_amt = fields.Monetary(
        string='Sales Amount',
        compute='_compute_sales_amt',
        store=True,
    )
    is_template = fields.Boolean(
        string="Template Project",
    )
    so_id = fields.Many2one(
        comodel_name='sale.order',
        string='Sales Order',
    )


    @api.multi
    @api.depends('so_id.order_line.project_id',
                 'so_id.order_line.price_subtotal')
    def _compute_sales_amt(self):
        for project in self:
            amt = 0.0
            for line in project.so_id.order_line:
                if line.project_id == project:
                    amt += line.price_subtotal
            project.sales_amt = amt
