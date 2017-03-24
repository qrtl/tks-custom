# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models, api


class ProjectCommHistory(models.Model):
    _name = 'project.comm.history'
    _description = 'Project Communication History'

    @api.model
    def _default_user(self):
        return self.env.context.get('user_id', self.env.user.id)

    task_id = fields.Many2one(
        comodel_name='project.task',
        string='Task',
        required=True,
    )
    task_state = fields.Selection(
        related='task_id.state',
        string='Task State',
        store=True,
        readonly=True,
    )
    project_id = fields.Many2one(
        comodel_name='project.project',
        related='task_id.project_id',
        string='project',
        store=True,
    )
    type = fields.Selection(
        selection=[
            ('received', 'Received'),
            ('sent', 'Sent')
        ],
        string='Type',
        required=True,
    )
    date = fields.Date(
        required=True,
        default=fields.Date.context_today,
    )
    content = fields.Text(
        required=True,
    )
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='User',
        default=_default_user,
        required=True,
    )
