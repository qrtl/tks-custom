# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class ProjectTaskComplete(models.TransientModel):
    _name = 'project.task.complete'
    _description = 'Project task complete'

    @api.multi
    def action_task_done(self):
        task_ids = self._context.get('active_ids', False)
        # self.env['project.task'].browse(task_ids).action_task_done()
        self.env['project.task'].browse(task_ids).action_task_done()
        return {'type': 'ir.actions.act_window_close'}
