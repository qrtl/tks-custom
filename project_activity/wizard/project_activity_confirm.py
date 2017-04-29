# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models, fields, api, _
from odoo.exceptions import Warning


class ProjectActivityConfirm(models.TransientModel):
    _name = 'project.activity.confirm'
    _description = 'Project activity confirm'

    @api.multi
    def action_activity_confirm(self):
        activity_ids = self._context.get('active_ids', False)
        activities = self.env['project.activity'].browse(activity_ids)
        for activity in activities:
            if not activity.confirmed:
                activity.confirmed = True
        return {'type': 'ir.actions.act_window_close'}
