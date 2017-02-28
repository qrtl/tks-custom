# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class ProjectDateUpate(models.TransientModel):
    _name = 'project.date.update'

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
    def update_project_dates(self):
        return
