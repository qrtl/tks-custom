# -*- coding: utf-8 -*-
# Copyright 2016 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models, fields


class ProjectTaskType(models.Model):
    _inherit = 'project.task.type'

    # unfinished = fields.Boolean(
    #     'Unfinished Stage'
    # )
    # finished = fields.Boolean(
    #     'Done Stage'
    # )
    stage_state = fields.Selection(
        [('to_do', 'To Do'),
         ('done', 'Done'),
         ('no_need', 'Not Needed')],
        'Stage State',
    )
