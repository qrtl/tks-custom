# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import datetime
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
    def update_task_dates(self, project):
        self.ensure_one()
        for task in project.task_ids:
            task.date_deadline = fields.Date.to_string(
                fields.Date.from_string(project.date) -
                datetime.timedelta(days=task.days_project_due)
            )
        return

    @api.multi
    def update_project_dates(self):
        context = dict(self._context or {})
        active_ids = context.get('active_ids', [])
        active_model = context.get('active_model', False)
        project = self.env[active_model].browse(active_ids)
        default = {
            'date_start': self.start_date,
            'date': self.end_date,
        }
        project.write(default)
        self.update_task_dates(project)
        return
