# -*- coding: utf-8 -*-

from openerp import api, fields, models


class AccountAccount(models.Model):
    _inherit = "account.account"

    analytic_type_id = fields.Many2one(
        'analytic.type',
        string='Analytic Type'
    )


class AccountAccountLine(models.Model):
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
        return super(AccountAccountLine, self).create(vals)

    @api.onchange('general_account_id')
    def _onchange_analytic_type_id(self):
        self.analytic_type_id = self.general_account_id.analytic_type_id
