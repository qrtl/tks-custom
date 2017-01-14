# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import Warning


class ProjectTaskComplete(models.TransientModel):
    _name = 'project.task.complete'
    _description = 'Project task complete'

    @api.multi
    def action_task_done(self):
        task_ids = self._context.get('active_ids', False)
        tasks = self.env['project.task'].browse(task_ids)
        if not all(task.stage_id.stage_state == 'to_do' for task in tasks):
            raise Warning(_('All selected tasks must be in "To Do" state'))
        else:
            tasks.action_task_done()
        return {'type': 'ir.actions.act_window_close'}
