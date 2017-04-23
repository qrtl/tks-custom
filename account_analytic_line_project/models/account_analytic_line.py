# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models, fields, api


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    @api.model
    def _default_analytic_id(self):
        pj_id = self._context.get('default_project_id', False)
        if pj_id:
            return self.env['project.project'].browse(
                pj_id).analytic_account_id
        return False


    pj_id = fields.Many2one(
        comodel_name='project.project',
        compute='_compute_pj_id',
        inverse='_set_account_id',
        store=True,
        string='Associated Project',
    )
    account_id = fields.Many2one(
        'account.analytic.account',
        'Analytic Account',
        required=True,
        ondelete='restrict',
        index=True,
        default=_default_analytic_id,
    )


    @api.multi
    @api.depends('account_id')
    def _compute_pj_id(self):
        for line in self:
            if line.account_id and line.account_id.project_ids:
                line.pj_id = line.account_id.project_ids[0].id

    @api.multi
    def _set_account_id(self):
        for line in self:
            line.account_id = line.pj_id.account_id.id
