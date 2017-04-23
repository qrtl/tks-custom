# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    def _default_analytic_id(self):
        project_id = self._context.get('project_id', False)
        if project_id:
            return self.env['project.project'].browse(
                project_id).analytic_account_id.id
        return False


    account_analytic_id = fields.Many2one(
        'account.analytic.account',
        string='Analytic Account',
        default=_default_analytic_id,
    )
