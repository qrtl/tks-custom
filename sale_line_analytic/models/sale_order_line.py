# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    
    project_id = fields.Many2one(
        comodel_name='project.project',
        compute='_get_category_desc',
        store=True,
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

    @api.depends('layout_category_id', 'order_id.category_desc_ids')
    def _get_category_desc(self):
        desc_obj = self.env['sale.layout_category.desc']
        for line in self:
            desc_recs = desc_obj.search([
                ('sale_order_id', '=', line.order_id.id),
                ('layout_category_id', '=', line.layout_category_id.id),
            ])
            if desc_recs:
                line.category_desc = desc_recs[0].name
                line.project_id = desc_recs[0].project_id
            else:
                line.category_desc = False
                line.project_id = False
        return
