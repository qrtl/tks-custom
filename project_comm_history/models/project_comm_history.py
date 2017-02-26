# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class ProjectCommHistory(models.Model):
    _name = 'project.comm.history'
    _description = 'Project Communication History'

    task_id = fields.Many2one(
        comodel_name = 'project.task',
        string='Task',
        required=True,
    )
    project_id = fields.Many2one(
        comodel_name = 'project.project',
        related='task_id.project_id',
        string='project',
        required=True,
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
    )
    content = fields.Text(
    )
