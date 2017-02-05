# -*- coding: utf-8 -*-
# Copyright 2016 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    project_id = fields.Many2one(
        comodel_name='project.project',
        compute='_get_project',
        store=True,
        string='Project'
    )


    @api.multi
    @api.depends('account_analytic_id')
    def _get_project(self):
        for ln in self:
            if ln.account_analytic_id:
                ln.project_id = ln.account_analytic_id.project_ids[0]
            else:
                ln.project_id = False
        return
