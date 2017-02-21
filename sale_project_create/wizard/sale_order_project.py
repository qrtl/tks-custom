# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class SaleOrderProject(models.TransientModel):
    _name = 'sale.project'

    @api.model
    def _default_description(self):
        context = dict(self._context or {})
        active_ids = context.get('active_ids', [])
        active_model = context.get('active_model', False)
        if active_model:
            order = self.env[active_model].browse(active_ids)
            if order:
                return order.doc_title
        return ''


    project_template_id = fields.Many2one(
        'project.project',
        string="Project Template",
        required=True,
    )
    description = fields.Char(
        required=True,
        default=_default_description,
    )
    start_date = fields.Date(
        string="Start Date",
        required=True,
        default=fields.Date.context_today,
    )
    end_date = fields.Date(
        string="End Date",
        required=True,
        default=fields.Date.context_today,
    )


    @api.multi
    def create_project(self):
        context = dict(self._context or {})
        active_ids = context.get('active_ids', [])
        active_model = context.get('active_model', False)
        order = self.env[active_model].browse(active_ids)
        default = {
            'name': order.partner_id.name + " " + order.name + " " +
                    self.description,
            'date_start': self.start_date,
            'date': self.end_date,
            # 'sales_amt': order.amount_untaxed,
            'partner_id': order.partner_id.id,
            'is_template': False,
            'so_id': order.id,
        }
        new_project_id = self.project_template_id.sudo().copy(default)
        # analytic_account_id = new_project_id.analytic_account_id.id
        # order.write({
        #     'sale_project_id': new_project_id.id,
        #     'project_id': analytic_account_id,
        # })
        action_id = self.env.ref('project.open_view_project_all_config')
        action = action_id.read([])[0]
        action['domain'] = \
            "[('id','in', ["+','.join(map(str, [new_project_id.id]))+"])]"
        return action
