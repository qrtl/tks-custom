# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    
    project_id = fields.Many2one(
        comodel_name='project.project',
        string="Project"
    )
    related_project_id = fields.Many2one(
        comodel_name='account.analytic.account',
        compute='_update_related_project',
        store=True,
        string="Analytic Account"
    )


    @api.multi
    @api.depends('project_id')
    def _update_related_project(self):
        for line in self:
            if line.project_id:
                line.related_project_id = line.project_id.analytic_account_id
            else:
                line.related_project_id = False
        return

    @api.multi
    def _prepare_invoice_line(self, qty):
        self.ensure_one()
        res = super(SaleOrderLine, self)._prepare_invoice_line(qty=qty)
        if self.related_project_id:
            res.update({'account_analytic_id': self.related_project_id.id})
        return res
