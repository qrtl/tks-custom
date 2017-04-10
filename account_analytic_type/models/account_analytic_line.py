# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from openerp import api, fields, models


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    analytic_type_id = fields.Many2one(
        'analytic.type',
        string='Analytic Type',
    )
    related_analytic_type = fields.Selection(
        related="analytic_type_id.analytic_type",
    )


    @api.model
    def create(self, vals):
        if vals.get('general_account_id', False) and\
            vals['general_account_id'] and not\
                vals.get('analytic_type_id', False):
            account_obj = self.env['account.account']
            account = account_obj.browse(vals['general_account_id'])
            vals.update(analytic_type_id=account.analytic_type_id.id)
        # assumption: project_id is included only for timesheet entries
        if vals.get('project_id', False):
            analytic_type_id = self.env['analytic.type'].search([
                ('analytic_type', '=', 'labour')])[0].id
            vals.update(analytic_type_id=analytic_type_id)
        return super(AccountAnalyticLine, self).create(vals)

    @api.onchange('general_account_id')
    def _onchange_analytic_type_id(self):
        self.analytic_type_id = self.general_account_id.analytic_type_id
